import pandas as pd
import streamlit as st
import os
import zipfile
from io import BytesIO

from alteracoes_base_implementacao import ImplementandoAlteracoesBase as ab
from alteracoes_registros import AlteracoesRegistros as ar

# Classe para processar SPED com múltiplos arquivos
class SpedProcessor(ab, ar):
    def __init__(self, file_path, file_content):
        self.file_path = file_path
        self.file_content = file_content
        self.df = None

    def LendoELimpandoDadosSped(self):
        data = []
        self.file_content.seek(0)  # Voltar ao início do arquivo para garantir a leitura

        # Lendo o conteúdo do arquivo diretamente da memória
        lines = self.file_content.read().decode('ISO-8859-1').splitlines()

        for linha in lines:
            linha = linha.strip()
            if linha.startswith('|'):
                valores = linha.split('|')[1:]  # Remove o primeiro '|'
                data.append(valores)

        # Criar um DataFrame
        self.df = pd.DataFrame(data)
        st.dataframe(self.df)

        # Aplicando transformações
        self.calculando_contadores_de_linhas()
        self.dados_willian()
        self.alterar_F500()
        self.alterar_F525()
        self.zerar_M200()  
        self.zerar_M600()
        self.alterar_M400()
        self.alterar_M800()
        self.excluir_M210()
        self.excluir_M610()
        self.alterar_M410()
        self.alterar_M810()
        self.alterar_A170()
        self.alterar_C170()
        self.alterar_A100()
        self.alterar_C100()
        self.adicionar_registros_M()

        return self.df

    def devolvendo_txt(self):
    # Função para formatar cada linha
        def formatar_linha(row):
            # Seleciona apenas as colunas preenchidas (não vazias)
            valores = row.dropna().tolist()

            # Verifica se o registro é um dos que devem ser truncados após a coluna 4
            if row[0] in ['M400', 'M410', 'M800', 'M810']:
                # Mantém apenas as colunas 0 a 4
                if len(valores) > 4:
                    valores = valores[:5]
                return '|' + '|'.join(map(str, valores)) + '|'
            else:
                # Para outros registros, mantém todas as colunas
                return '|' + '|'.join(map(str, valores)) 

        # Aplica a formatação a cada linha do DataFrame
        formatted_lines = self.df.apply(formatar_linha, axis=1)
        result = '\n'.join(formatted_lines)

        # Remover linhas após o registro |9999| na coluna 0
        result_lines = result.splitlines()
        filtered_lines = []
        for line in result_lines:
            filtered_lines.append(line)
            # Verifica se a linha começa com |9999| (coluna 0)
            if line.startswith('|9999|'):
                break

        result = '\n'.join(filtered_lines)
        return result

# Configuração do Streamlit
st.set_page_config(page_title="Alterar Blocos do arquivo .txt", layout="wide")
st.title("Alterações automáticas do arquivo .txt")

# Upload de múltiplos arquivos
uploaded_files = st.file_uploader("Carregue os arquivos .txt", type=["txt"], accept_multiple_files=True)

# Processamento dos arquivos
if uploaded_files:
    processed_files = {}

    for uploaded_file in uploaded_files:
        original_name = uploaded_file.name
        new_name = os.path.splitext(original_name)[0] + "_retificado.txt"  # Adiciona _retificado no nome
        file_name = uploaded_file.name
        processor = SpedProcessor(file_name, uploaded_file)
        df = processor.LendoELimpandoDadosSped()
        processed_txt = processor.devolvendo_txt()

        # Armazena o conteúdo do arquivo processado em um dicionário
        processed_files[file_name] = processed_txt

    # Criar o arquivo .zip com os arquivos processados
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for file_name, content in processed_files.items():
            zip_file.writestr(file_name, content)

    zip_buffer.seek(0)

    # Botão de download do arquivo ZIP
    st.download_button(
        label="Baixar Arquivos Processados (.zip)",
        data=zip_buffer,
        file_name="arquivos_processados.zip",
        mime="application/zip"
    )