import streamlit as st
import app as app

st.set_page_config(page_title='/account')
with st.container():
    st.sidebar.title('Menu')
    st.sidebar.write('---')
    st.sidebar.subheader('Download App')
    st.sidebar.subheader('Sobre')
    st.sidebar.subheader('Ajuda')
    st.sidebar.subheader('Política da Empresa')
    st.sidebar.write('---')
    st.sidebar.selectbox('Idioma',['Português','Espanhol','Italiano','Japonês','Inglês','Francês'])

with st.container():
    st.title('MY :violet[Business]')
    st.write('MY Business é o site para você que gostaria de administrar a sua empresa ou StartUp! Vamos Começar!')
    acesso = st.selectbox('Login/Cadastro', ['Login','Cadastro'])

    if acesso == 'Login':
        email = st.text_input('Endereço de Email')
        st.write('---')
        senha = st.text_input('Senha', type = 'password')
        st.write('[Esqueceu a senha?](https://support.google.com/accounts/answer/7682439?hl=pt-BR)')
        st.link_button('Acessar', 'app.py')

    else:
        email = st.text_input('Endereço de Email')
        st.write('---')
        senha = st.text_input('Senha', type='password')
        conf_senha = st.text_input('Confirme a Senha', type='password')
        st.write('---')
        username = st.text_input('Username')
        st.link_button('Criar Conta','app.py')



