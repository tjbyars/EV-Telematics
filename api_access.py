import boto3

# Initialize Boto3 S3 client
s3 = boto3.client('s3')

# Specify bucket name and file key
bucket_name = 'ev-telematics'
file_key = 'telematics_data.csv'

# Download the dataset
s3.download_file(bucket_name, file_key, 'dataset_download.csv')

# Now you can work with your dataset locally
