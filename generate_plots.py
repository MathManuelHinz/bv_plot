import scipy.integrate as integrate
from math import pi,cos,sin
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

def sin_plot(n=100):
    xs=[4*pi/(n-1)*i for i in range(n)]
    ys1=[integrate.quad(lambda t: abs(cos(t)),0,x)[0] for x in xs]
    ys2=[y-sin(xs[i]) for i,y in enumerate(ys1)]
    ys3=[ys1[i]-ys2[i] for i in range(n)]
    plt.clf()
    plt.plot(xs,ys1,label="f_1")
    plt.plot(xs,ys2,label="f_2")
    plt.plot(xs,ys3,label="sin")
    plt.legend()
    plt.savefig("sin.png")

def polynomial_plot(n=100):
    #x^3 - 6x^2 + 4x + 12
    f=lambda x: 3*x**2-12*x+4
    F=lambda x:x**3 - 6*x**2 + 4*x + 12
    xs=[-4+12/(n-1)*i for i in range(n)]
    ys1=[integrate.quad(lambda t: abs(f(t)),-4,x)[0] for x in xs]
    ys2=[y-F(xs[i]) for i,y in enumerate(ys1)]
    ys3=[ys1[i]-ys2[i] for i in range(n)]
    plt.clf()
    plt.plot(xs,ys1,label="f_1")
    plt.plot(xs,ys2,label="f_2")
    plt.plot(xs,ys3,label="$x^3 - 6x^2 + 4x + 12$")
    plt.legend()
    plt.savefig("polynomial.png")

def generate_plot(f,F,a,b,plot_path="plot.png",n=100):
    xs=[-a+b/(n-1)*i for i in range(n)]
    ys1=[integrate.quad(lambda t: abs(f(t)),a,x)[0] for x in xs]
    ys2=[y-F(xs[i]) for i,y in enumerate(ys1)]
    ys3=[ys1[i]-ys2[i] for i in range(n)]
    plt.clf()
    plt.plot(xs,ys1,label="f_1")
    plt.plot(xs,ys2,label="f_2")
    plt.plot(xs,ys3,label="$F$")
    plt.legend()
    plt.savefig(plot_path)

if __name__ == "__main__":
    sin_plot()
    polynomial_plot()
    generate_plot(lambda x: -sin(x), cos,-1,5)