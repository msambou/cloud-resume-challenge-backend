import boto3


class Database:
    def __init__(self):
        self.client = boto3.resource('dynamodb', 'us-east-2')
        self.table = self.client.Table("cloud-resume-challenge")
        

    """
    Function to get total resume views
    """
    def get_count(self):
        try:
            response = self.table.get_item(Key={'id': 1})
            
            status = response["ResponseMetadata"]["HTTPStatusCode"]
            if status == 200:
                responseData = {
                    "status": True,
                    "status_code": 200,
                    "message": "Query successful",
                    "view_count": int(response["Item"]["view_count"])
                }
                print(responseData)
                return responseData
            else:
                responseData = {
                    "status": False,
                    "status_code": status,
                    "message": "Query NOT successful",
                }
                print(responseData)
                return responseData
        except:
            responseData = {
                "status": False,
                "status_code": 500,
                "message": "Server error",
            }
            print(responseData)
            return responseData

    """
    Function to reset the resume views to 0
    """
    def reset_count(self):
        response = self.table.put_item(
            Item = {'id': 1, 'view_count': 0}
        )

    """
    Function to increment the resume view count
    """
    def increment_count(self):
        try:
            response = self.table.update_item(
                Key = {'id': 1},
                UpdateExpression='SET view_count = view_count + :incr',
                ExpressionAttributeValues={
                    ':incr': 1
                }
            )
            # print(response)
            status = response["ResponseMetadata"]["HTTPStatusCode"]
            if status == 200:
                responseData = {
                    "status": True,
                    "status_code": 200,
                    "message": "Query successful",
                }
                return responseData
            else:
                responseData = {
                    "status": False,
                    "status_code": status,
                    "message": "Query NOT successful",
                }
                return responseData
        except:
            responseData = {
                "status": False,
                "status_code": 500,
                "message": "Server error",
            }
            print(responseData)
            return responseData
        

database = Database()
# database.increment_count()
database.get_count()
# database.showTable()

