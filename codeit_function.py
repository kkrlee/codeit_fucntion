def hello():
    print("hello, world")
    print("welcome to world")

hello()


def hello(name):
    print("\nhello, %s" % (name))
    print("welcome to world")

hello("mj")
hello("sy")



def print_sum(a, b):
    print(a + b)
def print_product(a, b):
    print(a * b)
def print_residue(a, b):
    print(a % b)
def print_average(a, b, c):
    print((a + b + c) / 3)
print_sum(4, 2)
print_product(4, 2)
print_residue(5, 2)
print_average(2,3,8)

def print_full_name(first_name, last_name):
    print(last_name, first_name)

print_full_name("윤수", "이")
print_full_name("수민", "이")
