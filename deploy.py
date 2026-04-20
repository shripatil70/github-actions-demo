#pythonfile
import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'github-actions-bucket-demo1', 'index.html')
