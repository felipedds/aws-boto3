import boto3

aws_management_console = boto3.session.Session(region_name='us-east-1') # Get AWS Management Console

iam_console_client = aws_management_console.client(service_name='iam', region_name='us-east-1') # IAM Client Object
ec2_console_client = aws_management_console.client(service_name='ec2', region_name='us-east-1') # EC2 Client Object
s3_console_client = aws_management_console.client(service_name='s3', region_name='us-east-1') # S3 Client Object

# List all IAM users using client object
response_iam = iam_console_client.list_users()
for user in response_iam['Users']:
    print(user['UserName'], user['UserId'])

# List all EC2 Instances using client object
response_ec2 = ec2_console_client.describe_instances()
for reservation in response_ec2['Reservations']:
    for instance in response_ec2['Instances']:
        print(instance['InstanceId'])

# List all S3 Instances using client object
response_s3 = s3_console_client.list_buckets()
for bucket in response_s3['Buckets']:
    print(bucket['Name'])