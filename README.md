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

```bash
pip install chalice
```

Now, enter the restful_aurora_api directory, and issue the following command to deploy the API:
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

## Create an Aurora database called "employees"
Use the AWS Console to create a database called "employees."

## Create a simple database and load some data
Browse to http://www.jackdb.com and create an account. Jackdb is an online SQL client that we'll use to 
connect to the employees database. Use Jackdb to establish a connection to the Aurora database and do the following:
1. Use create_employees_table.sql to create a new table
2. Import employees.csv into the table


