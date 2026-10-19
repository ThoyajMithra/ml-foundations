def numarical_derivative(f,x,h=1e-7):
    return (f(x+h)-f(x-h))/ (2 * h)

def numerical_second_derivative(f,x,h=1e-7):
    hlp = lambda v: numarical_derivative(f, v, h=1e-4)
    return numarical_derivative(hlp,x)


def f(x):
    return x**2

if __name__=="__main__":

    for x in [-2, -1, 0, 1, 2]:
        numerical = numarical_derivative(f, x)
        first = 2 * x
        second =numerical_second_derivative(f,x)
        print(f"{x=}  f'(x) {numerical=:.6f}   {second=:.6f}")