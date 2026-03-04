import bcrypt

class Criptografia:

    @classmethod
    def gerarHash(cls, senha):
        senha = bytes(senha, 'utf-8')
        hash = bcrypt.hashpw(senha, bcrypt.gensalt())
        return hash.decode()

    @classmethod
    def compararSenha(cls, senha, hash):
        senha = bytes(senha, 'utf-8')
        hash = bytes(hash, 'utf-8')
        return bcrypt.checkpw(senha, hash)

if __name__ == "__main__":
    senha = "123456"
    senha_criptografada = Criptografia.gerarHash(senha)
    print(f'Senha: {senha}')
    print(f'Senha cript: {senha_criptografada}')

    result = Criptografia.compararSenha(senha, senha_criptografada)
    print(f'Comparação: {result}')