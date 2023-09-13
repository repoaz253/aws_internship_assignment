import os
import boto3

def lambda_handler(event, context):
    source_bucket = 'SOURCE_BUCKET_NAME'
    source_key = 'SOURCE_OBJECT_KEY'
    destination_bucket = 'DESTINATION_BUCKET_NAME'
    destination_key = 'DESTINATION_OBJECT_KEY'
    
    source_access_key = os.environ['SOURCE_ACCESS_KEY']
    source_secret_key = os.environ['SOURCE_SECRET_KEY']
    destination_access_key = os.environ['DESTINATION_ACCESS_KEY']
    destination_secret_key = os.environ['DESTINATION_SECRET_KEY']

    source_s3 = boto3.client('s3',
        aws_access_key_id=source_access_key,
        aws_secret_access_key=source_secret_key
    )

    destination_s3 = boto3.client('s3',
        aws_access_key_id=destination_access_key,
        aws_secret_access_key=destination_secret_key
    )
    try:
        response = destination_s3.copy_object(
            CopySource={'Bucket': source_bucket, 'Key': source_key},
            Bucket=destination_bucket,
            Key=destination_key
        )
        return {
            'statusCode': 200,
            'body': f'Object copied successfully: {response}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error copying object: {str(e)}'
        }
