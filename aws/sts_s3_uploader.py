import boto3
import os
import time
from datetime import datetime


class DroneS3Uploader:
    def __init__(self, auth_response):
        """
        auth_response: DroneAuthResponse object from server (including 'sts' map)
        """
        # GET STS SETTINGS
        sts_info = auth_response
        print(sts_info)
        self.access_key = sts_info.get('accessKeyId')
        self.secret_key = sts_info.get('secretAccessKey')
        self.session_token = sts_info.get('sessionToken')
        self.bucket_name = sts_info.get('bucketName')
        self.region_name = sts_info.get('region')
        self.expiration = sts_info.get('expiration')

        # S3 CLIENT SETTING
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            aws_session_token=self.session_token,
            region_name=self.region_name
        )

    def upload_image_path(self, drone_id, local_image_path):
        """Uploads a file from a local path and returns the full S3 URL"""
        if not os.path.exists(local_image_path):
            print(f"NO_FILE: {local_image_path}")
            return None

        # image: uploads/droneId/yyyyMMdd_HHmmss.jpg
        ext = os.path.splitext(local_image_path)[1]
        s3_key = f"uploads/{drone_id}/{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"

        try:
            self.s3_client.upload_file(
                local_image_path,
                self.bucket_name,
                s3_key,
                ExtraArgs={'ContentType': 'image/jpeg'}
            )
            full_url = f"https://{self.bucket_name}.s3.{self.region_name}.amazonaws.com/{s3_key}"

            print(f"UPLOAD_SUCCESS: {full_url}")
            return full_url
        except Exception as e:
            print(f"UPLOAD_FAILED: {e}")
            return None