import random
import time

CYAN  = "\033[1;36m"
RED   = "\033[1;31m"
RESET = "\033[0;0m"

print('Bem vindo ao LUCASSI Refine Simulator!')
qtditem = int(input('Insira a quantidade de itens +4 para prosseguir: '))
qtditem4 = qtditem
elunium = [0 , 0, 0]
isucess = [0, 0, 0, 0, 0, 0]
c = [0, 0, 0, 0, 0, 0]
iquebra = [0]

time.sleep(0.5)

def refino5(qtditem4):
    qtditem4 -= 1
    elunium[1] += 1
    chance = int(90)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+4 para +5) Aprimoramento completado com sucesso.', RESET)
        isucess[0] += 1
        c[0] += 1
    else:
        resultado = False
        print(RED, '(+4 para +5) Aprimoramento falhou.', RESET)
        iquebra[0] += 1
    print('********************************')
    time.sleep(0.5)
    if resultado:
        refino6()    
    
    return qtditem4

def refino6():
    isucess[0] -= 1
    elunium[1] += 1
    chance = int(70)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+5 para +6) Aprimoramento completado com sucesso.', RESET)
        isucess[1] += 1
        c[1] += 1
    else:
        resultado = False
        print(RED, '(+5 para +6) Aprimoramento falhou.', RESET)
        iquebra[0] += 1
    print('********************************')
    time.sleep(0.5)
    if resultado:
        refino7()   

def refino7():
    isucess[1] -= 1
    elunium[1] += 1
    chance = int(70)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+6 para +7) Aprimoramento completado com sucesso.', RESET)
        isucess[2] += 1
        c[2] += 1
    else:
        resultado = False
        print(RED, '(+6 para +7) Aprimoramento falhou.', RESET)
        iquebra[0] += 1
    print('********************************')
    time.sleep(0.5)        
    if resultado:
        refino8()  

def refino8():
    isucess[2] -= 1
    elunium[2] += 1
    chance = int(40)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+7 para +8) Aprimoramento completado com sucesso.', RESET)
        isucess[3] += 1
        c[3] += 1
    else:
        resultado = False
        print(RED, '(+7 para +8) Aprimoramento falhou.', RESET)
        print('''O refino retornou para +6... 
Realizando nova tentativa de aprimoramento.''')
        isucess[2] += 1
    print('********************************')
    time.sleep(0.5)    
    if resultado:
        refino9()
    else:
        refino7()  

def refino9():
    isucess[3] -= 1
    elunium[2] += 1
    chance = int(40)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+8 para +9) Aprimoramento completado com sucesso.', RESET)
        isucess[4] += 1
        c[4] += 1
    else:
        resultado = False
        print(RED, '(+8 para +9) Aprimoramento falhou.', RESET)
        print('''O refino retornou para +7... 
Realizando nova tentativa de aprimoramento.''')
        isucess[3] += 1
    print('********************************')
    time.sleep(0.5)    
    if resultado:
        refino10()
    else:
        refino8()

def refino10():
    isucess[4] -= 1
    elunium[2] += 1
    chance = int(20)
    tentativa = random.randint(1, 100)
    if tentativa <= chance:
        resultado = True
        print(CYAN, '(+9 para +10) Aprimoramento completado com sucesso.', RESET)
        isucess[5] += 1
        c[5] += 1
    else:
        resultado = False
        print(RED, '(+9 para +10) Aprimoramento falhou.', RESET)
        print('''O refino retornou para +8... 
Realizando nova tentativa de aprimoramento.''')
        isucess[4] += 1
    print('********************************')
    time.sleep(0.5)    
    if resultado == False:
        refino9()

while qtditem4 > 0:
    qtditem4 = refino5(qtditem4)
    

print('***** RESUMO DA SILUMAÇÃO *****')
print('Quantidade de Itens +4: ', qtditem)
print('Itens +5: ', c[0])
print('Itens +6: ', c[1])
print('Itens +7: ', c[2])
print('Itens +8: ', c[3])
print('Itens +9: ', c[4])
print('Itens +10: ', c[5])
print('Itens Quebrados: ', iquebra)
print('Qtd de Elunium Comum: ', elunium[0])
print('Qtd de Elunium Enriquecido: ', elunium[1])
print('Qtd de Elunium Perfeito: ', elunium[2])

input('Pressione qualquer tecla para fechar...')