# Código python que verifica se uma frase é um pangrama
from unidecode import unidecode

def verificar_pangrama(frase):
    # Converte a frase para minúsculas e remove os espaços
    frase = frase.lower().replace(" ", "")
    frase = unidecode(frase)
    # Cria um conjunto com as letras do alfabeto
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    # Cria um conjunto com as letras da frase
    letras = set(frase)
    # Verifica se o conjunto das letras da frase é igual ao do alfabeto
    return letras == alfabeto

# Teste unitário que verifica se a função verificar_pangrama funciona corretamente

import pytest

def test_retorna_verdadeiro_quando_frase_pangrama():
    # define uma frase que é um pangrama
    frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"
    # chama a função verificar_pangrama com a frase
    frase_eh_pangrama = verificar_pangrama(frase)
    # verifica se o resultado é verdadeiro
    assert frase_eh_pangrama

def test_retorna_falso_quando_frase_nao_pangrama():
    # define uma frase que não é um pangrama
    frase = "A raposa marrom pula sobre o cachorro preguiçoso"
    # chama a função verificar_pangrama com a frase
    frase_eh_pangrama = verificar_pangrama(frase)
    # verifica se o resultado é falso
    assert not frase_eh_pangrama

# Teste integrado que verifica se o código funciona com uma frase digitada pelo usuário
# Importa a biblioteca msvcrt
import msvcrt
# Importa a biblioteca time
import time

def test_verifica_pangrama_com_entrada_do_usuario():
    # Define um tempo limite em segundos para o usuário digitar uma frase
    tempo_limite = 10
    # Define uma variável para armazenar a frase digitada pelo usuário
    frase = ""
    # Define uma variável para armazenar o tempo inicial
    tempo_inicial = time.time()
    # Mostra uma mensagem na tela pedindo ao usuário que digite uma frase
    print(f"Digite uma frase em {tempo_limite} segundos: ", end="")
    # Enquanto o tempo limite não for excedido e o usuário não pressionar Enter
    while time.time() - tempo_inicial < tempo_limite and not frase.endswith("\n"):
    # Se o usuário pressionar alguma tecla
        if msvcrt.kbhit():
            # Lê a tecla pressionada
            tecla = msvcrt.getche()
            # Se a tecla for Enter, adiciona uma quebra de linha à frase
            if tecla == b"\r":
                frase += "\n"
            # Se a tecla for Backspace, remove o último caractere da frase
            elif tecla == b"\x08":
                frase = frase[:-1]
            # Se a tecla for outra, adiciona o caractere à frase
            else:
                frase += tecla.decode()
    # Remove a quebra de linha da frase
    frase = frase.strip()
    # Verifica se a frase digitada pelo usuário é um pangrama
    assert verificar_pangrama(frase)
