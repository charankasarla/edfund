import boto3
import base64
import json
import os
from datetime import datetime

s3_client = boto3.client('s3')
BUCKET_NAME = os.getenv('BUCKET_NAME')
def lambda_handler(event, context):
    """
    AWS Lambda function to store a file in an S3 bucket.
    The file should be provided in the event payload as Base64-encoded content.

    Example event:
    {
        "fileName": "example.pdf",
        "fileContent": "Base64-encoded content here"
    }
    """
    try:
        file_name = event.get('fileName')
        file_content_base64 = event.get('fileContent')

        if not file_name or not file_content_base64:
            raise ValueError("Both 'fileName' and 'fileContent' must be provided in the event object.")

        file_content = base64.b64decode(file_content_base64)

        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%SZ')
        s3_key = f"uploads/{timestamp}-{file_name}"

        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=file_content
        )

        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"File '{file_name}' has been successfully uploaded to S3.",
                'fileUrl': file_url
            })
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }
