from time import sleep
from getpass import getpass
cont = 0
tentativa = 3
senha = getpass('Cadastre uma senha: ').strip()
senha2 = getpass('Confirme a senha: ').strip()
while True:
    if senha != senha2:
        tentativa += -1
        print(f'Senhas não conferem... Tente novamente')
        senha = getpass('Cadastre uma senha: ').strip()
        senha2 = getpass('Confirme a senha: ').strip()
    else:
        break
print('SENHA CADASTRADA COM SUCESSO')
chances = 3
for var in range(0, 3):
    conf = getpass('Digite a senha: ').strip()
    chances += -1
    if conf == senha:
        print('Bem Vindo')
        break
    elif conf != senha:
        cont += 1
        print(f'SENHA INVÁLIDA... \n{var+1}a tentativa')
        print(f'Restam {chances} tentativas')
        if cont == 3:
            print('Quantidades de tentativas excedidas')
            import time 
            def countdown(t): 
                while t: 
                    mins, secs = divmod(t, 60) 
                    timer = (f'{mins:02d}:{secs:02d}')
                    print(timer, end="\r") 
                    time.sleep(1) 
                    t -= 1
                print('Tente novamente') 
            t = print('Aguarde 30 segundos para nova tentantiva') 
            countdown(int(30))
            chances = 3
            for var in range(0, 3):
                conf = str(input('Digite a senha: ')).strip()
                chances += -1
                if conf == senha:
                    print('Bem Vindo')
                    break
                elif conf != senha:
                    cont += 1
                    print(f'SENHA INVÁLIDA... \n{var+1}a tentativa')
                    print(f'Restam {chances} tentativas')
                    print('O SISTEMA IRÁ BLOQUEAR EM BREVE...')
                    if var == 2:
                        print('SISTEMA BLOQUEADO. CONTATE SUPORTE')