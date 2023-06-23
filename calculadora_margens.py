import streamlit as st

def calcular_probabilidade_real(odd):
    probabilidade_real = 1 / odd * 100
    return round(probabilidade_real, 2)

# Interface do Streamlit
st.title("Calculadora de Probabilidade Real")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

if st.button("Calcular"):
    # Calcular a margem da casa de apostas (juice)
    margem = 1 / odd_casa + 1 / odd_empate + 1 / odd_visitante - 1

    # Verificar se a soma dos resultados é maior que 100%
    if margem > 1:
        st.warning("A soma das odds é maior que 100%. Ajuste as odds.")

    # Calcular as probabilidades reais
    probabilidade_real_casa = calcular_probabilidade_real(odd_casa / (1 + margem))
    probabilidade_real_empate = calcular_probabilidade_real(odd_empate / (1 + margem))
    probabilidade_real_visitante = calcular_probabilidade_real(odd_visitante / (1 + margem))

    st.write("Juice (Margem da Casa de Apostas): {:.2f}%".format(margem * 100))
    st.write("Probabilidade Real Casa: {:.2f}%".format(probabilidade_real_casa))
    st.write("Probabilidade Real Empate: {:.2f}%".format(probabilidade_real_empate))
    st.write("Probabilidade Real Visitante: {:.2f}%".format(probabilidade_real_visitante))

