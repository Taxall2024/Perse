import pandas as pd
import numpy as np

class AlteracoesRegistros():
    
    def __init__(self, df):
        self.df = df
        
    def alterar_F500(self):
        self.df.loc[self.df[0] == 'F500', 2] = '06'
        self.df.loc[self.df[0] == 'F500', 7] = '06'
    
    def alterar_F525(self):
        self.df.loc[self.df[0] == 'F525', 7] = '06'
        self.df.loc[self.df[0] == 'F525', 8] = '06'
    
    def alterar_F550(self):
        self.df.loc[self.df[0] == 'F550', 2] = '06'
        self.df.loc[self.df[0] == 'F550', 3] = '0'
        self.df.loc[self.df[0] == 'F550', 5] = '0'
        self.df.loc[self.df[0] == 'F550', 6] = '0'
        self.df.loc[self.df[0] == 'F550', 7] = '06'
        self.df.loc[self.df[0] == 'F550', 8] = '0'
        self.df.loc[self.df[0] == 'F550', 10] = '0'
        self.df.loc[self.df[0] == 'F550', 11] = '0'
    
    def zerar_M200(self):
        self.df.loc[self.df[0] == 'M200', 1:12] = '0'

    def zerar_M600(self):
        self.df.loc[self.df[0] == 'M600', 1:12] = '0'
    
    def excluir_M210(self):
        self.df = self.df[self.df[0] != 'M210']
        self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == 'M210'))]

    def excluir_M205(self):
        self.df = self.df[self.df[0] != 'M205']
        self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == 'M205'))]
    
    def excluir_M610(self):
        self.df = self.df[self.df[0] != 'M610']
        self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == 'M610'))] 
    
    def excluir_M605(self):
        self.df = self.df[self.df[0] != 'M605']
        self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == 'M605'))]

    # Arquivo não consolidados
    def alterar_A170(self):
        mask = self.df[0] == 'A100'
        coluna_4 = self.df.loc[mask, 4]
        # Verifica se alguma dessas linhas tem o valor '02' na coluna 4
        if  (coluna_4 == '00').any():    
            colunas = [10,11, 14, 15]
            self.df.loc[self.df[0] == 'A170', colunas] = '0'
            self.df.loc[self.df[0] == 'A170', [8, 12 ]] = '06'
        
        elif (coluna_4 == '02').any() and (coluna_4 == '04').any() : 
            for i in range(len(self.df) - 1):
                if ((self.df.iloc[i, 0] == 'A100') & (self.df.iloc[i, 2] == '0')) and self.df.iloc[i + 1, 0] == 'A170':
                    self.df.iloc[i + 1, 1] = ''
                    self.df.iloc[i + 1, 2] = ''
                    self.df.iloc[i + 1, 3] = ''
                    self.df.iloc[i + 1, 4] = ''
                    self.df.iloc[i + 1, 5] = ''
                    self.df.iloc[i + 1, 6] = ''
                    self.df.iloc[i + 1, 7] = ''
                    self.df.iloc[i + 1, 8] = ''
                    self.df.iloc[i + 1, 9] = ''
                    self.df.iloc[i + 1, 10] = ''
                    self.df.iloc[i + 1, 11] = ''
                    self.df.iloc[i + 1, 12] = ''
                    self.df.iloc[i + 1, 13] = ''
                    self.df.iloc[i + 1, 14] = ''
                    self.df.iloc[i + 1, 15] = ''
                    self.df.iloc[i + 1, 16] = ''
                    self.df.iloc[i + 1, 17] = ''


            for j in range(1, 51):
                if i + j < len(self.df) and self.df.iloc[i + j, 0] == 'A170':
                    self.df.iloc[i + j, 33] = '' 
                    self.df.iloc[i + j, 26] = '' 
                    self.df.iloc[i + j, 32] = '' 

        
    
    def alterar_C170(self):
        mask = self.df[0] == 'C100'
        coluna_5 = self.df.loc[mask, 5]
        # Verifica se alguma dessas linhas tem o valor '02' na coluna 4
        if  (coluna_5 == '00').any(): 
            colunas = [15, 26, 29, 32, 35]
            self.df.loc[self.df[0] == 'C170', colunas] = '0'
            self.df.loc[self.df[0] == 'C170', [12, 24, 30]] = '06'
        elif ((coluna_5 == '02').any() and (coluna_5 == '04').any()): 
            for i in range(len(self.df) - 1):
                if ((self.df.iloc[i, 0] == 'C100') & (self.df.iloc[i, 2] == '0')) and self.df.iloc[i + 1, 0] == 'C170':
                    self.df.iloc[i + 1, 1] = ''
                    self.df.iloc[i + 1, 2] = ''
                    self.df.iloc[i + 1, 3] = ''
                    self.df.iloc[i + 1, 4] = ''
                    self.df.iloc[i + 1, 5] = ''
                    self.df.iloc[i + 1, 6] = ''
                    self.df.iloc[i + 1, 7] = ''
                    self.df.iloc[i + 1, 8] = ''
                    self.df.iloc[i + 1, 9] = ''
                    self.df.iloc[i + 1, 10] = ''
                    self.df.iloc[i + 1, 11] = ''
                    self.df.iloc[i + 1, 12] = ''
                    self.df.iloc[i + 1, 13] = ''
                    self.df.iloc[i + 1, 14] = ''
                    self.df.iloc[i + 1, 15] = ''
                    self.df.iloc[i + 1, 16] = ''
                    self.df.iloc[i + 1, 17] = ''
                    self.df.iloc[i + 1, 18] = ''
                    self.df.iloc[i + 1, 19] = ''
                    self.df.iloc[i + 1, 20] = ''
                    self.df.iloc[i + 1, 21] = ''
                    self.df.iloc[i + 1, 22] = ''
                    self.df.iloc[i + 1, 23] = ''
                    self.df.iloc[i + 1, 24] = ''
                    self.df.iloc[i + 1, 25] = ''
                    self.df.iloc[i + 1, 26] = ''
                    self.df.iloc[i + 1, 27] = ''
                    self.df.iloc[i + 1, 28] = ''
                    self.df.iloc[i + 1, 29] = ''
                    self.df.iloc[i + 1, 30] = ''
                    self.df.iloc[i + 1, 31] = ''
                    self.df.iloc[i + 1, 32] = ''
                    self.df.iloc[i + 1, 33] = ''
        

            for j in range(1, 51):
                if i + j < len(self.df) and self.df.iloc[i + j, 0] == 'C170':
                    self.df.iloc[i + j, 33] = '' 
                    self.df.iloc[i + j, 26] = '' 
                    self.df.iloc[i + j, 32] = '' 
    


    def alterar_A100(self):
        mask = self.df[0] == 'A100'
        coluna_4 = self.df.loc[mask, 4]
        
        # Verifica se alguma dessas linhas tem o valor '02' na coluna 4
        if (coluna_4 == '02').any() and (coluna_4 == '04').any():    
            # Define as colunas que serão alteradas (colunas 8 a 20)
            colunas = list(range(8, 20)) 
            
            # Atribui valores vazios às colunas especificadas para as linhas onde a coluna 4 é '02'
            self.df.loc[mask & (coluna_4 == '02'), colunas] = '' # ou usar '' para strings vazias
        
        # Verifica se alguma dessas linhas tem o valor '00' na coluna 4
        if (coluna_4 == '00').any():
            # Altera apenas as colunas 15 e 17 para '0,0' nas linhas onde a coluna 4 é '00'
            self.df.loc[mask & (coluna_4 == '00'), [15, 17]] = '0'

    def alterar_C100(self):
        mask = self.df[0] == 'C100'
        coluna_5 = self.df.loc[mask, 5]
        if ((coluna_5 == '02').any() and (coluna_5 == '04').any()): 
            # Define as colunas que serão alteradas
            colunas = list(range(8, 28)) 
            # Atribui valores vazios às colunas especificadas para as linhas onde a coluna 0 é 'A100'
            self.df.loc[mask, colunas] = ''
        elif (coluna_5 == '00').any():
            self.df.loc[mask & (coluna_5 == '00'), [25, 26]] = '0'


    def adicionar_registros_M(self):
        """
        Adiciona os registros M400, M410, M800 e M810 dentro do bloco de registros M
        respeitando a ordem numérica correta e atualiza o contador 9900.
        """
        
        registros_para_remover = ['M400', 'M410', 'M800', 'M810']
        self.df = self.df[~self.df[0].isin(registros_para_remover)]

        self.df.reset_index(drop=True, inplace=True)

        def calcular_valor_registrosM(self):
            # Verifica se há registros 'F550' (caso consolidado)
            if 'F550' in self.df[0].values:
                # Caso consolidado: pega o valor da coluna 1 do primeiro registro 'F550'
                valor_F550 = self.df.loc[self.df[0] == 'F550', 1]
                # Converte a string para número, substituindo vírgula por ponto
                valor_F550 = valor_F550.replace(",", ".", regex=True)
                valor_registrosM = pd.to_numeric(valor_F550, errors='coerce').sum()  # Converte para número e soma
                valor_registrosM = float(valor_registrosM) if not pd.isna(valor_registrosM) else '0'
            else:
                # Caso não consolidado: soma os valores das colunas 4 (para 'A170') e 6 (para 'C170')
                valores_A170 = self.df.loc[self.df[0] == 'A170', 4]  # Valores da coluna 4 onde a coluna 0 é 'A170'
                valores_C170 = self.df.loc[self.df[0] == 'C170', 6]  # Valores da coluna 6 onde a coluna 0 é 'C170'

                # Converte as strings para números, substituindo vírgula por ponto
                valores_A170 = valores_A170.replace(",", ".", regex=True)
                valores_C170 = valores_C170.replace(",", ".", regex=True)

                # Converte para números e soma
                soma_A170 = pd.to_numeric(valores_A170, errors='coerce').sum()  # Converte para número e soma
                soma_C170 = pd.to_numeric(valores_C170, errors='coerce').sum()  # Converte para número e soma
                soma_total = soma_A170 + soma_C170  # Soma total

                # Atribui a soma à variável valor_registrosM
                valor_registrosM = soma_total if not pd.isna(soma_total) else '0'

            # Formata o valor com vírgula como separador decimal e sem separador de milhares
            valor_formatado = "{:.2f}".format(valor_registrosM).replace(".", ",")

            # Retorna o valor formatado
            return valor_formatado

        # Calcula o valor de valor_registrosM
        valor_registrosM = calcular_valor_registrosM(self)

        def alterar_codigo_escrituracao(self):
            # Verifica se a coluna 4 da linha onde a coluna 0 é '0500' tem o valor '411'
            if self.df.loc[self.df[0] == '0500', 5].item() == '411':
                codigo_escrituracao = '411'
                print(codigo_escrituracao)
            else:
                codigo_escrituracao = self.df.loc[self.df[0] == '0500', 5].item()
                print(codigo_escrituracao)
            return codigo_escrituracao

        def alterar_nome_escrituracao(self):
            if self.df.loc[self.df[0] == '0500', 6].item() == 'RECEITA DO PERSE':
                nome_escrituracao = 'RECEITA DO PERSE'
                print(nome_escrituracao)
            else:
                nome_escrituracao = self.df.loc[self.df[0] == '0500', 6].item()
                #nome_escrituracao = 'RECEITA DO PERSE'
                print(nome_escrituracao)
            
            return nome_escrituracao
        
        codigo_escrituracao = alterar_codigo_escrituracao(self)
        #print(codigo_escrituracao)
        nome_escrituracao = alterar_nome_escrituracao(self)
        #print(nome_escrituracao)
        # Define os registros a serem adicionados
        registros = [
            ["M400", "06", valor_registrosM, codigo_escrituracao, nome_escrituracao],
            ["M410", "920", valor_registrosM, codigo_escrituracao, nome_escrituracao],
            ["M800", "06", valor_registrosM, codigo_escrituracao, nome_escrituracao],
            ["M810", "920", valor_registrosM, codigo_escrituracao, nome_escrituracao]
        ]

        # Verificar o número total de colunas do DataFrame
        num_colunas = self.df.shape[1]

        # Encontrar a posição correta para inserir os registros dentro do bloco M
        indices_m = self.df.index[self.df[0].str.startswith('M')]

        if not indices_m.empty:
            # Criar uma lista de registros M existentes para determinar a posição correta
            registros_m_existentes = self.df.loc[indices_m, 0].tolist()

            # Ordenar os registros M existentes com base no valor numérico após o "M"
            registros_m_existentes.sort(key=lambda x: int(x[1:]))

            # Inserir os novos registros na ordem correta
            for registro in registros:
                if not (self.df[0] == registro[0]).any():
                    # Criar uma nova linha preenchendo as colunas restantes com ''
                    nova_linha = registro + [''] * (num_colunas - len(registro))

                    # Encontrar a posição correta para inserir o novo registro
                    posicao_insercao = None
                    for i, reg_existente in enumerate(registros_m_existentes):
                        if int(registro[0][1:]) < int(reg_existente[1:]):
                            # Encontrar o índice correspondente no DataFrame
                            posicao_insercao = self.df.index[self.df[0] == reg_existente].tolist()[0]
                            break

                    # Se não encontrou uma posição, insere no final do bloco M
                    if posicao_insercao is None:
                        posicao_insercao = indices_m[-1] + 1

                    # Garantir que a posição de inserção não ultrapasse o tamanho do DataFrame
                    posicao_insercao = min(posicao_insercao, len(self.df))

                    # Adicionar a nova linha na posição correta
                    self.df = pd.concat([
                        self.df.iloc[:posicao_insercao],  # Parte antes da posição correta
                        pd.DataFrame([nova_linha], columns=self.df.columns),  # Nova linha
                        self.df.iloc[posicao_insercao:]  # Parte após a inserção
                    ], ignore_index=True)

                    # Atualizar a lista de registros M existentes
                    registros_m_existentes.append(registro[0])
                    registros_m_existentes.sort(key=lambda x: int(x[1:]))
        else:
            # Se não houver registros M, adicionar todos os novos registros no começo
            for registro in registros:
                nova_linha = registro + [''] * (num_colunas - len(registro))
                self.df = pd.concat([
                    pd.DataFrame([nova_linha], columns=self.df.columns),
                    self.df
                ], ignore_index=True)

        # Atualizar o contador 9900
        self.atualizar_contador_9900()

    def atualizar_contador_9900(self):

        #self.df.reset_index(drop=True, inplace=True)
        # Contar os registros M400, M410, M800, M810
        m400 = self.df.loc[self.df[0].str.startswith('M400', na=False), 0].shape[0]
        m410 = self.df.loc[self.df[0].str.startswith('M410', na=False), 0].shape[0]
        m800 = self.df.loc[self.df[0].str.startswith('M800', na=False), 0].shape[0]
        m810 = self.df.loc[self.df[0].str.startswith('M810', na=False), 0].shape[0]

        print('--------> LOG --------> Contador 400 :', m400)
        print('--------> LOG --------> Contador 410 :', m410)
        print('--------> LOG --------> Contador 800 :', m800)
        print('--------> LOG --------> Contador 810 :', m810)

        # Lista de registros |M| que serão adicionados como |9900|Mxxx|quantidade|
        registros_m = ['M400', 'M410', 'M800', 'M810']
        quantidades = [m400, m410, m800, m810]

        # Criar os novos registros |9900|Mxxx|quantidade| como 3 colunas
        novos_registros_9900 = [
            ['9900', registro, str(quantidade)] for registro, quantidade in zip(registros_m, quantidades)
        ]

        # Encontrar os índices dos registros |9900| existentes
        self.df.reset_index(drop=True, inplace=True)
        indices_9900 = self.df.index[self.df[0].str.startswith('9900', na=False)].tolist()

        # Inserir os novos registros |9900|Mxxx|quantidade| na ordem correta
        for novo_registro in novos_registros_9900:
            # Extrair o código M do novo registro (ex: M400, M410, etc.)
            codigo_m = novo_registro[1]

            # Encontrar a posição correta para inserir o novo registro
            posicao_insercao = None
            for i, idx in enumerate(indices_9900):
                # Extrair o código M do registro |9900| existente
                codigo_existente = self.df.iloc[idx, 1]  # Segunda coluna (Mxxx)
                if codigo_m < codigo_existente:
                    posicao_insercao = idx
                    break

            # Se não encontrou uma posição, insere no final do bloco |9900|
            if posicao_insercao is None:
                posicao_insercao = indices_9900[-1] + 1 if indices_9900 else len(self.df)

            # Criar uma nova linha com apenas 3 colunas
            nova_linha = novo_registro

            # Criar um DataFrame temporário com as 3 colunas
            df_temp = pd.DataFrame([nova_linha], columns=self.df.columns[:3])

            # Inserir o novo registro na posição correta
            self.df = pd.concat([
                self.df.iloc[:posicao_insercao],  # Parte antes da posição correta
                df_temp,  # Nova linha com 3 colunas
                self.df.iloc[posicao_insercao:]  # Parte após a inserção
            ], ignore_index=True)

            # Atualizar a lista de índices dos registros |9900|
            #indices_9900 = self.df.index[self.df[0].str.startswith('9900', na=False)].tolist()
            self.df.reset_index(drop=True, inplace=True)
