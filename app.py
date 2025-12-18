import streamlit as st

st.set_page_config(page_title="Pump Power Calculator", page_icon="💧")

st.title("💧 Pump Power Calculator")
st.write("Calculate the required pump power based on flow rate, head, and efficiency.")

# Input fields
flow_rate = st.number_input(
    "Flow Rate (m³/s)",
    min_value=0.0,
    step=0.01
)

head = st.number_input(
    "Head (m)",
    min_value=0.0,
    step=1.0
)

efficiency = st.number_input(
    "Efficiency (0–1)",
    min_value=0.01,
    max_value=1.0,
    step=0.01
)

# Button
if st.button("Calculate Pump Power"):
    rho = 1000   # kg/m^3
    g = 9.81     # m/s^2

    power_watt = (rho * g * flow_rate * head) / efficiency
    power_kw = power_watt / 1000

    st.success(f"🔌 Required Pump Power: **{power_kw:.2f} kW**")
  
