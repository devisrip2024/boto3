import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\Admin\Desktop\batch code\boto3\hello.txt" , 'elasticbeanstalk-us-east-2-878088820643', 'hello.txt')
