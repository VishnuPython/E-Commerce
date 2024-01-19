from flask import Flask,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS,cross_origin

#Add mysql connection values in lines 8-12

app=Flask(__name__)
app.config['MYSQL_HOST']=''
app.config['MYSQL_USER']=''
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_PORT']=0
app.config['MYSQL_DB']=''
mysql=MySQL(app)
cors=CORS(app)

class Main:
    def products(count):
        cur=mysql.connection.cursor()
        ID=1001
        products_json=[]
        for product in range(count):
            cur.execute(f"""select * from products where id={ID}""")
            data=cur.fetchone()
            products_count=0
            for i in data:
                products={'id':data[0],'title':data[1],'price':data[2],'imagePath':data[3]}
            products_json.append(products)
            ID=ID+1
        cur.close()
        return products_json
        

@app.route('/products',methods=['GET'])
@cross_origin()
def main():
    products=Main.products(7)
    return jsonify(products)

if __name__=='__main__':
    app.run(debug=True)
