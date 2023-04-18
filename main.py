from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.Product.Product import product_router
from routers.User.User import user_router
from models.users import User
from fastapi.responses import HTMLResponse


# metodos Path, Query sirven para las validaciones, y especificar por donde van a entrar los datos

# HTMLResponse y JSONResponse son para responder algo del lado del cliente, en caso de que sean datos
# Se usa JSONResponse y en caro de que sea una estructura que requeria mostrarse con algo escpeficio se usa HTMLResponse
# field Sirve para definir los campos de un modelo de datos Python que se utiliza para la validación y serialización de datos.

#  Creamos una instancia
app = FastAPI()
# Titulo de la documentacion
app.title = "Documentacion Principal"

app.description = "Descripcion Documentacion Principal"
app.version = "1.0.0"
app.add_middleware(ErrorHandler)


@app.get('/')
def get_hello():
    return HTMLResponse("<div style='display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; text-align: center;'> <h1>Bienvenido a mi API</h1> <p>Te invito a ver la documentación en <a href='http://206.81.10.19/docs'>http://206.81.10.19/docs</a></p></div>")


Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(product_router)
