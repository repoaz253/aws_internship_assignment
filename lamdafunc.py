import boto3
#boto3 is AWS SDK for aws services to interact with Python

def lambda_handler(event, context):
    source_bucket = 'awssourcebucketA'  
    source_key = 'objectkeyawsSourceBucketA'      
    target_bucket = 'awsTargetBucketB'  
    target_key = 'objectkeyawstargetbucketB'     

    s3_source = boto3.client('s3', region_name='us-east-1', aws_access_key_id='objectkeyawsSourceBucketAid', aws_secret_access_key='objectkeyawsSourceBucketA')
    s3_target = boto3.client('s3', region_name='us-east-1', aws_access_key_id='objectkeyawsTargetBucketBid', aws_secret_access_key='objectkeyawsTargetBucketB')
#Exception handlling 
    try:
        s3_target.copy_object(CopySource={'Bucket': source_bucket, 'Key': source_key}, Bucket=target_bucket, Key=target_key)
        return {
            'statusCode': 200,
            'body':'Object is copied successfully'
        }
    
    except Exception as e:
        error_message = f"There was an Error Copying: {e}"
        return {
            'statusCode': 500,
            'body': error_message
        }
