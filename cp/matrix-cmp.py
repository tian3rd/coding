'''
Problem: check the product of matrix A and B is equal to C. 

Solution 1: 
the usual complexity is O(n^3) for matrices production: 
to get one element, one need to go over from 1 to n --> O(n);
to get n*n elements, one need to repeat that n*n times; 
thus, the total complexity is O(n^3). 

Solution 2: 
Freivalds algorithm: https://en.wikipedia.org/wiki/Freivalds%27_algorithm. 
generate a random vector v of n-dim, check if ABv == Cv
implementation as follows

Input file: 
1st line: n (dimension of matrix) is an int
2nd to n+1 line: n*n matrix A of all ints
n+2 to 2n+1 line: n*n matrix B of all ints
2n+2 to 3n+1 line: n*n matrix C of all ints

'''

from random import randint
from sys import stdin

# first, read the dimension from file
def read_dim(): 
    return stdin.readline()

# second, read 3 matrices line by line
def read_arr():
    arr = map(int, stdin.readline.split())
    return arr

def read_mat(dim): 
    mat = []
    for _ in range(dim): 
        mat.append(read_arr())
    return mat

# third, calculate the product of a matrix and a vector (reducing complexity)
def multiply_mat_vec(mat, vec): 
    dim = len(vec)
    rtn = []
    for i in range(dim): 
        rtn.append(sum(mat[i][j] * vec[j] for j in range(dim)))
    return rtn

# fourth, generate a random vector
def random_vec(dim): 
    vec = []
    for _ in range(dim): 
        vec.append(randint(1000000))
    return vec

if __name__ == "__main__": 
    dim = read_dim
    A = read_mat(dim)
    B = read_mat(dim)
    C = read_mat(dim)
    v = random_vec(dim)
    