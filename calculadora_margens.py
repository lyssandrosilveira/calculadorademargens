import streamlit as st

def calcular_probabilidade(odd):
    return round(1 / odd * 100, 2)

# Interface do Streamlit
st.title("Calculadora de Probabilidade Real")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

if st.button("Calcular"):
    # Calcular as probabilidades a partir das odds informadas
    probabilidade_casa = calcular_probabilidade(odd_casa)
    probabilidade_empate = calcular_probabilidade(odd_empate)
    probabilidade_visitante = calcular_probabilidade(odd_visitante)

    # Calcular o juice (margem da casa de apostas)
    juice = 100 - (probabilidade_casa + probabilidade_empate + probabilidade_visitante)

    # Verificar se a soma das probabilidades é maior que 100%
    if juice < 0:
        st.warning("A soma das probabilidades é maior que 100%. Ajuste as odds.")

    # Calcular as probabilidades reais extraindo o juice
    probabilidade_real_casa = probabilidade_casa - (probabilidade_casa * juice / 100)
    probabilidade_real_empate = probabilidade_empate - (probabilidade_empate * juice / 100)
    probabilidade_real_visitante = probabilidade_visitante - (probabilidade_visitante * juice / 100)

    st.write("Probabilidade Casa: {:.2f}%".format(probabilidade_casa))
    st.write("Probabilidade Empate: {:.2f}%".format(probabilidade_empate))
    st.write("Probabilidade Visitante: {:.2f}%".format(probabilidade_visitante))
    st.write("Juice (Margem da Casa de Apostas): {:.2f}%".format(juice))
    st.write("Probabilidade Real Casa: {:.2f}%".format(probabilidade_real_casa))
    st.write("Probabilidade Real Empate: {:.2f}%".format(probabilidade_real_empate))
    st.write("Probabilidade Real Visitante: {:.2f}%".format(probabilidade_real_visitante))


