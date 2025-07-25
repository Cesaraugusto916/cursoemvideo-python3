"""
Versão aprimorada por GitHub Copilot em 25/07/2025
Baseado no EXERCÍCIO 021: Tocando um MP3

Aprimoramentos realizados:
- Validação do arquivo.
- Mensagens de status mais claras.
- Permite escolher o arquivo MP3.
"""

import pygame
import os
pygame.init()
while True:
    arquivo = input('Digite o nome do arquivo MP3 (ou "fim" para encerrar): ').strip()
    if arquivo.lower() == 'fim':
        print('Encerrando programa.')
        break
    if not os.path.isfile(arquivo):
        print('Arquivo não encontrado!')
        continue
    try:
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()
        print(f'Reproduzindo {arquivo}...')
        pygame.event.wait()
    except Exception as e:
        print(f'Erro ao tentar reproduzir: {e}')
