
def derive(f, x, h=0.0001):
    derivate = (f(x+h)-f(x))/h
    return derivate