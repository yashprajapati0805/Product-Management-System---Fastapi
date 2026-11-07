from fastapi import FastAPI,HTTPException,Depends
from database import session,engine
from models import Product
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

#db connection
db = session()

#SQLAlchemy table creation
database_models.Base.metadata.create_all(bind = engine)




@app.get("/")
def greet():
    return "Welcome to Site!!"

products = [
    Product(id=1,name="Coca Cola",description="Soft Drink",price=9.99,quantity=10),
    Product(id=2,name="Loq",description="Laptop",price=99999.99,quantity=5),
    Product(id=3,name="HKFX",description="Keyboard",price=8500,quantity=63)
]

#Inserting Pydantic-BaseModel objects into database
#.model_dump creates dictionary
#in python we use(**) to unpack dictionary
#And nothhing will be store until we .commit() to database
def init_db():
    db = session()
    count =db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
init_db()

#Dependency Injection(Fastapi)
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    #This is an orm query that returns all sqlalchemy database objects.
    db_products = db.query(database_models.Product).all()
    return db_products


# Getting Product by id
@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):
    #This is an orm query that matches entered id with database model product id and returns the first element
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    #Checks db_products is not empty.
    if db_products:
        return db_products

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


# Adding an product.
@app.post("/products")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return "Product Added Successfully",product

#Updating a product.
@app.put("/products")
def update_product(product:Product,id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.price = product.price
        db_product.quantity = product.quantity
        db_product.name = product.name
        db_product.description = product.description
        db.commit()
        return product,"Added Successfully"
    else:
        return "Product Not found"

#Deleting a product.

@app.delete("/products")
def delete_product(id:int,db:Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted!!!"
    else:
        raise HTTPException(status_code=404, detail="Product Not found")