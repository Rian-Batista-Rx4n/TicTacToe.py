import random
from time import sleep as s
ganhou = contador = jogo = o = x = velha = speed = 0
dificuldade = 4
while True:
    jogar = int(input("""\nJogar com BOT?
[ 1 ] SIM
[ 2 ] NÃO
--> """))
    if jogar == 1 or jogar == 2:
        break
s(0.5)
if jogar == 1:
    print('\nPS: Dificuldades 1 e 2 ( EASY $ NORMAL ) será disponivel em breve.\n\n')
    s(1)
    while True:
        dificuldade = int(input(f"""Dificuldade
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[ 3 ] HARDWARE
[ 8 ] RANDOMWARE / EASY
[ 9 ] BURRA VS ARTIFICIAL (COMPUTADOR VC COMPUTADOR)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
SPEED = {speed} (padrão: 0) 
[ 0 ] SPEED (TROCAR VELOCIDADE DO BOT)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
--> """))
        if dificuldade == 1 or dificuldade == 2 or dificuldade == 3 or dificuldade == 8 or dificuldade == 9:
            break
        if dificuldade == 0:
            s(1)
            while True:
                speed = float(input('\nVelocidade em Segundos (racionais usar "." por exemplo "0.1"): \n'))
                if speed < 0:
                    print('Valor digitado invalido!')
                if speed > -1:
                    break
        else:
            print('SÉ É TONTO?')
            s(1)
            print('')
while True:
    vez = random.randint(0, 1)
    jafoi = list()
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    if velha >= 9 and ganhou == 2:
        s(1)
        print('\n'*100)
        print('DEU VELHA!')
        print(jogo)
        opc = str(input('Jogar de novo? [S/N]: ')).upper().strip()
        ganhou = 0
        velha = 0
        if opc == 'N':
            print('\n' * 100)
            print('Obrigado por testar meu jogo: R X 4 N')
            break
    elif ganhou == 1:
        s(1)
        print(jogo)
        opc = str(input('Jogar de novo? [S/N]: ')).upper().strip()
        ganhou = 0
        velha = 0
        if opc == 'N':
            print('\n'*100)
            print('Obrigado por testar meu jogo: R X 4 N')
            break
    print('=' * 30)
    print(f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
''')
    print('=' * 30)
    s(1)
    while not ganhou >= 1:
        if velha >= 9:
            vez = 1
            ganhou = 2
            print('\n')
        elif vez == 1:
            s(speed)
            if velha >= 9:
                ganhou = 2
                print('\n')
            elif dificuldade == 9:
                x = random.randint(1, 9)
            else:
                x = int(input('Qual posição você quer o "X": '))
            contador = jafoi.count(x)
            if contador != 0:
                print('Posição já está sendo utilizada!')
            elif x == '':
                print('Invalido!')
            elif x <= 0:
                print('Valor invalido!')
            elif x >= 10:
                print('Valor invalido!')
            else:
                vez = 0
                velha += 1
                jafoi.append(x)
                print('='*30)
                if x == 1:
                    a = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
    '''
                    print(jogo)
                elif x == 2:
                    b = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 3:
                    c = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
    '''
                    print(jogo)
                elif x == 4:
                    d = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 5:
                    e = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 6:
                    f = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 7:
                    g = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 8:
                    h = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
                elif x == 9:
                    i = 'X'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                    '''
                    print(jogo)
            if a == d == g == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if b == e == h == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if c == f == i == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if a == b == c == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if d == e == f == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if g == h == i == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if a == e == i == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if c == e == g == 'X':
                s(2)
                print('\n' * 100)
                print('X ganhou!')
                ganhou = 1
            if ganhou == 1:
                vez = 1
        if vez == 0 and ganhou == 0 and velha < 9:
            s(speed)
            print('=' * 30)
            if dificuldade == 9 or dificuldade == 8:
                o = random.randint(1, 9)
            if jogar == 2:
                o = int(input('Qual posição você quer o "O": '))
            else:
                if dificuldade == 3:
                    if a == b == 'O' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    elif a == c == 'O' and b == 2:
                        o = 2
                        b = 'O'
                        vez = 1
                    elif b == c == 'O' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif d == e == 'O' and f == 6:
                        o = 6
                        f = 'O'
                        vez = 1
                    elif d == f == 'O' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == f == 'O' and d == 4:
                        o = 4
                        d = 'O'
                        vez = 1
                    elif g == h == 'O' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif g == i == 'O' and h == 8:
                        o = 8
                        h = 'O'
                        vez = 1
                    elif h == i == 'O' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif a == d == 'O' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif a == g == 'O' and d == 4:
                        o = 4
                        d = 'O'
                        vez = 1
                    elif d == g == 'O' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif b == e == 'O' and h == 8:
                        o = 8
                        h = 'O'
                        vez = 1
                    elif b == h == 'O' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == h == 'O' and b == 2:
                        o = 2
                        b = 'O'
                        vez = 1
                    elif c == f == 'O' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif c == i == 'O' and f == 6:
                        o = 6
                        f = 'O'
                        vez = 1
                    elif f == i == 'O' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    elif a == e == 'O' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif a == i == 'O' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == i == 'O' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif c == e == 'O' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif c == g == 'O' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == g == 'O' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    elif a == b == 'X' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    elif a == c == 'X' and b == 2:
                        o = 2
                        b = 'O'
                        vez = 1
                    elif b == c == 'X' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif d == e == 'X' and f == 6:
                        o = 6
                        f = 'O'
                        vez = 1
                    elif d == f == 'X' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == f == 'X' and d == 4:
                        o = 4
                        d = 'O'
                        vez = 1
                    elif g == h == 'X' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif g == i == 'X' and h == 8:
                        o = 8
                        h = 'O'
                        vez = 1
                    elif h == i == 'X' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif a == d == 'X' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif a == g == 'X' and d == 4:
                        o = 4
                        d = 'O'
                        vez = 1
                    elif d == g == 'X' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif b == e == 'X' and h == 8:
                        o = 8
                        h = 'O'
                        vez = 1
                    elif b == h == 'X' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == h == 'X' and b == 2:
                        o = 2
                        b = 'O'
                        vez = 1
                    elif c == f == 'X' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif c == i == 'X' and f == 6:
                        o = 6
                        f = 'O'
                        vez = 1
                    elif f == i == 'X' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    elif a == e == 'X' and i == 9:
                        o = 9
                        i = 'O'
                        vez = 1
                    elif a == i == 'X' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == i == 'X' and a == 1:
                        o = 1
                        a = 'O'
                        vez = 1
                    elif c == e == 'X' and g == 7:
                        o = 7
                        g = 'O'
                        vez = 1
                    elif c == g == 'X' and e == 5:
                        o = 5
                        e = 'O'
                        vez = 1
                    elif e == g == 'X' and c == 3:
                        o = 3
                        c = 'O'
                        vez = 1
                    if vez == 0:
                        o = random.randint(1, 9)
            contador = jafoi.count(o)
            if contador != 0:
                print('Posição já está sendo utilizada!')
            elif o == '':
                print('Invalido!')
            elif o <= 0:
                print('Valor invalido!')
            elif o >= 10:
                print('Valor invalido!')
            else:
                vez = 1
                velha += 1
                jafoi.append(o)
                if o == 1:
                    a = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 2:
                    b = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 3:
                    c = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 4:
                    d = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 5:
                    e = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 6:
                    f = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 7:
                    g = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 8:
                    h = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
                elif o == 9:
                    i = 'O'
                    jogo = f'''
          {a}  {b}  {c}
          {d}  {e}  {f}
          {g}  {h}  {i}
                                    '''
                    print(jogo)
            if a == d == g == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if b == e == h == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if c == f == i == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if a == b == c == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if d == e == f == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if g == h == i == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if a == e == i == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            if c == e == g == 'O':
                s(2)
                print('\n' * 100)
                print('O ganhou!')
                ganhou = 1
            print('=' * 30)
