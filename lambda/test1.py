import json
import boto3
from test2 import fun

s3=boto3.resource("s3")

def lambda_handler(event,context):
	bucketlist=[]
	fun()
	for bucket in s3.buckets.all():
		bucketlist.append(bucket.name)
	print(json.dumps(bucketlist))
	return {
		"statusCode": 200,
		"body": bucketlist
	}