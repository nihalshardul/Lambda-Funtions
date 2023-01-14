import json
import boto3
from datetime import datetime, timezone


def lambda_handler(event, context):
    # TODO implement
    today = datetime.now(timezone.utc).date()
    client = boto3.client('ec2')
    response = client.describe_snapshots(OwnerIds=['self'])
    snapshots = response['Snapshots']
    count = 0
    for snapshot in snapshots:
        start_time = snapshot['StartTime'].date()
        if start_time == today:
            count += 1
    
    print("Today's Snapshot count : ", count)
    
    if count == 0:
        snsArn = '<enter-sns-topic-arn>'
        subject = 'Warning : Snapshots not been created today.'
        body = """
                     <br>
                     This is to inform you that, Snapshots has not ben created today.
                     <br>
                     Please take a note of the date, and if possible try to take snapshots today.
             """
        sns = boto3.client('sns')
        response = sns.publish(
            TopicArn=snsArn,
            Message=body ,
            Subject=subject
        )
        print("The mail is sent successfully")
    else:
        print ("Snapshot created...")
        print ("No need to send mail.")
    
    return 0
