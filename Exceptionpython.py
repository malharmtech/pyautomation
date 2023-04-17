ItemsIncart = 0

if ItemsIncart != 2:
    pass

assert(ItemsIncart == 0)


try:
    with open('test1.text', 'r') as reader:
        reader.read()
except:
    with open('test.text', 'r') as reader:
        reader.read()

try:
    with open('test1.text', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("done finally")