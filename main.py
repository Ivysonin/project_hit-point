# Importando
from funções.classe_cadastrar import Cadastrar

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# Salvando os Funcionários
funcionarios = []

# =========================== Iniciando programa ===========================
print(f'{cor_ciano}----- Bem-vindo ao sistema de controle de ponto! -----\n{reset_cor}') # Organização

while True:
    # Para salvar informações como: nome, entrada e saida de horas
    nome = input(f'{cor_verde}Nome do Funcionário: {reset_cor}')
    entradas = []
    saidas = []

    while True: 
        entradas.append(input(f'{cor_verde}Horario de entrada no formato ( HH:MM:SS ): {reset_cor}'))
        saidas.append(input(f'{cor_verde}Horario de saida no formato ( HH:MM:SS ): {reset_cor}'))
        escolha_continuar = input(f'\n{cor_vermelho}Deseja cadastrar mais horas (s/n): {reset_cor}').lower()
        if escolha_continuar == 'n':
            break

    # Fazendo uma cópia do que tem dentro das listas, e limpando elas para que um novo possível funcionário se cadastre
    funcionarios.append(Cadastrar(nome, entradas.copy(), saidas.copy()))
    entradas.clear() # Limpando
    saidas.clear() # Limpando
    escolha_continuar = input(f'{cor_vermelho}Deseja cadastrar mais um funcionário? (s/n): {reset_cor}').lower()
    if escolha_continuar == 'n' :
        break

for i in range(len(funcionarios)):
    # Consigo usar as funções da classe pq dentro da lista 'funcionarios' eu tenho objetos
    funcionarios[i].calcular_horas()
    funcionarios[i].informacoes()

print('====================================================================================================')
print(f'{cor_ciano} {"Saindo do sistema de controle de ponto" :^100} {reset_cor}')
print('====================================================================================================')