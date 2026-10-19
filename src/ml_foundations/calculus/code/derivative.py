def numarical_derivative(f,x,h=1e-7):
    return (f(x+h)-f(x-h))/ (2 * h)

def f(x):
    return x**2

if __name__=="__main__":

    for x in [-2, -1, 0, 1, 2]:
        numerical = numarical_derivative(f, x)
        analytical = 2 * x
        print(f"{x=}  f'(x) {numerical=:.6f}  {analytical=}")