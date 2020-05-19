import sys


def asc(n):
    return int(''.join(sorted(str(n))))


def desc(n):
    return int(''.join(sorted(str(n))[::-1]))


n = input("Poner numero: ")

repdigits = ["1111", "2222", "3333", "4444",
             "5555", "6666", "7777", "8888", "9999"]

digits = list(n)
# print(digits)


if n not in repdigits:
    if n == "6174":
        print("0")
        sys.exit()
    print("numero valido")
else:
    print("8")
    sys.exit()

n_completado = int(n)
if len(digits) < 4:
    if len(digits) == 3:
        n_completado *= 10
    if len(digits) == 2:
        n_completado *= 100
    if len(digits) == 1:
        n_completado *= 1000

print(n_completado)

iteraciones = 0
while n_completado != 6174:
    n_completado = desc(n_completado) - asc(n_completado)
    if n_completado == 999: 
        n_completado *= 10
    iteraciones = iteraciones + 1
    # print(n_completado)
    print(iteraciones)
