from Class_Feb19 import Product, Item, Movies

def get_products():
    return (Product("Stanley 13 Ounce Wood Hammer", 10, 2, 5, "Hammer"),
            Movies("The Holy Grail", 20, 1, 5, "DVD", 1975))

def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"Name: {product.name()}\nPrice: {product.price()}\nQuantity: {product.quantity()}\nDiscount: {product.discount()}\nTotal: {product.totalPrice()}")
    if isinstance(product, Item):
        print(f"Author: {product.author}")
    elif isinstance(product, Movies):
        print(f"{'Year':{w}} {product.year}")
    print(f"{'Discount price':{w}} {product.getDiscountPrice():.2f}")
    print()

def main():
    test_products = get_products()
    for item in test_products:
        show_product(item)

if __name__ == "__main__":
    main()