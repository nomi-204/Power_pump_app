def pump_power(flow_rate, head, efficiency):
    rho = 1000      # density of water (kg/m^3)
    g = 9.81        # gravity (m/s^2)

    power = (rho * g * flow_rate * head) / efficiency
    return power / 1000  # convert to kW


# User Input
Q = float(input("Enter flow rate (m^3/s): "))
H = float(input("Enter head (m): "))
eta = float(input("Enter efficiency (0–1): "))

power_kw = pump_power(Q, H, eta)
print(f"Required Pump Power: {power_kw:.2f} kW")
