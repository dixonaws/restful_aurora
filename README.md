# restful_aurora
Stand up an API to get data from an Aurora database. Commands here are tested on macOS, but should
work fine on Linux

## Setup a Python virtual environment and activate it
```bash
virtualenv `which python3` venv
source venv/bin/activate
```

## Install AWS Chalice
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

