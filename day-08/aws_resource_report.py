import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Initialize the EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Fetch all instances
response = ec2_client.describe_instances()

# Iterate through the reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
