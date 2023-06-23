import streamlit as st

def calcular_probabilidades(odd_casa, odd_empate, odd_visitante):
    prob_odd_casa = 1 / odd_casa
    prob_odd_empate = 1 / odd_empate
    prob_odd_visitante = 1 / odd_visitante
    total_prob = prob_odd_casa + prob_odd_empate + prob_odd_visitante

    prob_justa_odd_casa = prob_odd_casa / total_prob * 100
    prob_justa_odd_empate = prob_odd_empate / total_prob * 100
    prob_justa_odd_visitante = prob_odd_visitante / total_prob * 100

    odds_justa_odd_casa = 100 / prob_justa_odd_casa
    odds_justa_odd_empate = 100 / prob_justa_odd_empate
    odds_justa_odd_visitante = 100 / prob_justa_odd_visitante

    return prob_justa_odd_casa, prob_justa_odd_empate, prob_justa_odd_visitante

# Interface do Streamlit
st.title("Calculadora de Probabilidade Real")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

if st.button("Calcular"):
    prob_casa, prob_empate, prob_visitante = calcular_probabilidades(odd_casa, odd_empate, odd_visitante)

    st.write("Probabilidade Real Casa: {:.2f}%".format(prob_casa))
    st.write("Probabilidade Real Empate: {:.2f}%".format(prob_empate))
    st.write("Probabilidade Real Visitante: {:.2f}%".format(prob_visitante))
