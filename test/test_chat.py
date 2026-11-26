
import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

client = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

try:
    response = client.converse(
        modelId=os.getenv("BEDROCK_CHAT_MODEL"),
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": "Explain RAG in one sentence."}
                ]
            }
        ],
        inferenceConfig={"maxTokens": 100}
    )

    print("SUCCESS!")
    print(response["output"]["message"]["content"][0]["text"])

except ClientError as e:
    print("AWS ERROR:")
    print(e.response["Error"])
