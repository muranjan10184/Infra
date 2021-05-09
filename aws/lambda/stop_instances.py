
import boto3
import json

region = 'us-east-2'
instances = ['i-09dfa949583d328bd']
rds_identifier = 'vy-rds'
ec2 = boto3.client('ec2', region_name=region)
rds = boto3.client('rds')

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    rds.stop_db_instance(DBInstanceIdentifier=rds_identifier)

