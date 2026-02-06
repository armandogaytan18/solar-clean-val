import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Solar Clean McMinnville", page_icon="☀️")

# Encabezado con gancho comercial
st.title("☀️ Solar Clean McMinnville")
st.subheader("¡No dejes que la lluvia de Oregon ensucie tus ahorros!")

st.markdown("""
¿Sabías que la acumulación de polen y minerales puede reducir la eficiencia de tus paneles hasta en un **30%**? 
La lluvia no es suficiente para limpiarlos. 
             
**Ofrecemos:**
* Limpieza técnica con agua desionizada.
* Inspección visual de micro-fisuras.
* Reporte de eficiencia post-limpieza.
""")

st.divider()

# Formulario de captura
st.write("### Reserva una inspección gratuita en el área 97128")
with st.form("solicitud_cliente"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono de contacto")
    zip_code = st.selectbox("Código Postal", ["97128", "97111", "97132", "Otro"])
    
    boton_envio = st.form_submit_button("Solicitar cotización gratuita")

    if boton_envio:
        if nombre and email:
            # Guardar datos en un CSV local para validar
            nuevo_lead = {
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Nombre": nombre,
                "Email": email,
                "Telefono": telefono,
                "Zip": zip_code
            }
            df = pd.DataFrame([nuevo_lead])
            df.to_csv("interesados.csv", mode='a', header=not st.file_exists("interesados.csv"), index=False)
            
            st.success(f"¡Gracias {nombre}! Te contactaremos en menos de 24 horas.")
            st.balloons()
        else:
            st.error("Por favor completa los campos principales.")

# Footer informativo
st.info("Servicio local en Yamhill County. Garantía de eficiencia o no pagas.")
