"""
manipulation de nombres complexes en python
avec des matrices
"""

#_____FONCTIONS UTILES_____

def create_matrix(i, j):
    return [[0 for k in range(j)] for k in range(i)]

def mat_mult(A, B):
    out = create_matrix(len(A), len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                out[i][j] += A[i][k] * B[k][j]
    return out

def mat_sum(A, B):
    out = create_matrix(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            out[i][j] = A[i][j] + B[i][j]
    return out

def scal_mult(A, k):
    out = create_matrix(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            out[i][j] = A[i][j] * k
    return out

def factorial(n):
    total = 1 
    for i in range(2, n + 1):
        total *= i
    return total

def bincoef(k, n):
    return factorial(n) // (factorial(k) * factorial(n - k))

#_____MATRICES UTILES_____

ID = create_matrix(2, 2) #matrice identité
ID[0][0] = 1
ID[1][1] = 1    

N = create_matrix(2, 2) #matrice nulle
            
I = create_matrix(2, 2) #i
I[0][1] = -1
I[1][0] = 1

I2 = create_matrix(2, 2) #i^2
I2[0][0] = -1
I2[1][1] = -1     

I3 = create_matrix(2, 2) #i^2
I3[0][1] = 1
I3[1][0] = -1  

I4 = create_matrix(2, 2) #i^2
I4[0][0] = 1
I4[1][1] = 1

pow_I = [I4, I, I2, I3] #liste des puissances de i

def power_i(exp):
        return pow_I[exp % 4]

#_____POO_____

class Complex():
    def __init__(self, r, i):
        self.C = self.cmatrix(r, i)
        
    def cmatrix(self, r, i):
        out = create_matrix(2, 2)
        
        out[0][0] = r 
        out[1][1] = r 
        out[0][1] = - i
        out[1][0] = i
        
        return out
        
    def __add__(self, other):
        if isinstance(other, Complex):
            out = mat_sum(self.C, other.C)
            return Complex(out[0][0], out[1][0])
        else : 
            out = [[self.C[0][0] + other, self.C[0][1]], [self.C[1][0], self.C[1][1] + other]]
            return Complex(out[0][0], out[1][0])
            
    
    def __mul__(self, other):
        if isinstance(other, Complex):
            out =  mat_mult(self.C, other.C)
            return Complex(out[0][0], out[1][0])
        else : 
            out =  scal_mult(self.C, other)
            return Complex(out[0][0], out[1][0])
        
    def power_complex(self, n):
        a = self.C[0][0]
        b = self.C[1][0]
        
        total = create_matrix(2, 2)
        
        for k in range(0, n + 1):
            bc = bincoef(k, n)
            
            A = scal_mult(ID, a ** (n - k))
            B = scal_mult(power_i(k), b ** k)
            
            X = mat_mult(A, B)
            X = scal_mult(X, bc)
            
            total = mat_sum(X, total)
            
        return total
    
    def __pow__(self, n):
        if n != int(n):
            raise ValueError("n shouldn't be float")
        else : 
            out = self.power_complex(n)
            return Complex(out[0][0], out[1][0])
        
    def __truediv__(self, other):
        if isinstance(other, Complex):
            det = 1 / ((other.C[0][0] ** 2) - (other.C[1][0] * other.C[0][1]))
            inv_z1 = scal_mult([[other.C[0][0], other.C[1][0]], [other.C[0][1], other.C[1][1]]], det)
            out = mat_mult(self.C, inv_z1)
            return Complex(out[0][0], out[1][0])
        else : 
            out =  scal_mult(self.C, 1/other)
            return Complex(out[0][0], out[1][0])
            
        
    def __repr__(self):
        p = "+"
        if self.C[1][0] < 0 : 
            p = "-"
        if self.C[1][0] == 1 or self.C[1][0] == -1: 
            if self.C[0][0] != 0:
                return f"{self.C[0][0]} {p} i"
            elif self.C[1][0] < 0 :
                return "-i"
            else : 
                return "i"
        elif self.C[1][0] == 0: 
            return f"{self.C[0][0]}"
        elif self.C[0][0] == 0:
            return f"{self.C[1][0]}i"
        else : 
            return f"{self.C[0][0]} {p} {abs(self.C[1][0])}i"
        
#_____FONCTIONS COMPLEXES_____

def exp(z): 
    n = 20
    total = Complex(0, 0)
    for i in range(0, n + 1):
        X = (z ** i) * (1 / factorial(i))
        total += X
    return total

def sin(z):
    n = 20
    total = Complex(0, 0)
    total += z
    d = [1, - 1]
    for i in range(1, n + 1):
        X = (z ** (2 * i + 1)) * (1 /factorial(2 * i + 1)) * d[i % 2]
        total += X
    return total

def cos(z):
    n = 20
    total = Complex(1, 0)
    d = [1, -1]
    for i in range(1, n + 1):
        X = (z ** (2 * i)) * (1 /factorial(2 * i)) * d[i % 2]
        total += X
    return total
    

#_____TESTS_____

if __name__ == "__main__":
    
    import math as m
    import matplotlib.pyplot as plt
    

    z = Complex(1, 1)
    z1 = Complex(0, 1)
    z *= z1
    print(z)

        

    
    

            
        
