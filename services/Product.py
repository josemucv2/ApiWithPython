from models.products import Product as ProductModel
from schemas.Product import Product as ProductSchema

class ProductService():
    def __init__(self, db)-> None:
        self.db = db
    # all products
    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result
    # only ona product
    def get_only_products(self,id):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result
    #  filter the cateogry
    def get_category_products(self,category):
        result = self.db.query(ProductModel).filter(ProductModel.category == category).first()
        return result
    #  create a Product
    def create_product(self, product: ProductSchema):
        new_product = ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return
    # Update a Product
    def update_product(self, id: int, product: ProductSchema):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        result.category = product.category
        result.description = product.description
        result.price = product.price
        result.title = product.title
        self.db.commit()
        return
    # Deklete a Product
    def delete_product(self,id: int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        self.db.delete(result)
        self.db.commit()
        return
