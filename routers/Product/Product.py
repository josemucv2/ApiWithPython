from fastapi import APIRouter,Depends, Path, Query
from config.database import Session
from models.products import Product as ProductModel
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi.responses import  JSONResponse
import data
from middlewares.jwt_bearer import JWTBearer
from schemas.Product import Product as ProductSchema
from services.Product import ProductService


product_router = APIRouter()

@product_router.get('/products', tags=['Products'], response_model=List[ProductSchema], status_code=200)
def get_products() -> List[ProductSchema]:
    db = Session()
    result =ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#  ----------------------------- GET BY ID ------------------------------------------------- #


@product_router.get('/products/{id}', tags=['Products'], response_model=List[ProductSchema], status_code=200)
def get_products_by_id(id: int = Path(ge=1, le=200)) -> ProductSchema:
    db = Session()
    result = ProductService(db).get_products(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#  ----------------------------- GET CATEGORY ------------------------------------------------- #


@product_router.get('/products/', tags=['Products'], response_model=List[ProductSchema], status_code=200)
def get_products_by_categories(category: str = Query()) -> List[ProductSchema]:
  db = Session()
  result = ProductService(db).get_category_products(category)
  return JSONResponse(status_code=200, content=jsonable_encoder(result))

  
#  ----------------------------- POST ------------------------------------------------- #


@product_router.post('/products', tags=['Products'], response_model=dict, status_code=200)
def create_product(product: ProductSchema) -> dict:
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={"message": "Product created"})

#  ----------------------------- UPDATE ------------------------------------------------- #


@product_router.put('/products/{id}', tags=['Products'], response_model=dict, status_code=200)
def update_product(id, product: ProductSchema) -> dict:
    db = Session()
    result = ProductService(db).get_only_products(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    
    ProductService(db).update_product(id, product)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Product updated"})

#  ----------------------------- DELETE ------------------------------------------------- #


@product_router.delete('/products/{id}', tags=['Products'], response_model=dict, status_code=200)
def delete_product(id: int) -> dict:
    db = Session()
    result = ProductService(db).get_only_products(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content={"message": "Product deleted"})

#  ----------------------------- POST LOGIN ------------------------------------------------- #