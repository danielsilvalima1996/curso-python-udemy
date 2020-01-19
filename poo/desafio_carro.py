#!/usr/bin/python3
class Carro:
    def __init__(self, velocidade_maxima=180):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        # Resposta do Daniel
        # if self.velocidade_atual + delta <= self.velocidade_maxima:
        #     self.velocidade_atual += delta
        #     return self.velocidade_atual
        # else:
        #     self.velocidade_atual = self.velocidade_maxima
        #     return self.velocidade_maxima

        # Resposta professor
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        # Resposta do Daniel
        # if 0 <= self.velocidade_atual >= delta:
        #     self.velocidade_atual -= delta
        #     return self.velocidade_atual
        # else:
        #     self.velocidade_atual = 0
        #     return self.velocidade_atual

        # Resposta professor
        nova = self.velocidade_atual - 20
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print('Acelerando', c1.acelerar(8))
        # print('atual', c1.velocidade_atual)
        # print('maxima', c1.velocidade_maxima)

    for _ in range(10):
        print('Freando', c1.frear(20))
        # print('atual', c1.velocidade_atual)
        # print('maxima', c1.velocidade_maxima)
