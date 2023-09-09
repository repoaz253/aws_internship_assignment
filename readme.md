## Create two acconuts AccountA and AccountB 
AccountA has awssourcebucketa and AccountB has awstargetbucketb

## S3 bucket access from AccountB 

In Account B, we need to create an IAM role that allows cross-account access to the S3 bucket. 
Name this role as Allow_access_to_accountA
Go to IAM>Roles>Create role
Under Selected trusted entity select aws account
Attach permission for amazons3fullaccess and after creation under policies and edit the trust relationship with trustrelation.json

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/eb3f2372-689d-453c-9bdb-edf1558fcbcf">

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/59ccc912-4bbc-497b-b6de-0e6cd1b61699">

 Create a Role in accountA 

Go to IAM>Roles>Create role
Under Selected trusted entity select aws service
Select service as lambda
Under persmision add s3access and name the role as lambdaroletoaccessaccountb_bucket

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/fd7f1578-c82a-41ff-9f0b-4fca120ff5a7">

Edit the policy of role lambdaroletoaccessaccountb_bucket created and select inline policy as json 

Copy the arn from accountB 

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/4113a6d5-0dd7-4caa-82a2-71657887b419">





## Create s3 Buckets in both the Accounts

Create awssourcetargetbucketA in account A and awstargetbucketB in account B 

In awstargetbucketB in account B under bucket policy paste IAMpolicyforACCB_Bucket.json

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/7efaabd8-e337-46af-a8af-eed4a586c1bd">



## Create a lambda function 

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/58b1a480-f8da-43cc-ace1-67ac3c6ab075">

## Add trigger to lamda function object replication

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/6538f4b7-4231-47a0-ad05-27e861d73a7f">

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/9a9456e6-ec0b-4568-b4a1-c6d35e069ceb">


## Under code source paste lambdafunc.py

<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/4b59cea8-b548-4a3f-b863-aeb213b161f1">






