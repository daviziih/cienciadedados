#Velocidade projetil lançado metro por segundo.

VELOCIDADE;
DISTANCIA_METROS = 10;
TEMPO_SEGUNDOS = 10;

VELOCIDADE = (DISTANCIA_METROS * 1000) / (TEMPO_SEGUNDOS * 60);

print(VELOCIDADE);

#Calcular volume de objetos geométricos.

VOLUME_ESPERA = 0;
VOLUME_CILINDRO = 0;
VOLUME_RETANGULO = 0;

RAIO = 3;
ALTURA = 2;
LARGURA = 2;
COMPRIMENTO = 12;

VOLUME_ESPERA = (4/3) * 3.1415 * (RAIO * RAIO * RAIO);
VOLUME_CILINDRO = 3.1415 * (RAIO * RAIO) * ALTURA;
VOLUME_RETANGULO = COMPRIMENTO * LARGURA * ALTURA

print("Volume Esfera ", VOLUME_ESPERA);
print("Volume Cilindro ", VOLUME_CILINDRO);
print("Volume Retangulo ", VOLUME_RETANGULO);

#Manipulação de números.

numero = 10;

valor1 = 5;
valor2 = 2;

print("Numero", numero)
print(" ")
print("Antecessor:", numero - 1)
print("Sucessor:", numero + 1)
print("Dobrado:", numero * 2)
print("Multiplicado 3.25:", numero * 3.25)
print("Multiplicado -1.26:", numero * -1.26)
print(" ")
print("Valor 1:", valor1)
print("Valor 2:", valor2)
print(" ")
print("Soma:", valor1 + valor2)
print("Subtração:", valor1 - valor2)
print("Divisão:", valor1 / valor2)
print("Multiplicação:", valor1 * valor2)

#Conversão de temperatura e métrica no jogo

F = 0;
Celsius = 20;
C = 18;

milhas = 0;
quilometros = 20;
q = 0;

metros = 0;
pes = 20;
pe = 0;

F = (9 * Celsius + 160) / 5
C = (F - 32) * (5 / 9)

milhas = quilometros * 0.621371
q = milhas * 1.60934

metros = pes * 0,3048
pe = metros * 3,28084

print("Fahrenheit: ", F)
print("Celsius: ", C)
print("Milhas: ", milhas)
print("Quilometros: ", q)
print("Metros: ", metros)
print("Pes: ", pe)

x = [1, 2, 3]
print(x)

x = 5
y = "10"

result = x + int(y)

print(result)
