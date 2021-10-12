import numpy as np
import test_main
import scipy

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    from math import pi 
    area = (2 * pi * r * r) + (2 * pi * r * h)
    if r > 0 and h > 0:
        return area
    else:
        return np.NaN
    

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if not isinstance(n, int):
        return None
    if n <= 0:
        return None
    elif n == 1:
        return np.array([1])
    a = 1
    b = 1
    i = 0
    lista = []
    while (i < n):
        lista.append(a)
        suma = a + b
        a = b
        b = suma
        i += 1
    return np.array([lista])


def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mt = M.T
    Mdet = np.linalg.det(M)
    if Mdet == 0:
        return np.NaN
    else:
        Minv = np.linalg.inv(M)
    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if n <= 0 or m <= 0:
        return None
    elif n > 0 and m > 0 and isinstance(n, int) and isinstance(m, int):
        M = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                if i > j:
                    M[i][j] = i
                else:
                    M[i][j] = j
    else:
        return None
    return M



if __name__ == '__main__':
    test_main.main()
