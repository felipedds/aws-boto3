import boto3

# First form
aws_management_console = boto3.session.Session(region_name='us-east-1') # Get AWS Management Console
iam_console = aws_management_console.resource('iam') # Get IAM Console
for user in iam_console.users.all():
    print(user.name)

# Second form
iam = boto3.resource('iam')
for user in iam.users.all():
    print(user.name)