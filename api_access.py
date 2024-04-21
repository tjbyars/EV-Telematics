import boto3

# Initialize Boto3 DynamoDB client
dynamodb = boto3.client('dynamodb')

# Specify the table name
table_name = 'EV-Telematics'

# Prompt the user to enter the ID they want to query
id_value = input("Enter the ID you want to query: ")

# Define the key condition expression for the query
key_condition_expression = 'id = :idval'

# Define the expression attribute values for the query
expression_attribute_values = {
    ':idval': {'S': id_value}
}

# Define the projection expression to only include the 'reg_number' attribute in the result
projection_expression = 'reg_number'

# Perform the query
response = dynamodb.query(
    TableName=table_name,
    KeyConditionExpression=key_condition_expression,
    ExpressionAttributeValues=expression_attribute_values,
    ProjectionExpression=projection_expression
)

# Process the query results
for item in response['Items']:
    reg_number = item['reg_number']['S']
    print("Registration Number:", reg_number)
