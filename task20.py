s = 0
k = 0

s = 14
print(f'а) {s}')

k = -3
print(f'а) {k}')

try:
    d = s + 1
    print(f'a) {d}')
except NameError as e:
    print(e)

s = d
print(f'а) {s}')

try:
    k = 2 * s
    print(f'a) {d}')
except NameError as e:
    print(e)

k = 30
print(f'б) {k}')

try:
    d = k - 5
    print(f'б) {d}')
except NameError as e:
    print(e)

try:
    k = 2 * d
    print(f'б) {d}')
except NameError as e:
    print(e)

try:
    s = k - 100
    print(f'б) {d}')
except NameError as e:
    print(e)
