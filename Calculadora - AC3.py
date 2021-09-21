import abc
from logging import raiseExceptions
from unittest import TestCase,main


class Calculadora(object):
    def calcular(self,arg1,arg2,oper):
        operacao = OperacaoFabrica().criar(oper)
        if(operacao == None):
            return 0
        else:
            result = operacao.executar(arg1,arg2)
            return result

class OperacaoFabrica(object):
    def criar(self, oper):
        if (oper == 'soma'):
            return Soma()
        elif (oper == 'subtracao'):
            return Subtracao()
        elif (oper == 'divisao'):
            return Divisao()
        elif (oper == 'multiplicacao'):
            return Multiplicacao()
        elif (oper == 'potenciacao'):
            return Potenciacao()
        elif (oper == 'resto'):
            return Resto()

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self,arg1,arg2):
        pass


class Soma(Operacao):
    def executar(self, arg1, arg2):
        result = arg1 + arg2
        return result
class Subtracao(Operacao):
    def executar(self, arg1, arg2):
        result = arg1 - arg2
        return result
class Divisao(Operacao):
    def executar(self, arg1, arg2):
        result = arg1 / arg2
        return result
class Multiplicacao(Operacao):
    def executar(self, arg1, arg2):
        result = arg1 * arg2
        return result    
class Resto(Operacao):
    def executar(self,arg1,arg2):
        result = arg1%arg2
        return result
class Potenciacao(Operacao):
    def executar(self, arg1, arg2):
        result = arg1 ** arg2
        return result


class Testes(TestCase):
    def test_soma(self):
        calculo_soma = Calculadora()
        result = calculo_soma.calcular(2,3,'soma')
        self.assertEqual(result,5)
        
    def test_multiplicacao(self):
        calculo_multiplicacao = Calculadora()
        result = calculo_multiplicacao.calcular(2,5,'multiplicacao')
        self.assertEqual(result,10)

    def test_divisao(self):
        calculo_divisao = Calculadora()
        result = calculo_divisao.calcular(2,4,'divisao')
        self.assertEqual(result,0.5)

    def test_subtracao(self):
        calculo_subtracao = Calculadora()
        result = calculo_subtracao.calcular(10,50,'subtracao')
        self.assertEqual(result, -40)

    def test_potenciacao(self):
        calculo_potencia = Calculadora()
        result = calculo_potencia.calcular(4,4,'potenciacao')
        self.assertEqual(result,256)
    def test_resto(self):
        calculo_resto= Calculadora()
        result= calculo_resto.calcular(99,2,'resto')
        self.assertEqual(result,1)


banner = """"CALCULADORA
Operações:\n
    Multiplicacao x
    Subtracao -    
    Soma +
    Divisao /
    Potenciacao n²
    Resto %\n"""


def codigo():
    operacoes=['soma','subtracao','multiplicacao','divisao','potenciacao','resto']
    operacao=input("Digite o nome da operação, sem acento:\n").lower()
    if operacao not in operacoes:
        print("Diogite uma operação válida!")
        codigo()
    arg1=float(input("Digite o valor 1:\n"))
    arg2=float(input("Digite o valor 2:\n"))
    result = Calculadora().calcular(arg1,arg2,operacao)
    print ("result = {0:g}".format(float(result)))


print(banner)
codigo()
main()