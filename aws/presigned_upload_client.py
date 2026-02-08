import os
import requests

class PresignedUploadClient:
    """
    Client for uploading files to S3 using a presigned URL
    """

    def __init__(self, server_url):
        self.server_url = server_url.rstrip('/')
        self.upload_endpoint = f"{self.server_url}/upload-url"

    def upload_file(self, file_path):
        """
        Upload a file to S3 and return the uploaded file URL

        Args:
            file_path (str): Path to the file to upload

        Returns:
            str: S3 URL of the uploaded file, or None on failure
        """
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            return None

        try:
            # 1. Request a presigned URL from the server
            file_ext = os.path.splitext(file_path)[1].lstrip('.')
            res = requests.post(
                self.upload_endpoint,
                json={"fileType": file_ext},
                timeout=10
            )

            if res.status_code != 200:
                print(f"Error: Failed to get presigned URL - {res.status_code}")
                return None

            data = res.json()
            upload_url = data["upload_url"]
            fields = data["fields"]
            key = data["key"]

            # 2. Upload the file to S3 using multipart/form-data
            with open(file_path, "rb") as f:
                filename = os.path.basename(file_path)
                files = {"file": (filename, f, "image/jpeg")}
                upload_res = requests.post(
                    upload_url,
                    data=fields,
                    files=files,
                    timeout=30
                )

            if upload_res.status_code in [200, 204]:
                # Build the final S3 file URL
                bucket_name = upload_url.split('.s3.')[0].split('//')[-1]
                region = os.getenv("SERVER_REGION")
                s3_url = f"https://{bucket_name}.s3.{region}.amazonaws.com/{key}"

                print(f"Upload success: {s3_url}")
                return s3_url
            else:
                print(f"Error: Upload failed - {upload_res.status_code}")
                print(upload_res.text)
                return None

        except requests.exceptions.Timeout:
            print("Error: Request timeout")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error: Request failed - {e}")
            return None
        except Exception as e:
            print(f"Error: Unexpected error - {e}")
            return None
