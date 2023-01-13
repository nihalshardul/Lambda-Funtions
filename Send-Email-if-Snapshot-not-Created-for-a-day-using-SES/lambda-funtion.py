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
        frommail= 'nihal@peace.com'
        tomail= 'nihal@peace.com'
        client = boto3.client('ses')
        subject = 'Warning : Snapshots not been created today.'
        body = """
                     <br>
                     This is to inform you that, Snapshots has not ben created today.
                     <br>
                     Please take a note of the date, and if possible try to take snapshots today.
             """
        message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
        response = client.send_email(Source = tomail, Destination = {"ToAddresses": [tomail]}, Message = message) 
        print("The mail is sent successfully")
        print ("Email Send, please check th inbox of : ", tomail)
    else:
        print ("Snapshot created...")
        print ("No need to send mail.")
    return 0
