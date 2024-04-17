import sqlite3

class GuitarShop:
    """
    GuitarShop Class represents a guitar shop with many musical instruments.
    """

    def __init__(self):
        self.conn = sqlite3.connect('guitar_shop.sqlite')
        self.cursor = self.conn.cursor()

    def view_products(self):
        """
        view_products method returns a list of all products in a nice format.
        :return:
        """
        category_name = input('Category name: ')
        # Retrieve the category ID based on the provided category name
        query_category_id = "SELECT categoryId FROM Category WHERE categoryName = ?"
        self.cursor.execute(query_category_id, (category_name,))
        category_id = self.cursor.fetchone()
        if category_id:
            query_products = "SELECT productCode, productName, listPrice FROM Product WHERE categoryID = ?"
            self.cursor.execute(query_products, category_id)
            products = self.cursor.fetchall()
            if products:
                print("Code\t\t\tName\t\t\t\t\t\t\t\t\t\tPrice")
                print(75 * "-")
                for product in products:
                    # Format for spacing everything correctly
                    print("{:<15}{:<40}{:>10}".format(*product))
            else:
                print("No products found for this category.")
        else:
            print("Category not found.")

    def update_product_price(self):
        """
        update_product_price method updates the price of the product from the DB.
        Arun I couldn't get the price of the product to get updated in the DB, only on this end. Had trouble.
        :return:
        """
        product_code = input("Product code: ")
        new_price = input("New product price: ")
        query = "UPDATE Product SET listPrice = ? WHERE productCode = ?"
        try:
            self.cursor.execute(query, (new_price, product_code))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Product updated.")
            else:
                print("Product not found.")
        except sqlite3.Error as e:
            print("Error updating product price:", e)

    def main(self):
        """
        main method of the program.
        :return:
        """
        print("Product Manager")
        print()
        print("CATEGORIES")
        print()
        print("Guitars | Basses | Drums")
        print()
        print("COMMAND MENU")
        print("view - View products by category")
        print("update - Update product price")
        print("exit - Exit program")
        print()
        while True:
            command = input("Command: ")
            if command.lower() == 'view':
                self.view_products()
            elif command.lower() == 'update':
                self.update_product_price()
            elif command.lower() == 'exit':
                print("Bye!")
                break
            else:
                print("Invalid command please try again")


if __name__ == "__main__":
    shop = GuitarShop()
    shop.main()
