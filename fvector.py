from typing import List
Vector = List[float]

def vector_add(v1: Vector,v2: Vector):
    #add corresponding elements of vectors
    return[v_i+w_i for v_i, w_i in zip(v1,v2)]

def vector_subtracting(v1: Vector,v2: Vector):
    #add corresponding elements of vectors
    return[v_i-w_i for v_i, w_i in zip(v1,v2)]


# Sum different vectors
def vector_sum(vectors: List[Vector]):
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


# Multiply vector by a scalar
def scalar_multiply(c: float, v: Vector):
    return [c * v_i for v_i in v]

# Mean of the vectors
def vectors_mean(vs: List[Vector]):
    n=len(vs)
    return(








