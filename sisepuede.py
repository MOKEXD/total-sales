#here we create a inventory management system fo a moke app, we will create
#a function to registrer products, and other to calculate the total of this products.
products = []

def init(): #here we create a function to registrer products
    n = int(input("how many products do you want to register?: "))

    for i in range(n):
        print("product", i+1)

        name = input("product name: ")
        price = int(input("product price: "))
        quantity = int(input("product quantity: "))

        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

        print("product added successfully", i+1)
        print("product name:", name)
        print("product price:", price)
        print("product quantity:", quantity)
