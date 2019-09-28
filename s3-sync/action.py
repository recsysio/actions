#!/usr/bin/env python3

import os
import sys
import boto3
import mimetypes

env = os.environ.copy()
local_dir, s3_dir = sys.argv[1:3]

params = dict(
    aws_access_key_id=env['ACCESS_KEY'],
    aws_secret_access_key=env['ACCESS_SECRET'],
    endpoint_url=env['ENDPOINT'],
)

s3 = boto3.resource('s3', **params)
bucket = s3.Bucket(env['BUCKET'])

for root, dirs, files in os.walk(local_dir):
    for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_dir)
        s3_path = os.path.join(s3_dir, relative_path)

        ExtraArgs = {
            'ACL': env.get('ACL', ''),
            'ContentType': mimetypes.guess_type(local_path)[0],
        }

        bucket.upload_file(local_path, s3_path, ExtraArgs=ExtraArgs)
