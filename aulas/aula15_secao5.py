# criar a pasta do projeto 
mkdir project1 

# Iniciar o projeto com o Poetry 
poetry init (dentro da pasta do projeto) 

# Iniciar o ambiente virtual 
poetry shell 

# mostrar path da env 
poetry env info -p 

# Instalar as dependencias 
poetry add fastapi uvicorn requests aiohttp


# Criar o arquivo main.py 
from fastapi import FastAPI


app = FastAPI() #instanciar

@app.get('/hello-world')
def hello_world():
    return 'helloWorld!'


#Rodar o projeto
uvicorn main:app --reload