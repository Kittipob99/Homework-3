#Written in Python IDLE 3.14.6
class Matrix:
    def __init__(self, data):
        self.data = data

    def show(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)

    def subtract(self, other):
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)

        return Matrix(result)

    def multiplication(self, other):
        result = []

        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                total = 0

                for k in range(len(other.data)):
                    total += self.data[i][k] * other.data[k][j]

                row.append(total)

            result.append(row)

        return Matrix(result)


# Create matrices
A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

# Show A
print("Matrix A:")
A.show()

# Show B
print("\nMatrix B:")
B.show()

# Addition
print("\nA + B:")
C = A.add(B)
C.show()

# Subtraction
print("\nA - B:")
C = A.subtract(B)
C.show()

# Multiplication
print("\nA * B:")
C = A.multiplication(B)
C.show()
