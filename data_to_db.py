import boto3
import csv

# Initialize Boto3 DynamoDB client
dynamodb = boto3.client('dynamodb')

# Specify the name of your DynamoDB table
table_name = 'ev-telematics'

# Open the CSV file
with open('telematics_data.csv', 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Convert data types if necessary
        # For example, convert string to int
        # row['column_name'] = int(row['column_name'])
        
        # Build the item to insert into the DynamoDB table
        item = {key: {'S': value} for key, value in row.items()}
        
        # Insert the item into the DynamoDB table
        response = dynamodb.put_item(
            TableName=table_name,
            Item=item
        )