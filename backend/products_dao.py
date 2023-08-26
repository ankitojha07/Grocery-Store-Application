# dao : data access object

from sqlConnection import getSqlConnection

def getAllProducts(connection):
    
    cursor = connection.cursor()

    query = "select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products inner join uom on products.uom_id=uom.uom_id"

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name' : name,
                'uom_id' : uom_id,
                'price_per_unit' : price_per_unit,
                'uom_name' : uom_name
            }
        )
    return response

def insertNewProduct(connection, product):
    cursor = connection.cursor()
    query = ("insert into products "
            "(name, uom_id, price_per_unit)"
             "values (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def deleteProduct(connection, product_id):
    cursor = connection.cursor()
    query = ("delete from products where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = getSqlConnection()

    # getting all products
    print("Printing old products : \n")

    print(getAllProducts(connection), "\n")

    #inserting new products
    print("Product id : ", insertNewProduct(connection,{
        'product_name':'Tomato',
        'uom_id':'2',
        'price_per_unit':'160'
    }),"\n")
    

    #deleting a product by product id
    deleteProduct(connection, 19)

    # printing products again
    print("Printing remaining products : \n")
    print(getAllProducts(connection), "\n")