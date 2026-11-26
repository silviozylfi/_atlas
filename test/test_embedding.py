
import os
import json
import boto3
import time
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

print("Region:", os.getenv("AWS_REGION"))
print("Model:", os.getenv("BEDROCK_EMBED_MODEL"))

time.sleep(10)

try:
    response = client.invoke_model(
        modelId=os.getenv("BEDROCK_EMBED_MODEL"),
        body=json.dumps({
            "inputText": "Hello Amazon Bedrock",
            "dimensions": 1024,
            "normalize": True
        }),
        contentType="application/json",
        accept="application/json"
    )

    data = json.loads(response["body"].read())

    print("SUCCESS!")
    print("Embedding dimension:", len(data["embedding"]))

except ClientError as e:
    print("AWS ERROR:")
    print(e.response["Error"])
