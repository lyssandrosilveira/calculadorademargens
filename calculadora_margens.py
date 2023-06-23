import streamlit as st

def calcular_margem(odd_casa, odd_empate, odd_visitante):
    possibilidade_casa = 1 / odd_casa
    possibilidade_empate = 1 / odd_empate
    possibilidade_visitante = 1 / odd_visitante
    margem = (possibilidade_casa + possibilidade_empate + possibilidade_visitante - 1) * 100
    return margem

def calcular_comissao(odd_casa, odd_empate, odd_visitante):
    possibilidade_casa = 1 / odd_casa
    possibilidade_empate = 1 / odd_empate
    possibilidade_visitante = 1 / odd_visitante
    comissao_casa = (1 / possibilidade_casa - 1) * 100
    comissao_empate = (1 / possibilidade_empate - 1) * 100
    comissao_visitante = (1 / possibilidade_visitante - 1) * 100
    return comissao_casa, comissao_empate, comissao_visitante

# Interface do Streamlit
st.title("Calculadora de Margens")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

if st.button("Calcular"):
    margem = calcular_margem(odd_casa, odd_empate, odd_visitante)
    comissao_casa, comissao_empate, comissao_visitante = calcular_comissao(odd_casa, odd_empate, odd_visitante)

    st.write("Margem: {:.2f}%".format(margem))
    st.write("Comissão para Casa: {:.2f}%".format(comissao_casa))
    st.write("Comissão para Empate: {:.2f}%".format(comissao_empate))
    st.write("Comissão para Visitante: {:.2f}%".format(comissao_visitante))

