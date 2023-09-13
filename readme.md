## Create two acconuts AccountA and AccountB and s3 buckets within that accounts 
AccountA has awssourcebucketa and AccountB has targetaccountb

## S3 bucket access from AccountB 

In Account B, we need to create an IAM role that allows cross-account access to the S3 bucket so we have to selected trusted entity as aws account
Go to IAM create a role accessaccounta
Under Selected trusted entity select aws account
Attach permission for amazons3fullaccess and after creation under policies and edit the trust relationship with trustrelation.json

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/2e691453-6666-4105-9b37-d94ddc8d8e9b">

 Create a Role in accountA 

Go to IAM>Roles>Create role
Under Selected trusted entity select aws service
Select service as lambda
Under persmision add s3access and name the role as lambdarole and add cloudwatchwatchaccess as permission 

Edit the policy of role lambdarole created and select inline policy as json 

create policy accountbaccess.json and getandput.json


## Create a lambda function 

create lambda function and select permisions as lamdarole 
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/5cb70899-d57b-4743-91b6-22f5391171c2">


## Add trigger to lamda function object replication

add trigger to lamda function as oject created event 

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/4cfd5591-438d-4e2e-bfc8-260325c6cbf7">


## Under code source paste lambdafunc.py
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/86534688-228e-4815-a03d-f63a259bf367">










