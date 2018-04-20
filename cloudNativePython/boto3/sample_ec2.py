
import sys

import boto3
from botocore.exceptions import ClientError
from logall import config_logging

# Configuring and getting a logger object
logger = config_logging()


def main():

    instance_id = 'i-029316a4a1ea81d56'
    if sys.argv[1] != 0:
        action = sys.argv[1].upper()
    else:
        action = 'OFF'

    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    simple_log(response)

    if action == 'ON':
        response = ec2.monitor_instances(InstanceIds=[instance_id])

        # Do a dryrun first to verify permissions
        try:
            ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(object=e):
                raise

        try:
            ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            simple_log(response)
        except ClientError as e:
            if 'DryRunOperation' not in str(object=e):
                simple_log(e)
    else:
        response = ec2.unmonitor_instances(InstanceIds=[instance_id])

        # Do a dryrun first to verify permissions
        try:
            ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(object=e):
                raise

        try:
            ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
            simple_log(response)
        except ClientError as e:
            if 'DryRunOperation' not in str(object=e):
                simple_log(e)

    logger.info('Response %s', response)


def simple_log(response):
    logger.info('Response %s', response)


if __name__ == '__main__':
    main()
