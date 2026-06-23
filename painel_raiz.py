
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração da página e identidade visual
st.set_page_config(page_title="Índice RAIZ - Auditoria Institucional", page_icon="📊", layout="wide")

st.title("Painel de Auditoria: Índice RAIZ")
st.subheader("Desnudando o Banzo Institucional através da Ciência de Dados")
st.markdown("Este painel materializa as proposições analíticas que exigem que a máquina pública quantifique de forma transparente o seu impacto direto sobre os corpos e territórios marginalizados.")
st.divider()

# Barra lateral de controle e parametrização
st.sidebar.header("Parâmetros de Auditoria")
ano_selecionado = st.sidebar.selectbox("Recorte Temporal (Ano)", [2023, 2024, 2025, 2026])
territorio_selecionado = st.sidebar.multiselect("Demarcações Territoriais", ["Norte", "Sul", "Leste", "Oeste", "Centro"], default=["Norte", "Sul"])

# Renderização do ambiente gráfico
st.write("### Distribuição Quantitativa dos Impactos Institucionais")
fig = go.Figure()
fig.add_trace(go.Bar(x=territorio_selecionado, y=[0] * len(territorio_selecionado), marker_color='#8B0000'))
fig.update_layout(title=f"Mapeamento de Indicadores - Ano Base: {ano_selecionado}", template="plotly_white")

st.plotly_chart(fig, use_container_width=True)
