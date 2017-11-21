# se crearan las siguientes funciones para imprimir una matriz y un vector,
# ya que este pprocedimiento se realiza varias veces

# funcion que imprime un vector dado, se usara mas adelante
def printVector(vector):
    print(vector)
# funcion que imprime una matriz dada, seusara mas adelante
def printMatriz(matriz):
    for i in range (len(matriz)):
        print (matriz[i])


print("[----Interpolacion polinomica newton]----")
# captura del el grade del polinomio
n = int( input("Ingrese el grado del polinomio a evaluar: ") )

# creacion de la  matriz
matriz=[0.0]*n
for i in range (n):
    matriz[i]=[0.0]*n # la matriz es inicializada en 0.0

    # creacion de un vector inicializado en 0.0
vect=[0.0]*n    # se usa vect, ya que vector es una palabra reservada,

#impresion de la matriz recien generada
print("matriz")
printMatriz(matriz)
#impresion del vector recien generado
print("vector")
print(vect);


#capturando valores
for i in range (n):
    x = float(input("ingrese valor de    x[" + str(i) + "] "))
    y = float(input("ingrese valor de f(x)[" + str(i) + "] "))
    vect[i]=x
    matriz[i][0]=y

#impresion de la matriz con el contenido capturado
print("Matriz capturada")
printMatriz(matriz)
#impresion del veector capturado
print("vector capturado")
print(vect)

# captura del punto a evaluar
punto_a_evaluar=float( input( "ingrese el punto a evaluar: " ) )

print("calculando . . . .")

for i in range(1,n):
    for j in range (i,n):
        print("[i]= " + str(i) + " [j]= " + str(j)); # impresion de los valores en los que inicia el ciclo
        print("(" + str(matriz[j][i-1]) + "-" + str(matriz[j-1][i-1]) + ")/(" + str(vect[j]) + "-" + str(vect[j-i]) + ")")
        matriz[j][i] = (matriz[j][i-1]-matriz[j-1][i-1])/(vect[j]-vect[j-i])
        print("matriz[" + str(j) + "]" + "[" + str(i) + "] = " + str( (matriz[j][i-1] - matriz[j-1][i-1])/(vect[j]-vect[j-i]) ) )

print(" - - - - - - - - - - - - - ")

print("impresion de la matriz despues del proceso")
print("matriz despues del proceso")
printMatriz(matriz)

aprx = 0.0
mul = 1.0

for i in range (n):
    print("matriz[" + str(i) + "][" + str(i) + "]= " + str( matriz[i][i]) )
    mul=matriz[i][i]
    print("mul antes del ciclo [j]: " + str(mul))
    for j in range (1,i+1):
        mul = mul * (punto_a_evaluar - vect[j-1])
        print("mul en el ciclo de j: " + str(mul))
        aprx = aprx + mul

