# LinAl.py
# Data Science From Scratch - Joel Grus Ch. 4
import math

height_weight_age = [ 150   #cm
                     65   #kg
                     26 ] #yrs
scores = [ 85, 90, 76, 92]


### Vectors
def add_vectors(u, v):
    '''Adds two vectors u and v'''
    return [u_i + v_i for u_i,v_i in zip(u,v)]  ### This is a nifty trick for list comprehensions

def subtract_vectors(u, v):
    '''Subtracts two vectors u and v'''
    return [u_i - v_i for u_i, v_i in zip(u,v)]

def sum_vectors(vectors):
    '''Subtracts n vectors in vectors'''
    ret_val = vectors[0]                     ### ret_val = 'return value'
    for v in vectors[1:]:                    ### I wanted to use sum, but
        ret_val = add_vectors(ret_val, v)    ### thought it might cause problems
    return ret_val
## sum_vector = partial(reduce, add_vector)

def scalar_multiply(a, vector):
    ''' a - scalar '''
    return [a * v_i for v_i in vector]

def mean_vector(vectors):
    ''' Return a vector whose ith component is the mean of each ith element.'''
    kNum = len(vectors)
    return scalar_multiply(1/kNum, sum_vector(vectors))

def dot(u, v):
    '''u_i * v_i + ... + u_n * v_n'''
    return sum(u_i * v_i for u_i, v_i in zip(u,v))

def sum_of_squares(v):
    '''v_1 * ... * v_n'''
    return dot(v,v)

def magnitude(v):
    '''Return magnitude of a vector, v'''
    return math.sqrt(sum_of_squares(v))

def square_distance(u, v):
    '''(u_i * v_i) ** 2 + ... + (u_n * v_n) ** 2'''
    return sum_of_squares(subtract_vectors(u,v))

def distance(u,v):
    return magnitude(subtract_vectors(u,v))


### Matrices
A = [[1, 2, 3
      4, 5, 6]]
B = [[1, 2
      3, 4
      5, 6]]

def shape(A):