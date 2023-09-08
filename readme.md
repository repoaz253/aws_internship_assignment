1. Create s3 Buckets in both the Accounts


2.Create the IAM role to access S3 Bucket in same account 
a. Create policy to access s3 bucket in same account 
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/55407d54-f6b3-489b-87ff-5ac7aa0895ff">


3. Create the IAM role to access S3 Bucket in diff account 
a. In account A create a role to access bucket in account b
<img width="990"  src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/55407d54-f6b3-489b-87ff-5ac7aa0895ff">
b. In account B create a role to allow cross account access


c. edit the permisions of awstargetbucket
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/b5a0d7d1-3635-496c-a1ae-2d23e7727403">


5.Create lambda function
https://github.com/repoaz253/aws_internship_assignment/assets/130156999/a549ac60-a227-44e5-9276-470dcdf36957
Add existing roles that we created for lambda
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/ee8abb96-bf78-4c73-b534-571f47a19a58">

6.Add trigger to lambda function 
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/04bc562d-b9b7-4489-9f8b-67c8df8209cd">


7. Add trigger as source bucket
<img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/269a7f1b-ea0b-4974-9bd9-c32e14815f48">

8. Add the lamda_func.py code
  <img width="990" src="https://github.com/repoaz253/aws_internship_assignment/assets/130156999/1c8b0a62-f124-48cb-a7c3-24c16faefdf0">





