import streamlit as st
import pandas as pd

st.set_page_config(page_title='/app')

with st.container() :
    st.sidebar.title('Menu')
    empresas = st.sidebar.selectbox('Selecione a Empresa',['Kazuya Sushi', 'Lucas StartUp'])
    if empresas == 'Kazuya Sushi':
        @st.cache_data
        def carregar_dados():
            tabela = pd.read_csv('resultados_restaurante.csv')
            return tabela

        with st.container():
             st.subheader('Controle Total do Seu Restaurante!')
             st.title('DashBoards de :red[Pratos Vendidos]')
             st.write('Informações dos Pratos Vendidos de seu Restaurante.')
             st.write('_Quer um Site Para Sua Empresa?_ [Clique Aqui!](https://github.com/Victor-Watanabe/):sunglasses:')

        with st.container():
            st.sidebar.write('---')
            st.sidebar.subheader('Cardápio')
            st.sidebar.subheader('Produtos')
            st.sidebar.subheader('Filiais')
            st.sidebar.subheader('Estoque')
            st.sidebar.subheader('Serviços')
            st.sidebar.subheader('Parcerias')
            st.sidebar.subheader('Mais Informações')
            st.sidebar.subheader('Configurações')
            st.sidebar.subheader('Controle Financeiro')
            st.sidebar.subheader('Contas')
            st.sidebar.subheader('Gerenciamento de Acesso')
            st.sidebar.subheader('Sair')

        with st.container():
            st.write('---')
            qntd_dias = st.selectbox('Selecione o Período', ['7 Dias', '15 Dias', '30 Dias'])
            num_dias = int(qntd_dias.replace('Dias', ''''''))
            dados = carregar_dados()
            dados = dados[-num_dias:]
            st.area_chart(dados, x='Data', y='Vendas')

    elif empresas == 'Lucas StartUp':
        @st.cache_data
        def carregar_dados():
            tabela = pd.read_csv('resultados_lucas.csv')
            return tabela

        with st.container():
             st.subheader('Controle Total da Sua StartUp!')
             st.title('DashBoards de :blue[Contratos Fechados]')
             st.write('Controle dos Contratos Fechados de Sua StartUp.')
             st.write('_Quer um Site Para Sua Empresa?_ [Clique Aqui!](https://github.com/Victor-Watanabe/):sunglasses:')

        with st.container():
            st.sidebar.write('---')
            st.sidebar.subheader('Contratos')
            st.sidebar.subheader('VideoAulas')
            st.sidebar.subheader('Cursos')
            st.sidebar.subheader('plataformas')
            st.sidebar.subheader('Colaboradores')
            st.sidebar.subheader('Parcerias')
            st.sidebar.subheader('Mais Informações')
            st.sidebar.subheader('Configurações')
            st.sidebar.subheader('Controle Financeiro')
            st.sidebar.subheader('Contas')
            st.sidebar.subheader('Gerenciamento de Acesso')
            st.sidebar.subheader('Sair')


        with st.container():
            st.write('---')
            qntd_dias = st.selectbox('Selecione o Período',['7 Dias','15 Dias','30 Dias'])
            num_dias = int(qntd_dias.replace('Dias',''''''))
            dados = carregar_dados()
            dados = dados[-num_dias:]
            st.area_chart(dados, x='Data', y='Contratos')



