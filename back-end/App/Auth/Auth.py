import os
from dotenv import load_dotenv
from jose import jwt, JWTError
from App.Models import UserModel, PermissionModel
from passlib.context import CryptContext
from datetime import datetime, timedelta

# Configuração do contexto de criptografia
crypto = CryptContext(schemes=["sha256_crypt"])
load_dotenv()

# Carregando as variáveis de ambiente
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

class Auth:
    def __init__(self):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def user_login(self, data):
        user = UserModel.get_user_by_username(data.username)

        if user:
            if not crypto.verify(data.password, user.hashed_password):
                return None
        else:
            if data.username == "admin" and data.password == "admin":
                user = UserModel(
                username="admin", 
                hashed_password=crypto.hash("admin"), 
                role="admin")
                UserModel.create_user(user)

                permission = PermissionModel(
                    name="admin",
                    permission="all"
                )
                PermissionModel.create_permission(permission)
            else:
                return None

        exp = datetime.utcnow() + timedelta(minutes=30)
        payload = {
            "sub": user.username,
            "exp": exp
        }

        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

        return {
            "access_token": token,
            "token_type": "bearer",
            "exp": exp.isoformat(),
            "role": user.role,
            "username": user.username,
            "id": str(user.id)
        }

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None