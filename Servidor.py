import socket
import pickle
import threading

def calcular_operacao(numeros):
    if numeros[2] == 1: # +
        return numeros[0]+numeros[1]
    elif numeros[2] == 2: # -
        return numeros[0]-numeros[1]
    elif numeros[2] == 3: # *
        return numeros[0]*numeros[1]
    elif numeros[2] == 4: # /
        return numeros[0]/numeros[1]

def thread_socket(conexao):
    print('dentro da thread...')

    numeros_bytes = conexao.recv(4096)
    numeros = pickle.loads(numeros_bytes)
    
    calculo = calcular_operacao(numeros)
    conexao.send(pickle.dumps(calculo))

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

servidor.bind((host, port))
print('Servidor funcionando...')

servidor.listen()

while True:
    print ("Esperando conexão!!")
    conexao, endereco_ip_do_cliente = servidor.accept()

    t = threading.Thread(target=thread_socket, args=(conexao,))
    t.start()