from Produto.FindQuery import ProdutosbyID
from Usuario.FindQuery import UsuariobyID
from bson.json_util import dumps
import json
import string
from random import choice
from bson.objectid import ObjectId


def SetUsuarios(mydb,conR):
    user = UsuariobyID(mydb)
    conR.hset("user:" + user['Email'], user['Nome'], dumps(user['Senha']))
    resultado = conR.hget('user:' + user['Email'] ,user['Nome'])
    decorador = json.loads(resultado.decode())
    print(decorador)

def setListaFavoritos(mydb,conR):
    user = UsuariobyID(mydb) 
    mycol = mydb.usuario
    conR.hset("user:" + user['Email'],user['Nome'], dumps(user['lista_Desejo']))
    buscarUser = mycol.find_one({'Email': user['Email']})

    execucao = True
    while execucao:
        print('''Deseja Continuar favoritando mais Produtos:\n
        - [0]Voltar\n
        - [1]Sim\n
        - [2]Não\n
        ''')
        escolha = input(str('escolha Uma Opção:'))
        match escolha:
            case '0':
                break
            case '1':
                Produtos = ProdutosbyID(mydb)
                conR.hset("user:" + user['Email'],Produtos['Nome'],dumps(Produtos))
                break
            case '2':
                return('Enviado Com Sucesso')
    resultado = conR.hkeys('user:' + user['Email'])
    resultante = []
    for dado in resultado:
        resultante.append(json.loads(conR.hget('user:' + user['Email'], dado.decode())))
        
    mydict = {
    "Nome":buscarUser['Nome'],
    "Data_Nascimento":buscarUser['Data_Nascimento'],
    "Email":buscarUser['Email'],
    "Senha":buscarUser['Senha'],
    "Telefone":buscarUser['Telefone'],
    "Cpf":buscarUser['Cpf'],
    "lista_Desejo":resultante,
    "Cidade":buscarUser['Cidade'],
    "Endereco":buscarUser['Endereco'],
    "Verificado":'Verificado'
    }                           
    mycol.update_one({'_id':ObjectId(buscarUser['_id'])},{'$set':mydict} , upsert=True)
    print('Enviado com Sucesso',conR.hkeys('user:' + user['Email']))


def getUsuariosRedis(conR):
    print(conR.keys())


def deletaRedis(conR):
    print(conR.keys())
    Nome =  input(str('escreva seu Nome Usuario:'))
    conR.delete(Nome)
    print('\n Usuario Retirado Do Redis Com Sucesso.')

def SetToken(mydb,conR):
    mycol = mydb.usuario
    print(conR.keys())
    user_Email =  input(str('escreva seu Email:'))
    user_Nome =  input(str('escreva seu Nome:'))
    Verificar = conR.hget("user:" + user_Email , user_Nome)
    verificado = json.loads(Verificar.decode())
    buscarUser = mycol.find_one({'Email': user_Email})
    mydict = {
    "Nome":buscarUser['Nome'],
    "Data_Nascimento":buscarUser['Data_Nascimento'],
    "Email":buscarUser['Email'],
    "Senha":buscarUser['Senha'],
    "Telefone":buscarUser['Telefone'],
    "Cpf":buscarUser['Cpf'],
    "lista_Desejo":buscarUser['lista_Desejo'],
    "Cidade":buscarUser['Cidade'],
    "Endereco":buscarUser['Endereco'],    
    "Verificado":'Verificado'
    }
    print(verificado)
    x = mycol.replace_one({'Email': user_Email, 'Nome':user_Nome}, mydict, upsert=True)
    print(x)

