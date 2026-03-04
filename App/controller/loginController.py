from App.model.userModel import Usuario 
from App.utils.criptografia import Criptografia
from App.config.database import Database

__currentUser = {
    "id": None,
    "nome": "",
    "email": "",
    "tipo": ""
}

def isLogged():
    return __currentUser['id']

def logout():
    __setCurrentUser(None)

def __setCurrentUser(id):
    # Modificado quando implementar a model
    __currentUser["id"] = id

def validateLogin(email, password):
    user = Usuario.login(email)
    result_senha = Criptografia.compararSenha(password, user.senha)
    if user.id and user.email == email and result_senha:
        __setCurrentUser(user.id)
        return True
    
    return False