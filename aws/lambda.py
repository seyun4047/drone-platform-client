# Upload this code on your AWS LAMBDA
# SET BUCKET_NAME="YOUR_S3_BUCKET_NAME"

# And You need to open your AWS API Gateway
# GET /upload-url
# POST /upload-url
#
# import json
# import boto3
# import uuid
# import os
#
# AWS_REGION = "ap-northeast-2" # SET_YOUR_AWS_REGION
# BUCKET_NAME = os.environ["BUCKET_NAME"]
#
# # S3 client
# s3 = boto3.client("s3", region_name=AWS_REGION)
#
#
# def lambda_handler(event, context):
#     file_type = "jpg"
#     content_type = "image/jpeg"
#     key = f"{uuid.uuid4()}.{file_type}"
#
#     # generate_presigned_post
#     presigned_post = s3.generate_presigned_post(
#         Bucket=BUCKET_NAME,
#         Key=key,
#         Fields={"Content-Type": content_type},
#         Conditions=[
#             {"Content-Type": content_type}
#         ],
#         ExpiresIn=300
#     )
#
#     return {
#         "statusCode": 200,
#         "headers": {
#             "Content-Type": "application/json"
#         },
#         "body": json.dumps({
#             "upload_url": presigned_post['url'],
#             "fields": presigned_post['fields'],
#             "key": key,
#             "content_type": content_type
#         })
#     }
