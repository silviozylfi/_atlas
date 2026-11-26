
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION")

client = boto3.client(
    "service-quotas",
    region_name=region,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

# Amazon Nova Lite daily token quota
quota_code = "L-45E0AD92"

print("Region:", region)

try:
    applied = client.get_service_quota(
        ServiceCode="bedrock",
        QuotaCode=quota_code
    )

    default = client.get_aws_default_service_quota(
        ServiceCode="bedrock",
        QuotaCode=quota_code
    )

    print("\n--- APPLIED ACCOUNT QUOTA ---")
    print("Name:", applied["Quota"]["QuotaName"])
    print("Value:", applied["Quota"]["Value"])
    print("Adjustable:", applied["Quota"]["Adjustable"])

    print("\n--- AWS DEFAULT QUOTA ---")
    print("Value:", default["Quota"]["Value"])

except Exception as e:
    print("ERROR:", e)
