import boto3
from pprint import pprint

aws_management_console = boto3.session.Session(region_name='us-east-1') # Gets AWS Management Console.
ec2_console_client = aws_management_console.client(service_name='ec2', region_name='us-east-1') # EC2 Client Object

ec2_instances = ec2_console_client.describe_instances()['Reservations'] 
for reservation in ec2_instances:
    for instance in reservation['Instances']:
        print(f"Image Id: {instance['ImageId']}\n Instance Id: {instance['InstanceId']}\n Launch Time: {instance['LaunchTime']}")
        print('\n')

ec2_volumes = ec2_console_client.describe_volumes()['Volumes']
for volume in ec2_volumes:
    print(f"Volume Id: {volume['VolumeId']}\n State Volume: {volume['State']}")
