#!C:\Users\tjwtb\anaconda3\pkgs\python-3.8.8-hdbf39b2_5\python.exe
print("content-type: text/html\n\n")

def RotarMatriz(Matriz):
    X = len (Matriz[0])
    for i in range(X // 2):
        for j in range(i,X-i-1):
            aux = Matriz[i][j] #posicion 1, 2
            Matriz[i][j]=Matriz[X-1-j][i] #posicion 7, 6
            Matriz[X-1-j][i] = Matriz[X-1-i][X-1-j] #posicion 9, 8
            Matriz[X-1-i][X-1-j] = Matriz[j][X-1-i] #posicion 3, 4
            Matriz[j][X-1-i] = aux  #se usa la auxiliar
        
    
Matriz = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def resultado():
    valor = Matriz
    x = 5
    for i in range(x):
        print(f"{valor[0]}\r\n")
        print("<br>")
        print(f"{valor[1]}\r\n")
        print("<br>")
        print(f"{valor[2]}\r\n")
        print("<br>")
        print("Siguiente giro")
        print("<br>")
        RotarMatriz(Matriz)

resultado()

#RotarMatriz(Matriz)
#imprimirMatriz(Matriz)
