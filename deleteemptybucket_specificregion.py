import boto3


access_key = "AKIAW6KT6TBGUO3PR5WZ"
secret_key = "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"
region_name = 'us-east-1'

s3_client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

s3 = boto3.resource("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

response = s3_client.list_buckets()
buckets = response["Buckets"]

empty_buckets = []
for bucket in buckets:
    bucket_name = bucket["Name"]
    result = s3_client.list_objects_v2(Bucket=bucket_name)
    if "Contents" not in result:
        versioning = s3_client.get_bucket_versioning(Bucket=bucket_name)
        if versioning.get("Status") != "Enabled":
            empty_buckets.append(bucket_name)


for bucket_name in empty_buckets:
    s3.Bucket(bucket_name).delete()
    print(f"Bucket {bucket_name} deleted.")