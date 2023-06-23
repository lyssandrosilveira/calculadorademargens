import streamlit as st

def calcular_odd_justa(odd, margem):
    odd_justa = odd / (1 + margem/100)
    return round(odd_justa, 2)

# Interface do Streamlit
st.title("Calculadora de Odds Justas")

odd_casa = st.number_input("Odd Casa")
odd_empate = st.number_input("Odd Empate")
odd_visitante = st.number_input("Odd Visitante")

margem = st.slider("Margem da Casa de Apostas (%)", min_value=0.0, max_value=100.0, step=0.01)

if st.button("Calcular"):
    odd_justa_casa = calcular_odd_justa(odd_casa, margem)
    odd_justa_empate = calcular_odd_justa(odd_empate, margem)
    odd_justa_visitante = calcular_odd_justa(odd_visitante, margem)

    # Verificar se a soma dos resultados é maior que 100%
    soma_odds_justas = odd_justa_casa + odd_justa_empate + odd_justa_visitante
    if soma_odds_justas > 100.0:
        st.warning("A soma das odds justas é maior que 100%. Ajuste as odds ou a margem.")

    st.write("Odd Justa Casa: {:.2f}".format(odd_justa_casa))
    st.write("Odd Justa Empate: {:.2f}".format(odd_justa_empate))
    st.write("Odd Justa Visitante: {:.2f}".format(odd_justa_visitante))

