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
    
    def zerar_M605(self):
        self.df.loc[self.df[0] == 'M600', 1:12] = '0'

    def alterar_M400(self):
        self.df.loc[self.df[0] == 'M400', 1] = '06'
    
    def alterar_M800(self):
        self.df.loc[self.df[0] == 'M800', 1] = '06'
    
    def alterar_M410(self):
        self.df.loc[self.df[0] == 'M410', 1] = '920'
    
    def alterar_M810(self):
        self.df.loc[self.df[0] == 'M810', 1] = '920'
    
    def excluir_M210(self):
        self.df = self.df[self.df[0] != 'M210']

    def excluir_M205(self):
        self.df = self.df[self.df[0] != 'M205']
    
    def excluir_M610(self):
        self.df = self.df[self.df[0] != 'M610']
    
    def excluir_M605(self):
        self.df = self.df[self.df[0] != 'M605']

    # Arquivo não consolidados

    def alterar_A170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'A170', colunas] = '00'
        self.df.loc[self.df[0] == 'A170', [8, 12]] = '06'
    
    def alterar_C170(self):
        colunas = [10, 11, 14, 15]
        self.df.loc[self.df[0] == 'C170', colunas] = '00'
        self.df.loc[self.df[0] == 'C170', [8, 12]] = '06'
        
    def alterar_A100(self):
        colunas = [15, 17, 18, 19]
        self.df.loc[self.df[0] == 'A100', colunas] = '00'

    def alterar_C100(self):
        colunas = [15, 17, 18, 19]
        self.df.loc[self.df[0] == 'C100', colunas] = '00'
    

    def adicionar_registros_M(self):
        """
        Adiciona os registros M400, M410, M800 e M810 dentro do bloco de registros M
        respeitando a ordem numérica correta.
        """

        # Captura o valor do campo 1 do registro 'F550' (não deve ser uma série)
        valor_registrosM = self.df.loc[self.df[0] == 'F550', 1]
        valor_registrosM = valor_registrosM.iloc[0] if not valor_registrosM.empty else '0'

        # Estrutura padrão dos registros M
        registros = [
            ["M400", "06", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M410", "920", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M800", "06", valor_registrosM, "411", "RECEITA DO PERSE"],
            ["M810", "920", valor_registrosM, "411", "RECEITA DO PERSE"]
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
            
        # Agora adicionamos a contagem correta em 9900
        #self.atualizar_contador_9900()

    # def atualizar_contador_9900(self):
    #     """ Atualiza o contador de registros 9900 """

    #     # Contar quantas vezes cada tipo de registro aparece
    #     contagem_registros = self.df[0].value_counts().reset_index()
    #     contagem_registros.columns = ["Registro", "Quantidade"]

    #     # Remover registros existentes do tipo 9900
    #     self.df = self.df[self.df[0] != "9900"]

    #     # Criar novas linhas do tipo 9900 com os valores corretos
    #     novos_registros_9900 = [
    #         ["9900", registro, str(quantidade)] for registro, quantidade in contagem_registros.values
    #     ]

    #     # Adicionar os novos registros 9900 no local correto (antes de 9999)
    #     idx_9999 = self.df.index[self.df[0] == "9999"].min()

    #     self.df = pd.concat([
    #         self.df.iloc[:idx_9999],  # Parte antes de 9999
    #         pd.DataFrame(novos_registros_9900, columns=self.df.columns),  # Novos registros 9900
    #         self.df.iloc[idx_9999:]  # Parte depois de 9999
    #     ], ignore_index=True)

    #     print("✅ Contadores 9900 atualizados corretamente!")

