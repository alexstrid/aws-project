import json


def hello(event, context):
   body = {
       "message": "Go Serverless v1.0! Testing Webhook",
       "input": event
   }

   response = {
       "statusCode": 200,
       "body": json.dumps(body)
   }

   return response

def calculator(event,context):
    print(event)
    num_dict = json.loads(event['body'])
    number1 = num_dict['number1']
    number2 = num_dict['number2']
    sum = number1 + number2
    return {
        'statusCode': 200,
        'body': json.dumps('The sum of '+str(number1)+ ' and '+str(number2) +' is '+str(sum)+'. Woho, webhook works!')
    }