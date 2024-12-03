x = 0

x = 10
print(f'a) {x}')

x = -10
print(f'a) {x}')

x = 17.5
print(f'б) {x}')

try:
    x = -2 * x
    print(f'б) {x}')
except NameError as e:
    print(e)

x = 60
print(f'в) {x}')

try:
    x = x - 1
    print(f'в) {x}')
except NameError as e:
    print(e)

x = 0
print(f'в) {x}')

x = -50
print(f'г) {x}')

x = -25
print(f'г) {x}')

try:
    x = x + k
    print(f'г) {x}')
except NameError as e:
    print(e)
