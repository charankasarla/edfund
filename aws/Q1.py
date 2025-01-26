import json

def lambda_handler(event, context):
    """
    AWS Lambda function to add two numbers.
    The numbers should be provided as part of the event object in the keys 'num1' and 'num2'.

    Example event:
    {
        "num1": 10,
        "num2": 20
    }
    """
    try: 
        num1 = event.get('num1')
        num2 = event.get('num2')

        if num1 is None or num2 is None:
            raise ValueError("Both 'num1' and 'num2' must be provided in the event object.")

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both 'num1' and 'num2' must be numbers (int or float).")

        result = num1 + num2

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f"The sum of {num1} and {num2} is {result}.",
                'result': result
            })
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': str(e)
            })
        }
