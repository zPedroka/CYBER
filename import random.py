import os
import random
import sys
import threading
import time

class Cofre:
    def __init__(self):
        self.senha = random.randint(0, 99999)
        self.aberto = False

    def verificar_senha(self, tentativa):
        if tentativa == self.senha:
            self.aberto = True
            return True
        else:
            return False

class Hacker(threading.Thread):
    def __init__(self, nome, cofre):
        threading.Thread.__init__(self)
        self.nome = nome
        self.cofre = cofre

    def run(self):
        global tentar
        tentativa = 0
        while tentar:
            if not self.cofre.verificar_senha(tentativa):
                tentativa += 1
                print(f'{self.nome}: Tentativa {tentativa}')
                time.sleep(0.1)
            else:
                print(f'{self.nome}: Cofre aberto!')
                self.cofre.aberto = True
                tentar = False
                break


class Policia(threading.Thread):
    def __init__(self, cofre):
        threading.Thread.__init__(self)
        self.cofre = cofre

    def run(self):
        global tentar
        time.sleep(10)
        if not self.cofre.aberto:
            print('A polícia pegou os hackers e eles estão presos!')
            tentar = False
            
tentar = True
cofre = Cofre()
hacker1 = Hacker('Hacker 1', cofre)
hacker2 = Hacker('Hacker 2', cofre)
policia = Policia(cofre)

hacker1.start()
hacker2.start()
policia.start()

hacker1.join()
hacker2.join()
policia.join()