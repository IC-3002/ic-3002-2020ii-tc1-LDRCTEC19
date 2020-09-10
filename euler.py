"Luis Diego Rodriguez Cruz 2018148987"
def e_cuadratica(n):
    # Implemente esta función
    if n == 0:
        return 1
    elif n == 1:
        return 1 
    else return ((1/factorial(e_cuadratica(n)))+((1/factorial(e_cuadratica(n-1)))


def e_lineal(n):
    # Implemente esta función
    e = 1
    for i in range(0,n):
    	e = e + (1/factorial(n))
    return e
