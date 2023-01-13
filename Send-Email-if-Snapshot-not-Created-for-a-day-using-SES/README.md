# Send-Email-if-Snapshot-not-Created-for-a-day-using-SES:

First look at the High Level Architecture Diagram then lambda-funtion.py and then Explanation to Implement.

1. High Level Architecture Diagram (snapshot-count-architecture.jpg):
	This file shows the Architecture to implement this mini-project using some AWS services.
	CloudWatch will trigger the lambda funtion on a specific time every day, Lamda Funtion 
	will take a total count of the snapshot and will send email using SES(Simple Email Service)
	if count is 0(means no snapshot were available for the day) else will not send email.	
	User will receive email if snapshot count is 0.

2. Lambda Funtion (lambda-funtion.py):
	In Lambda Funtion file (lambda-funtion.py), first we will count the number of snapshots
	available on the day. Then will create condition for count==0 and count>0.
	If count==0, we will create a template to send mail using SES. Using boto3 documentation,
	we will try to send email using send_email utility.
	Remember to replace your tomail and frommail.

3. Explanation:
	Lambda will require some permission to access ec2:describe and ses:send_email policy.
	As when creating Lambda funtion, We let AWS to create a role for us, then we add EC2 
	and SES Policy to that  role.
	We then create a CloudWatch Event to trigger the Lambda funtion at a specific time 
	every day.
	You would also need to add email and should be verified on AWS SES. Else will through 
	the error.
	After verifing, you should first Test the Lambda funtion. Whether it is working finr or
	not.
