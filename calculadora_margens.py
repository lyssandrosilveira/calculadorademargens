import streamlit as st

def calcular_probabilidades(odd_casa, odd_empate, odd_visitante):
    total_odds = odd_casa + odd_empate + odd_visitante

    prob_odd_casa = odd_casa / total_odds * 100
    prob_odd_empate = odd_empate / total_odds * 100
    prob_odd_visitante = odd_visitante / total_odds * 100

    juice = 100 - (prob_odd_casa + prob_odd_empate + prob_odd_visitante)

    return prob_odd_casa, prob_odd_empate, prob_odd_visitante, juice

# Interface do Streamlit
st.title("Qual a Probabilidade Real?")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

if st.button("Calcular"):
    prob_casa, prob_empate, prob_visitante, juice = calcular_probabilidades(odd_casa, odd_empate, odd_visitante)

    st.write("Probabilidade Real Casa: {:.2f}%".format(prob_casa))
    st.write("Probabilidade Real Empate: {:.2f}%".format(prob_empate))
    st.write("Probabilidade Real Visitante: {:.2f}%".format(prob_visitante))
    st.write("Juice da Casa de Apostas: {:.2f}%".format(juice))
