import json

# import requests


def lambda_handler(event, context):
    print('Hello World')
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
