import saveData
import os

try:
    from flask import Flask, request
except:
    os.system("pip3 install flask")
    from flask import Flask, request

app = Flask("scrapyTest")

def generateResponses (status, message, name_content=False,content=False):
    response = {}
    response["Status"] = status
    response["Message"]= message

    if name_content and content:
        response[name_content] = content

    return response

#Pegando o uma lista com os status do bot
def statusBot(data):
    list_status=[]
    for row in data:
        if row['status'] not in list_status:
            list_status.append(row['status'])
    return list_status


@app.route("/olamundo", methods=["GET"])
def olamundo():
    return {'message':'Olá mundo!'}


@app.route("/status", methods=["GET"])
def getStatusBot():

    db_noSql = saveData.MongoDb()
    
    try:
        list_status = statusBot(db_noSql.find_all())
        data = {i:len(db_noSql.find_all({'status':i})) for i in list_status}
        print(list_status)
        print(data)    
    
    except:
        return generateResponses(400,"Não foi encontrado informação")
    
    else:
        return generateResponses(200,'Sucesso','flags',data)
        
    #200 significa que capturou a lista com cpfs
    #1 inicia a captura dos dados contidos em cada cpf. Se parar a execução ficará com alguma lista parada nessa flag
    
@app.route("/input/flag/<flag>", methods=["GET"])
def sourceInputFlag(flag):
    db_noSql = saveData.MongoDb()
    
    try:
        data=db_noSql.find_all({'status':int(flag)})
        for row in data:
            del row['_id']
        #data = [row['_id']=str(row['_id']) for row in data]
        #print(data)
    except:
        return generateResponses(400, "Falha ao pesquisar")
    
    else:
        return generateResponses(200, f'Inputs flag {flag}', 'data', data)
app.run()