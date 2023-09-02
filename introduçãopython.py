print('Hello World') #Saída: Hello World

#Somando valores
print(5+9)

#Tipos e Variáveis
age = 21
print(age)
print(type(age))

age = "21"
print(age)
print(type(age))

valueA = 15
valueB = 20

result = valueA + valueB
print(result)

#Ponto Flutuante

height = 1.86
print(type(height))

#O Calculo para a maquina de ponto flutuante é dificil

sum = 0.1 + 0.5
print(sum)
#0.30000000000000004

#Tipos de Formatação

print(round(sum)) #Aqui só vai pegar o numero antes da virgula
print(round(sum, 2)) #Aqui é pra pegar dois numeros dps da virgula
print("%.2f" % sum)
print("{0:.2f}".format(sum))
print(int(sum)) #Aqui vai aredondar o numero
