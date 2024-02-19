from store_classes import StoreProducts

def add_product_to_cart():
    while True:
        try:
            product_name = input("Please enter the product name")
            if product_name not in StoreProducts:
                store.name = product_name
                StoreProducts.append(product_name)
                print("The product has been added to the cart!")
            else:
                print("The product is already in the cart, please try again.")
        except ValueError:
            print("Please enter a valid product")



def main():
    print("Welcome to the store!")
    print("Options:\n1. Add a product to your cart")
    store = StoreProducts('Stanley Hammer',2,5,'Red')
    while True:
        try:
            option = int(input("Enter an option: "))
            if option == 1:
                add_product_to_cart()
        except ValueError:
            print("Please try again.")

if __name__ == '__main__':
    main()
