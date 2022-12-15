"""saving documents to json line file"""
with open(f'rank1_{Date}.jsonl', 'w') as f:
    for docs in data:
        json.dump(docs, f)
        f.write('\n')
        
#Saving file to s3 resource
  key= DIRECTORY.split('/')[-1]       
  key= f"{key}/{YrMonth}/rank1_{Date}.json"
  s3 = boto3.resource('s3')
  s3.Object(BUCKET, key).put(Body=json.dumps(data))
#Saving using s3 client 
   s3 = boto3.resource('s3')
   s3.put_object(
        Bucket=BUCKET,
        Body= json.dumps(data),
        Key=key
        )
