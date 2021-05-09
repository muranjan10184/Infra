
import boto3
import json

region = 'us-east-2'
ec2_instances = ['i-09dfa949583d328bd']
rds_identifier = 'vy-rds'
ec2 = boto3.client('ec2', region_name=region)
rds = boto3.client('rds')

def lambda_handler(event, context):
    rds.start_db_instance(DBInstanceIdentifier=rds_identifier)
    ec2.start_instances(InstanceIds=ec2_instances)
    