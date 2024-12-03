s = 0
print(s)

s = -5
print(f'a) {s}')

s = -57
print(f'a) {s}')

s = -6
print(f'б) {s}')

try:
    s = -5.2 * s
    print(f'б) {s}')
except NameError as e:
    print(e)

s = 0
print(f'б) {s}')

s = -7.5
print(f'в) {s}')

try:
    s = 2 * s
    print(f'б) {s}')
except NameError as e:
    print(e)

s = 45
print(f'г) {s}')

s = -25
print(f'г) {s}')

try:
    s = s + k
    print(f'г) {s}')
except NameError as e:
    print(e)