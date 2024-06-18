class Product:
    def __init__(self, name):
        self.name = name

def show_products(products):
    if not products:
        print("Danh sách sản phẩm trống!")
        return

    print("Danh sách sản phẩm:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product.name}")

def add_product(products):
    new_product_name = input("Nhập tên sản phẩm mới: ")
    new_product = Product(new_product_name)
    products.append(new_product)
    print(f"Sản phẩm '{new_product_name}' đã được thêm thành công!")

def edit_product(products):
    if not products:
        print("Danh sách sản phẩm trống!")
        return

    show_products(products)
    product_index = int(input("Nhập vị trí sản phẩm cần sửa: ")) - 1

    if 0 <= product_index < len(products):
        new_name = input("Nhập tên mới cho sản phẩm: ")
        products[product_index].name = new_name
        print(f"Sản phẩm đã được đổi tên thành '{new_name}'!")
    else:
        print("Vị trí sản phẩm không hợp lệ!")

def delete_product(products):
    if not products:
        print("Danh sách sản phẩm trống!")
        return

    show_products(products)
    product_index = int(input("Nhập vị trí sản phẩm cần xóa: ")) - 1

    if 0 <= product_index < len(products):
        deleted_product = products.pop(product_index)
        print(f"Sản phẩm '{deleted_product.name}' đã được xóa!")
    else:
        print("Vị trí sản phẩm không hợp lệ!")

def main():
    products = []

    while True:
        print("\nChọn chức năng:")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Sửa tên sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            show_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            edit_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            print("Thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
