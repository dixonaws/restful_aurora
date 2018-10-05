# restful_aurora
Stand up an API to get data from an Aurora database. Commands here are tested on macOS, but should
work fine on Linux and should be ok for Windows with adjustments. We'll also deploy a sample employee database, 
load some data, and connect it to our API. 

## Get started with Python and Chalice

### Setup a Python virtual environment and activate it
```bash
virtualenv `which python3` venv
source venv/bin/activate
```

### Install AWS Chalice
Chalice is a microframework for writing serverless apps in python. It allows you to quickly 
create and deploy applications that use AWS Lambda. It provides:
- A command line tool for creating, deploying, and managing your app
- A decorator based API for integrating with Amazon API Gateway, Amazon S3, Amazon SNS, Amazon SQS, and other AWS services.
- Automatic IAM policy generation

> Run this command from the restful_aurora directory 

```bash
pip install -r requirements.txt
```

Now, create a new API
```bash
chalice new-project restful_aurora_api
```

enter the restful_aurora_api directory, and issue the following command to deploy the API locally:
```bash
chalice local
```

> This will start a basic web server on your local machine and start serving the RESTful endpoint from localhost:8000

Open a new terminal window and use curl to issue a GET request:

```bash
curl -x GET http://localhost:8000
```

Now, you can deploy the API to AWS API Gateway and Lambda with the following command:
```bash
chalice deploy
```

You should see the following when deployment completes successfully:
```
Creating deployment package.
Creating IAM role: restful_aurora_api-dev
Creating lambda function: restful_aurora_api-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-1:477157386854:function:restful_aurora_api-dev
  - Rest API URL: https://3nel6hbk0e.execute-api.us-east-1.amazonaws.com/api/
```

Now you can test the API with curl:
```bash
curl -X GET https://3nel6hbk0e.execute-api.us-east-1.amazonaws.com/api/ 
```

If all is well, you should see something like this:

```json
{"hello": "world"}
```

Boom! You deployed API Gateway, Lambda, IAM roles, and all of the configuration to serve a basic RESTful API. Now
lets do something more interesting, like accessing a database with that API.

## Create an Aurora database called "employees"
Use the AWS Console to create an Aurora-mysql database called "employees."

## Create a simple database and load some data
Browse to http://www.jackdb.com and create an account. Jackdb is an online SQL client that we'll use to 
connect to the employees database. Use Jackdb to establish a connection to the Aurora database and do the following:
1. Use create_employees_table.sql to create a new table
2. Import employees.csv into the table

## Adjust your API to connect to the database
You can reference the code in ```app.py.txt``` to modify ```app.py``` in your restful_aurora_api directory to return
a list of employees. Note that you'll have to create several Systems Manager Parameter Store values ahead of 
time. See https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html
or ```aws ssm help``` to create values for the database, username, password, etc. per the code in app.py.txt.

## Test your API locally
Run ```chalice local``` and use the curl command to get a listing of employees in the database. For this to work,
you will have to open the security group for your employees database so that you local machine can issue queries against it.

## Deploy to API Gateway and Lambda
If your API worked locally, then issue ```chalice deploy``` to deploy the new code to your RESTful endpoint. This will
update your Lambda function and API Gateway to return the right results.   