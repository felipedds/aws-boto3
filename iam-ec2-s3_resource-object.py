import boto3

aws_management_console = boto3.session.Session(region_name='us-east-1') # Get AWS Management Console
iam_console_resource = aws_management_console.resource(service_name='iam', region_name='us-east-1')
ec2_console_resource = aws_management_console.resource(service_name='ec2', region_name='us-east-1')
s3_console_resource = aws_management_console.resource(service_name='s3', region_name='us-east-1')

# List all IAM users using resource object
for user in iam_console_resource.users.all():
    print(user.user_name)

# List all EC2 instances using resource object
for instance in ec2_console_resource.instances.all():
    print(instance.instanceid)

# List all S3 buckets using resource object
for bucket in s3_console_resource.buckets.all():
    print(bucket.name)