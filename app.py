import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("⚙️ Mechanical Unit Converter & Density Checker")

st.markdown("""
### Developed By:
**Muhammad Bilal Kundi**  
**Reg No: 25R/24-ME-88**
""")

# ---------------- SIDEBAR ----------------
option = st.sidebar.selectbox(
    "Choose Tool",
    ["Unit Converter", "Material Density Checker"]
)

# ---------------- UNIT CONVERTER ----------------
if option == "Unit Converter":

    st.header("🔄 Unit Converter")

    category = st.selectbox(
        "Select Conversion Type",
        ["Length", "Pressure", "Temperature"]
    )

    # LENGTH
    if category == "Length":

        meter = st.number_input("Enter Length in Meters", value=1.0)

        cm = meter * 100
        mm = meter * 1000
        inch = meter * 39.3701
        feet = meter * 3.28084

        st.write(f"Centimeters: {cm}")
        st.write(f"Millimeters: {mm}")
        st.write(f"Inches: {inch}")
        st.write(f"Feet: {feet}")

    # PRESSURE
    elif category == "Pressure":

        pa = st.number_input("Enter Pressure in Pascal", value=1.0)

        kpa = pa / 1000
        bar = pa / 100000
        psi = pa * 0.000145038

        st.write(f"kPa: {kpa}")
        st.write(f"Bar: {bar}")
        st.write(f"PSI: {psi}")

    # TEMPERATURE
    elif category == "Temperature":

        celsius = st.number_input("Enter Temperature in Celsius", value=0.0)

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        st.write(f"Fahrenheit: {fahrenheit}")
        st.write(f"Kelvin: {kelvin}")

# ---------------- DENSITY CHECKER ----------------
elif option == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.success(f"Density of {material} = {density} kg/m³")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "Made with Streamlit by Muhammad Bilal Kundi"
)
