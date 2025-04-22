#This was what he tought

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return  pwd_context.hash(password)
    
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)



# # passlib is not actively maintained so we are getting issues with bcrypt but we can resolve them 
# # by directly using bcrypt or downgrading bcrypt


# # From GFG
# import bcrypt

# # Hash a password using bcrypt
# def hash_password(password):
#     pwd_bytes = password.encode('utf-8')
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
#     return hashed_password

# # Check if the provided password matches the stored password (hashed)
# def verify_password(plain_password, hashed_password):
#     password_byte_enc = plain_password.encode('utf-8')
#     return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)