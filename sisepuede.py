products = []

def init():
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