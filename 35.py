import argparse
import matplotlib.pyplot as plt

def traccia_lineare(n):
    x = [i/10 for i in range(101)]
    y = [n * xi for xi in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funzione Lineare: y = {} * x'.format(n))
    plt.savefig('grafico_lineare.png')

def traccia_polinomiale(n):
    x = [i/10 for i in range(101)]
    y = [xi ** n for xi in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funzione Polinomiale: y = x^{}'.format(n))
    plt.savefig('grafico_polinomiale.png')

def traccia_esponenziale(n):
    x = [i/10 for i in range(101)]
    y = [n ** xi for xi in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funzione Esponenziale: y = {}^x'.format(n))
    plt.savefig('grafico_esponenziale.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lineare', action='store_true')
    parser.add_argument('--polinomiale', action='store_true')
    parser.add_argument('--esponenziale', action='store_true')
    parser.add_argument('--numero', type=float, required=True)
    args = parser.parse_args()

    if args.lineare:
        traccia_lineare(args.numero)

    if args.polinomiale:
        traccia_polinomiale(args.numero)

    if args.esponenziale:
        traccia_esponenziale(args.numero)

    plt.show()
