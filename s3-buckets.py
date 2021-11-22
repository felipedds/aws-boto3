import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all(): # List buckets in Amazon S3
    print(bucket.name)

data = open('requirements.txt', 'rb') # Upload a new file
s3.Bucket('my-bucket').put_object(Key='requirements.txt', Body=data)

