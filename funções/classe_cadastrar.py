class Cadastrar:
    def __init__(self, nome, entrada, saida):
        self.nome = nome
        self.entrada = entrada
        self.saida = saida
        self.horas_totais = []

    def calcular_horas(self):
        for i in range(len(self.entrada)): # uso o 'self.entrada' pq necessariamente precisa da entrada de horas
            Entrada = self.entrada[i].split(':') # Divide todos os valores de 'entrada' a partir do ':'
            entrada_em_segundos = (int(Entrada[0]) * 3600) + int(Entrada[1]) * 60 + int(Entrada[2]) # Mudando o valor das 'Entradas' para 'int' e transformando em segundos

            Saida = self.saida[i].split(':')
            saida_em_segundo = (int(Saida[0]) * 3600) + int(Saida[1]) * 60 + int(Saida[2])

            tempo_total = saida_em_segundo - entrada_em_segundos # Pegando a diferença entre a saida e a entrada

            # Transformando de Segundos para Horas 
            horas    = tempo_total // 3600 % 24
            minutos  = tempo_total % 3600 // 60
            segundos = tempo_total % 3600 % 60

            # Formatando para o formato XX:XX:XX
            self.horas_totais.append(f'{horas}:{minutos}:{segundos}')

    def informacoes(self):
        print('====================================================================================================')
        print(f'FUNCIONÁRIO(A): {self.nome}')
        print('====================================================================================================')
        print(f'{"ÍNICIO":^20}{"SAÌDA":^20}{"TOTAL":^20}') # Usando :^20 para dar espaços entre eles

        for i in range(len(self.entrada)): # Uso o 'self.entrada' pq necessariamente precisa da entrada de horas
            # Usando 'i' para verificar todos os itens que estiver dentro das listas
            print(f'{self.entrada[i] :^20}{self.saida[i] :^20}{self.horas_totais[i] :^20}') # Usando :^20 para dar espaços entre eles (a mesma quantida que os nomes acima (ÍNICIO / SAÌDA / TOTAL) para ficar alinhado)