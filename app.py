import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f4f4f4;
}

h1, h2, h3 {
    color: #2c3e50;
}

.stButton>button {
    background-color: #5d6d7e;
    color: white;
    border-radius: 10px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #ecf0f1;
    border-radius: 8px;
}

.info-box {
    background-color: #d5dbdb;
    padding: 15px;
    border-radius: 12px;
    color: #1c2833;
    margin-bottom: 20px;
}

.result-box {
    background-color: #ebedef;
    padding: 15px;
    border-radius: 12px;
    color: #212f3d;
    margin-top: 15px;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

st.markdown("""
<div class="info-box">

### Developed By  
**Muhammad Bilal Kundi**  
**Reg No: 25R/24-ME-88**

</div>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
main_col, side_col = st.columns([4, 1])

# ---------------- RIGHT SIDE TOOL PANEL ----------------
with side_col:

    st.markdown("## 🛠️ Tools")

    option = st.radio(
        "Choose Tool",
        ["Unit Converter", "Material Density Checker"]
    )

# ---------------- MAIN CONTENT ----------------
with main_col:

    # =====================================================
    # UNIT CONVERTER
    # =====================================================
    if option == "Unit Converter":

        st.header("🔄 Mechanical Unit Converter")

        category = st.selectbox(
            "Select Conversion Type",
            [
                "Length",
                "Pressure",
                "Temperature",
                "Force",
                "Velocity",
                "Power"
            ]
        )

        # ---------------- LENGTH ----------------
        if category == "Length":

            meter = st.number_input("Enter Length in Meters", value=1.0)

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - Centimeters = {meter * 100:.2f} cm  
            - Millimeters = {meter * 1000:.2f} mm  
            - Inches = {meter * 39.3701:.2f} in  
            - Feet = {meter * 3.28084:.2f} ft

            </div>
            """, unsafe_allow_html=True)

        # ---------------- PRESSURE ----------------
        elif category == "Pressure":

            pa = st.number_input("Enter Pressure in Pascal", value=1.0)

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - kPa = {pa / 1000:.4f}  
            - Bar = {pa / 100000:.6f}  
            - PSI = {pa * 0.000145038:.6f}

            </div>
            """, unsafe_allow_html=True)

        # ---------------- TEMPERATURE ----------------
        elif category == "Temperature":

            celsius = st.number_input("Enter Temperature in Celsius", value=0.0)

            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - Fahrenheit = {fahrenheit:.2f} °F  
            - Kelvin = {kelvin:.2f} K

            </div>
            """, unsafe_allow_html=True)

        # ---------------- FORCE ----------------
        elif category == "Force":

            newton = st.number_input("Enter Force in Newton", value=1.0)

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - Kilonewton = {newton / 1000:.4f} kN  
            - Pound-force = {newton * 0.224809:.4f} lbf

            </div>
            """, unsafe_allow_html=True)

        # ---------------- VELOCITY ----------------
        elif category == "Velocity":

            ms = st.number_input("Enter Velocity in m/s", value=1.0)

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - km/h = {ms * 3.6:.2f}  
            - mph = {ms * 2.23694:.2f}

            </div>
            """, unsafe_allow_html=True)

        # ---------------- POWER ----------------
        elif category == "Power":

            watt = st.number_input("Enter Power in Watt", value=1.0)

            st.markdown(f"""
            <div class="result-box">

            ### Results

            - Kilowatt = {watt / 1000:.4f} kW  
            - Horsepower = {watt * 0.00134102:.4f} hp

            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # DENSITY CHECKER
    # =====================================================
    elif option == "Material Density Checker":

        st.header("🧱 Material Density Checker")

        materials = {
            "Steel": 7850,
            "Stainless Steel": 8000,
            "Aluminum": 2700,
            "Copper": 8960,
            "Brass": 8500,
            "Bronze": 8800,
            "Titanium": 4500,
            "Cast Iron": 7200,
            "Lead": 11340,
            "Zinc": 7135,
            "Nickel": 8908,
            "Magnesium": 1740,
            "Concrete": 2400,
            "Glass": 2500,
            "Rubber": 1522,
            "PVC Plastic": 1380,
            "Wood": 700,
            "Gold": 19300,
            "Silver": 10490
        }

        material = st.selectbox(
            "Select Material",
            list(materials.keys())
        )

        density = materials[material]

        st.markdown(f"""
        <div class="result-box">

        ### Density Result

        **{material}**  
        Density = **{density} kg/m³**

        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Made with Streamlit by Muhammad Bilal Kundi")
