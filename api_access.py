import boto3

# Initialize Boto3 DynamoDB client
dynamodb = boto3.client('dynamodb')

# Specify the table name
table_name = 'EV-Telematics'

# Function to get the maximum ID number from the database
def get_max_id_number():
    response = dynamodb.scan(
        TableName=table_name,
        Select='COUNT',  # Count the number of items in the table
    )
    return response['Count']

# Function to validate the ID input
def validate_id_input(input_str, max_id):
    try:
        id_value = int(input_str)
        if 1 <= id_value <= max_id:
            return id_value
        else:
            raise ValueError(f"ID value must be in the range of 1 to {max_id} inclusive.")
    except ValueError:
        raise ValueError(f"Invalid input. Please enter a valid integer value between 1 and {max_id}.")

# Get the maximum ID number from the database
max_id_number = get_max_id_number()

# Prompt the user to enter the ID they want to query
id_input = input(f"Enter the ID you want to query (1-{max_id_number} inclusive): ")

# Validate the ID input
id_value = validate_id_input(id_input, max_id_number)

# Define the key condition expression for the query
key_condition_expression = 'id = :idval'

# Define the expression attribute values for the query
expression_attribute_values = {
    ':idval': {'N': str(id_value)}  # Convert id_value to string ('N')
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
