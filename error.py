import saveData

def errorRequest (response, uri, message=None):
    """
    errorRequest (response = status_code, uri = url_error, message = Default None)
    This function receive three arguments,
    Status of request = (400, 404, 500, 508)
    url = Ex: 172.0.0.1:8008/hello_word
    message = "Not Authorized"
    """
    
    db = saveData.MongoDb()
    if response == 400:
        if message == None:
            message="Bad Request"
        print(f"[{response}] [{message}] [{uri}]")
        data={
            "status":response,
            "message": message,
            "url":uri
        }
        
    
    if response == 404:
        if message == None:
            message="Page Not Found"
        print(f"[{response}] [{message}] [{uri}]")
        data={
            "status":response,
            "message":message,
            "url":uri
        }
        
        
    if response == 500:
        if message == None:
            message="Internal Server Error"
        print(f"[{response}] [{message}] [{uri}]")
        data={
            "status":response,
            "message":message,
            "url":uri
        }
        
        
    if response == 508:
        if message == None:
            message="Loop Detected"
        print(f"[{response}] [{message}] [{uri}]")
        data={
            "status":response,
            "message":message,
            "url":uri
        }
        
    db.insert_one(data)