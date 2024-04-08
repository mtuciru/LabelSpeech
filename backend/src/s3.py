from io import BytesIO

import boto3
import botocore.exceptions
import mimetypes

from settings import settings


class S3:
    def __init__(self):
        session = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                        region_name=settings.AWS_REGION)
        self.s3client = session.client(service_name='s3', endpoint_url=settings.AWS_HOST)
        self.create_bucket()

    def get_url(self, fileid: str):
        try:
            self.s3client.head_object(Bucket=settings.AWS_BUCKET, Key=fileid)

            (mime, encoding) = mimetypes.guess_type(fileid, strict=True)
            if not mime:
                return self.s3client.generate_presigned_url("get_object", ExpiresIn=600,
                                                            Params={"Bucket": settings.AWS_BUCKET, "Key": fileid})
            else:
                return self.s3client.generate_presigned_url("get_object", ExpiresIn=600,
                                                            Params={"Bucket": settings.AWS_BUCKET, "Key": fileid,
                                                                    "ResponseContentType": mime})
        except botocore.exceptions.ClientError:
            raise FileNotFoundError("File not found")

    def download_file(self, file, fileid: str):
        try:
            self.s3client.head_object(Bucket=settings.AWS_BUCKET, Key=fileid)
            self.s3client.download_fileobj(settings.AWS_BUCKET, fileid, file)
            file.seek(0)
        except botocore.exceptions.ClientError:
            raise FileNotFoundError("File not found")

    def upload_file(self, file, fileid: str):
        with BytesIO(file) as f:
            self.s3client.upload_fileobj(f, settings.AWS_BUCKET, fileid)

    def create_bucket(self):
        try:
            self.s3client.create_bucket(Bucket=settings.AWS_BUCKET)
        except:
            pass


s3 = S3()
