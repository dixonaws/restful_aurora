from chalice import Chalice
import sys
import pymysql
import logging
import boto3
import json

app = Chalice(app_name='restful_aurora_api')
app.debug = True

logging.basicConfig()
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# create a client to the systems manager parameter store
client_ssm=boto3.client('ssm')

# get the database instance's url, username and pwd from the secure string store
param_db_host = client_ssm.get_parameter(
	Name='employees_db_host',
	WithDecryption=True
)

param_db_name = client_ssm.get_parameter(
	Name='employees_db_name',
	WithDecryption=True
)

param_db_username = client_ssm.get_parameter(
	Name='employees_db_username',
	WithDecryption=True
)

param_db_password = client_ssm.get_parameter(
	Name='employees_db_password',
	WithDecryption=True
)

str_db_host = param_db_host['Parameter']['Value']
str_db_name = param_db_name['Parameter']['Value']
str_db_username = param_db_username['Parameter']['Value']
str_db_password = param_db_password['Parameter']['Value']

# logger.log("Using db params: db_username=" + str_db_username + ", db_host=" + str_db_host + ", db_name=" + str_db_name + ", db_password=" + str_db_password)
#
# logger.log("Getting connection to " + str_db_host + "... ")
try:
    conn = pymysql.connect(str_db_host, user=str_db_username, passwd=str_db_password, db=str_db_name, connect_timeout=5)
except:
    # logger.error("ERROR: Unexpected error: Could not connect to database instance.")
    sys.exit()

# logger.log("done")


@app.route('/')
def index():
    return {'help': 'sample restful_aurora API'}

@app.route('/introspect')
def introspect():
    return app.current_request.to_dict()

@app.route('/employee/{employee_id}')
def get_all_employees(employee_id):
	return {'employee_id': employee_id}

@app.route('/employees')
def get_all_employees():
	# create a cursor from the connection and execute a simple SELECT
	cur = conn.cursor(pymysql.cursors.DictCursor)

	cur.execute("SELECT * from employee")

	# fetch one record into an array
	dict_response = cur.fetchall()
	int_number_of_records = cur.rowcount

	# logger.log("Found " + str(int_number_of_records) + " record(s)")

	# logger.log("response: " + dict_response)

	if (int_number_of_records > 0):
		json_result = json.dumps(dict_response)

	else:
		str_message = 'No employee records found.'
		json_result = json.dumps({
			'matches': int_number_of_records,
			'message': str_message,
			'data': {

			}
		})  # json_result

	return json_result

# Here are a few more examples:
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
