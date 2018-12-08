# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

'''s3 = session.resource ('s3')
for bucket in s3.buckets.all():
    print(bucket)

new_bucket = s3.create_bucket(Bucket='859081656887-acg-webotron-bucket-03', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket
for bucket in s3.buckets.all():
    print(bucket)

ec2_client = session.client('ec2')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession.py 1-100')'''