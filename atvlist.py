# mostre-me as seguintes listas, derivadas de: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#intervalo de 1 a 9
intervalo = list(range(1,10))
print(intervalo)
#intervalo 9 a 13
intervalo = list(range(9,14))
print(intervalo)
#numeros pares
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
print(pares)      
#numeros impares
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
impares = []
for num in lista:
    if num % 2 != 0:
        impares.append(num)
print(impares)
#todos os multiplos de 2, 3 e 4
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def eh_multiplos_de_2_3_4(num):
    return num % 2 == 0 and num % 3 == 0 and num % 4 == 0
    
multiplos_2_3_4 = list(filter(eh_multiplos_de_2_3_4, pares))
print(multiplos_2_3_4)
 
#lista reserva
lista_original = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista_reserva = lista_original.copy()
lista_reserva.append(16)
print("Lista original:", lista_original)
print("lista reserva:", lista_reserva)
#razão entre a soma do intervala de 10 a 15 pelo o intervala de 3 a 9 em float
intervalo_10_15 = list(range(10,16))
intervalo_3_9 = list(range(3,10))

soma_10_15 = sum(intervalo_10_15)
soma_3_9 = sum(intervalo_3_9)

razão = soma_10_15 / soma_3_9
print (f"a razão entrea a somas é: {razão: .4f}")




  
