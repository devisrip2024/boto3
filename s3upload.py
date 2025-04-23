import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\cloud\OneDrive\Desktop\batchcode's\boto3" , 'elasticbeanstalk-us-east-2-878088820643', 'hello.txt')
