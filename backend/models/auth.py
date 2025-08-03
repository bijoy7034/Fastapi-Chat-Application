from pydantic import BaseModel, model_validator

class UserRegister(BaseModel):
    fullname : str
    password : str
    confirm_password :  str
    email : str
    username : str
    
    @model_validator(mode="after")
    def check_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
    

class UserLogin(BaseModel):
    username : str
    password : str