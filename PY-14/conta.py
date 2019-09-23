import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
        
    def imprime(self):
        print('data abertura: {}'.format(self.data_abertura))
        print('transações: ')
        for t in self.transacoes:
            print('-', t)
        
        
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
        
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        print('inicializando uma conta')
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        
    def deposita(self, valor):
        self._saldo += valor
        self._historico.transacoes.append('depósito de {}'.format(valor))
        
    def saca(self, valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append('saque de {}'.format(valor))
            return True
        
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        
        if (retirou):
            destino.deposita(valor)
            self._historico.transacoes.append('transferencia de {} para conta'.format(valor, destino.numero))
            return True
        else:
            return False
        
    def extrato(self):
        print('numero: {} \nsaldo: {}'.format(self._numero, self._saldo))
        self._historico.transacoes.append('tirou extrato - saldo de {}'.format(self._saldo))
