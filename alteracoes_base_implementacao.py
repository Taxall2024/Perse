from alteracoes_base import AlteracoesBase
import pandas as pd

class ImplementandoAlteracoesBase(AlteracoesBase):
    def dados_willian(self):
        self.df.loc[self.df[0] == '0000', 1] = '006'
        self.df.loc[self.df[0] == '0000', 2] = '1'

        self.df.loc[self.df[0] == '0100', 1] = 'WILLIAM SILVA DE ALMEIDA'
        self.df.loc[self.df[0] == '0100', 2] = '89709861115'
        self.df.loc[self.df[0] == '0100', 3] = '19342DF'
        self.df.loc[self.df[0] == '0100', 6] = 'Q CRS 502 BLOCO B'
        self.df.loc[self.df[0] == '0100', 5] = '70330520'
        self.df.loc[self.df[0] == '0100', 9] = 'ASA SUL'
        self.df.loc[self.df[0] == '0100', 10] = '6181272930'
        self.df.loc[self.df[0] == '0100', 12] = 'NEGOCIOS@TAXALL.COM.BR'
        self.df.loc[self.df[0] == '0100', 13] = '5300108'

    def calculando_contadores_de_linhas(self):

        #Atualizar a contagem de '9900' após possíveis remoções
        contagem_99_00 = self.df[self.df[0] == '9900'].shape[0]

        #Encontrar os índices das linhas '9001' e '9999'
        start_index = self.df.index[self.df[0].str.startswith('9001')].min()
        end_index = self.df.index[self.df[0].str.startswith('9999')].max()

        # Criar um subconjunto do DataFrame entre '9001' e '9999'
        subset_df = self.df.loc[start_index:end_index]

        # Contar o número de linhas no subset
        contagem_linhas_99_90 = len(subset_df)

        # Calcular total de linhas, **excluindo '9999'**
        contagem_total_linhas = len(self.df[self.df[0] != '9999'])

        # Atualizar a linha '9999' com o total **sem contar ele mesmo**
        self.df.loc[self.df[0] == '9999', 1] = contagem_total_linhas

        #Atualizar a linha '9900' com a contagem correta (evitando erro se `9900` não existir)
        if contagem_99_00 > 0:
            self.df.loc[(self.df[0] == '9900') & (self.df[1] == '9900'), 2] = contagem_99_00

        # Atualizar a linha '9990' com a contagem de registros entre '9001' e '9999'
        self.df.loc[self.df[0] == '9990', 1] = contagem_linhas_99_90

        # Contar quantas linhas começam com 'M' (excluindo M210 e M610)
        contador_M = self.df[(self.df[0].str.startswith('M')) & (~self.df[0].isin(['M210', 'M610']))].shape[0]

        #Contar quantas linhas começam com 'F'
        contador_F = self.df[self.df[0].str.startswith('F')].shape[0]

        #Exibir logs no console para depuração
        print('---------- LOG Contador de linhas para Rubrica M => ', contador_M)
        print('---------- LOG Contador de linhas para Rubrica F => ', contador_F)

        #Atualizar contagem em 'M990' e 'F990'
        self.df.loc[self.df[0] == 'M990', 1] = contador_M
        self.df.loc[self.df[0] == 'F990', 1] = contador_F

        #Remover registros '9900' específicos de 'M210' e 'M610'
        for rubrica in ['M210', 'M610']:
            self.df = self.df[~((self.df[0] == '9900') & (self.df[1] == rubrica))]

        #Recalcular a contagem de '9900' depois das remoções
        contagem_99_00_atualizada = self.df[self.df[0] == '9900'].shape[0]

        #Atualizar a contagem correta de '9900'
        if contagem_99_00_atualizada > 0:
            self.df.loc[(self.df[0] == '9900') & (self.df[1] == '9900'), 2] = contagem_99_00_atualizada

        # Remover qualquer linha completamente vazia
        self.df.dropna(how='all', inplace=True)

