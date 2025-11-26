# Part I:
def print_circum(radius):
	pi = 3.14159
	circumference = 2 * pi * radius
	print(f"The circumference is: {circumference}")

print_circum(4)
print_circum(10)
print_circum(15.5)


# Part II:

def catalog():
	item1 = 200.0
	item2 = 400.0
	item3 = 600.0
	combo1 = (item1 + item2) * 0.9
	combo2 = (item2 + item3) * 0.9
	combo3 = (item3 + item1) * 0.9
	combo4 = (item1 + item2 + item3) * 0.75

	print("Online Store")
	print("=" * 30)
	print("Product(S)                     Price")
	print("Item 1                         ", item1)
	print("Item 2                         ", item2)
	print("Item 3                         ", item3)
	print("Combo 1(Item 1 + 2)            ", combo1)
	print("Combo 2(Item 2 + 3)            ", combo2)
	print("Combo 3(Item 1 + 3)            ", combo3)
	print("Combo 4(Item 1 + 2 + 3)        ", combo4)
	print("=" * 30)
	print("For delivery Contact:98764678899")

catalog()