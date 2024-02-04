from fastapi import FastAPI
import mysql.connector

app=FastAPI()

class Mysql:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    def connection(self,query):
        con=mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        cur=con.cursor()
        cur.execute(query)
        data=cur.fetchall()
        cur.close()
        con.close()
        return data
    def connection_commit(self,query):
        con=mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        cur=con.cursor()
        cur.execute(query)
        data=cur.commit()
        cur.close()
        con.close()
        return data

class Products(Mysql):
    def __init__(self):
        super().__init__("localhost","root","password","db")
    def products(self):
        products=[]
        query="""select * from products"""
        product_data=self.connection(query=query)
        for data in product_data:
            product_json={"id":data[0],"title":data[1],"price":data[2],"image_path":data[3]}
            products.append(product_json)
        return products
    def categories(self,category):
        query="""select * from products where category="%s" """
        data=self.connection(query,category)
        return data

class Profile(Mysql):
    def __init__(self,Id,email,password):
        super().__init__("localhost","root","password","db")
        self.Id=Id
        self.email=email
        self.password=password
    def create_user(self):
        query="""insert into users(id,email,password) values(%s,%s,%s)"""
        data=(self.Id,self.email,self.password)
        self.connection_commit(query,data)
        return data
    

    
    
@app.get("/")
async def products():
    products=Products()
    return products.products()



if __name__=='__main__':
    app.run(debug=True)
