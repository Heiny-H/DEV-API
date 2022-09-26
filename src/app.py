from flask import Flask, request, jsonify, response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

# proteger a senha do usuario
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://127.0.0.1:59083/dbInfo"
mongo = PyMongo(app)


@app.route('/usuarios', methods=['POST'])
def criar_Usuario():


# Recebe dados
nomeUsuario = request.json['usuario']  # meuexemplo
email = request.json['email']
senha = request.json['senha']


if usuario and email and senha:
   hashed_password = generate_password_hash(password)

  id =  mongo.db.users.insert(
      {'usuario': usuario,'email': email, 'senha': senha }
    )
   resposta = {
       'id': str(id)
       'usuario': usuario 
       'senha': hashed_password
       'email': email
   }
   
   return resposta
  
else:

return not_found()



@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = mongo.db.users.find()
    resposta= json_util.dumps(usuarios)
    return Resposta(resposta, mimetype="application/json")

@app.route('/usuarios/<id>', methods=['GET']) # todas as infos de um usuario em especifico 
def get_usuario(id):
    print(id)
    usuario = mongo.db.users.find_one({'_id': ObjectId(id), })
    resposta = json_util.dumps(usuario)
    return Resposta(resposta, mimetype="application/json")


@app.route('/usuarios/<_id>', methods=['PUT'])
def update_user(_id):
    usuario = request.json['usuario']
    email = request.json['email']
    senha = request.json['senha']
    if usuario and email and senha and _id:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'usuario': usuario, 'email': email, 'senha': hashed_password}})
        resposta = jsonify({'mensagem': 'usuario' + _id + 'Atualizado com Sucesso'})
        resposta.status_code = 200
        return resposta
    else:
      return not_found()


@app.errorhandler(404) # manipulação de erros
def não_encontrado(error=none):
    mensagem = jsonify({
        'mensagem': 'Recurso não encontrado' + request.url,
        'status': 404
    })
    
    resposta.status_code = 404
    
    return mensagem  


@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    resosta = jsonify({'mensagem': 'Usuario' + id + ' Deleted Successfully'})
    resposta.status_code = 200
    return resposta

if __name__ == "__main__":
    app.run(debug=true, port: 3000,)
    