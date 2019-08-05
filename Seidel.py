from math import sqrt


def seidel(A, b, eps):
    n = len(A)
    r = range(n)
    x = [0 for i in r]

    converge = False
    while not converge:
        x_new = x.copy()
        for i in r:
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in r)) <= eps
        x = x_new

    return x


print("Seidel method")
print("Enter the alpha: ", end="")
alpha = int(input())
print("Enter the epsilon: ", end="")
eps = float(input())

A = ((7 + alpha, 2.5, 2, 1.5, 1),
     (2.5, 8 + alpha, 2.5, 2, 1.5),
     (2, 2.5, 9 + alpha, 2.5, 2),
     (1.5, 2, 2.5, 10 + alpha, 2.5),
     (1, 1.5, 2, 2.5, 11 + alpha))
b = (1, 1, 1, 1, 1)

x = seidel(A, b, eps)
print("Solution: ", end="")
for i in range(len(x) - 1):
    print('{:.8f}'.format(x[i]), end=" ")
print('{:.8f}'.format(x[len(x) - 1]))
