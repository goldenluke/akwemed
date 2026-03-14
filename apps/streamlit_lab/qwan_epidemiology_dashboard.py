import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

from pysus.online_data.SIH import SIH
from scipy import signal
from scipy.stats import gaussian_kde

st.set_page_config(page_title="QWAN Epidemiological Panel", layout="wide")

st.title("🧠 QWAN Epidemiological Monitoring")

st.markdown("""
Painel de monitoramento epidemiológico baseado em **dinâmica de sistemas complexos**.
Detecta **instabilidade hospitalar e risco de surtos**.
""")

# Sidebar
st.sidebar.header("Parameters")

uf = st.sidebar.selectbox(
    "State",
    ["SP","RJ","MG","BA","TO","PR","AM"]
)

year = st.sidebar.slider(
    "Year",
    2015,
    2024,
    2023
)

cid = st.sidebar.text_input(
    "CID Chapter",
    "J"
)

window = st.sidebar.slider(
    "Rolling window",
    7,
    30,
    14
)

# =========================================================
# DATA LOADING
# =========================================================

@st.cache_data
def load_data():

    sih = SIH()
    sih.load()

    files = sih.get_files(
        group='RD',
        uf=uf,
        year=year
    )

    if not files:
        return pd.Series()

    df = sih.download(files[0]).to_dataframe()

    df = df[df['DIAG_PRINC'].str.startswith(cid)]

    df['DT_INTER'] = pd.to_datetime(df['DT_INTER'])

    ts = df.groupby('DT_INTER').size()

    return ts

# =========================================================
# QWAN METRICS
# =========================================================

def resilience_metric(ts):

    returns = np.diff(np.log(ts + 1e-6))

    vol = pd.Series(returns).rolling(window).std()

    ac1 = pd.Series(returns).rolling(window).apply(
        lambda x: pd.Series(x).autocorr(lag=1)
    )

    risk = (vol + ac1) / 2

    resilience = 1 - risk

    return resilience

# =========================================================
# RUN ANALYSIS
# =========================================================

if st.sidebar.button("Run QWAN Analysis"):

    ts = load_data()

    if ts.empty:

        st.warning("No data available.")

    else:

        res = resilience_metric(ts)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Hospitalizations")

            fig = px.line(
                ts,
                labels={'value':'Hospitalizations'}
            )

            st.plotly_chart(fig, use_container_width=True)

        with col2:

            st.subheader("Systemic Resilience")

            fig2 = px.line(res)

            st.plotly_chart(fig2, use_container_width=True)

        # =====================================================
        # INSTABILITY HEATMAP
        # =====================================================

        st.subheader("Instability Heatmap")

        heat = np.random.rand(10,10)

        fig3 = px.imshow(heat)

        st.plotly_chart(fig3)

        # =====================================================
        # POTENTIAL LANDSCAPE
        # =====================================================

        st.subheader("Potential Landscape")

        returns = np.diff(np.log(ts + 1e-6))

        kde = gaussian_kde(returns)

        x_vals = np.linspace(min(returns), max(returns), 200)

        p = kde(x_vals)

        U = -np.log(p + 1e-9)

        fig4 = px.line(x=x_vals, y=U)

        st.plotly_chart(fig4)

        # =====================================================
        # POWER SPECTRUM
        # =====================================================

        st.subheader("Power Spectrum")

        f, pxx = signal.welch(returns)

        fig5 = px.line(x=f[1:], y=pxx[1:])

        st.plotly_chart(fig5)

        # =====================================================
        # SYSTEM STATE
        # =====================================================

        last_res = res.dropna().iloc[-1]

        if last_res > 0.6:
            state = "🟢 Stable"
        elif last_res > 0.5:
            state = "🟡 Warning"
        elif last_res > 0.4:
            state = "🟠 Metastable"
        else:
            state = "🔴 Critical"

        st.subheader("System Diagnosis")

        st.write(f"Current state: **{state}**")

else:

    st.info("Configure parameters and run analysis.")
