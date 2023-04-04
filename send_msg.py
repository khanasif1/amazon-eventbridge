import boto3

client = boto3.client('events',
                      region_name='{regionname}',
                      aws_access_key_id= '{key id}',
                      aws_secret_access_key='{ key secret}')

response = client.put_events(
    Entries=[
        {
            'Source': 'user-event',
            'Time': '2019-01-16T18:16:01Z',
            'EventBusName':'{Eventbridge Bus name}',
            'DetailType': 'user-preferences-sqs',
            'Detail':'{ "username":"sam","city":"sydney","age":"44" }'
        }
    ]
)

print(response)