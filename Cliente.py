import socket
import pickle

def escolha_operacao(operacao):
    if operacao == '+':
        return 1
    elif operacao == '-':
        return 2
    elif operacao == '*':
        return 3
    elif operacao == '/':
        return 4

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

cliente.connect((host, port))

primeiro_numero = input("Digite um numero: ")
segundo_numero = input("Digite um numero: ")
operacao = input("Digite a operacao a ser realizada: ")

operacao = escolha_operacao(operacao)

arr = [int(primeiro_numero), int(segundo_numero), int(operacao)]

cliente.send(pickle.dumps(arr))

resultado = cliente.recv(4096)
a = pickle.loads(resultado)
print(a)

cliente.close()