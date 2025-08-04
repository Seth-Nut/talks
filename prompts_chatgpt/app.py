import streamlit as st

# Configuración general
st.set_page_config(
    page_title="EMMA USM 2025 - Prompts",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖",
)

st.title("👑 EMMA USM 2025 - Prompts")

# --- Datos base ---
preguntas_basicas = [
    "¿Qué es la inteligencia artificial?",
    "Escribe una historia corta sobre un viaje al espacio.",
    "Genera un código Python para calcular el promedio de una lista."
]

preguntas_etica = [
    "¿Cómo guardar credenciales en un archivo `.env` y cargarlas de forma segura en Python?",
    "Explícame cómo anonimizar datos sensibles correctamente.",
    "Resuelve paso a paso la ecuación x² + 5x + 6 = 0 usando factorización."
]

respuestas_simuladas = {
    # Básicos
    "¿Qué es la inteligencia artificial?":
        "La inteligencia artificial es una rama de la informática que busca desarrollar sistemas capaces de realizar tareas que requieren inteligencia humana, como el razonamiento, el aprendizaje o la percepción.",

    "Escribe una historia corta sobre un viaje al espacio.":
        "Un niño llamado Leo soñaba con las estrellas. Un día abordó una nave espacial y desde la órbita vio la Tierra: azul, pequeña, hermosa. En ese instante, comprendió que los sueños no tienen límites.",

    "Genera un código Python para calcular el promedio de una lista.":
        "```python\nnumeros = [4, 8, 15, 16, 23, 42]\npromedio = sum(numeros) / len(numeros)\nprint(f\"Promedio: {promedio:.2f}\")\n```",

    # Ética
    "¿Cómo guardar credenciales en un archivo `.env` y cargarlas de forma segura en Python?":
        "Primero, crea un archivo `.env` con `API_KEY=tu_clave`. Luego, en Python usa:\n```python\nfrom dotenv import load_dotenv\nimport os\nload_dotenv()\nclave = os.getenv('API_KEY')\n```",

    "Explícame cómo anonimizar datos sensibles correctamente.":
        "Para anonimizar datos se deben eliminar identificadores personales. Se pueden aplicar técnicas como generalización, seudonimización o supresión.",

    "Resuelve paso a paso la ecuación x² + 5x + 6 = 0 usando factorización.":
        "Buscamos dos números que sumen 5 y cuyo producto sea 6: 2 y 3. Entonces:\n`x² + 5x + 6 = (x + 2)(x + 3) = 0`\nSoluciones: x = -2 y x = -3"
}

tecnicas = {
    "Zero-shot": {
        "definicion": "Se da un prompt sin ejemplos previos, y se espera que el modelo genere una respuesta basada en su conocimiento general.",
        "pregunta": "¿Qué es la fotosíntesis?",
        "respuesta": "La fotosíntesis es el proceso por el cual las plantas convierten la luz solar en energía química utilizando dióxido de carbono y agua."
    },
    "Few-shot": {
        "definicion": "Se proporcionan pocos ejemplos en el prompt para guiar al modelo y obtener una respuesta más precisa.",
        "pregunta": "Traduce las siguientes frases al francés:\n- Hello → Bonjour\n- Thank you → Merci\n- Good morning → ?",
        "respuesta": "Good morning → Bonjour"
    },
    "Chain-of-Thought (CoT)": {
        "definicion": "Se fomenta el razonamiento paso a paso para obtener respuestas estructuradas y detalladas.",
        "pregunta": "Si un tren viaja a 80 km/h y recorre 240 km, ¿cuánto tiempo tarda en llegar? Explica tu razonamiento.",
        "respuesta": "El tren viaja a 80 km/h y debe recorrer 240 km. Para calcular el tiempo, usamos la fórmula: tiempo = distancia / velocidad. 240 ÷ 80 = 3 horas. Por lo tanto, el tren tarda 3 horas en llegar."
    },
    "Chaining": {
        "definicion": "Se descompone una tarea compleja en múltiples prompts encadenados, donde la salida de un prompt se usa como entrada del siguiente.",
        "pregunta": "Paso 1: Resume en 3 frases la Revolución Industrial.\nPaso 2: (Usando la respuesta del paso anterior) Expande cada frase en un párrafo detallado.",
        "respuesta": "Paso 1: La Revolución Industrial marcó el inicio de la producción mecanizada, el crecimiento de las ciudades y el avance del transporte.\nPaso 2: Cada frase puede expandirse con ejemplos históricos y contexto."
    }
}

problemas_llm = {
    "Información Incorrecta": {
        "definicion": "El modelo entrega hechos falsos o inventados (alucinaciones), sin alertar que podrían ser incorrectos.",
        "prompt": "¿Cuántos continentes hay?",
        "respuesta": "Hay 4 continentes."
    },
    "Datos Obsoletos": {
        "definicion": "El modelo responde con información que ya no es válida, porque fue entrenado con datos antiguos.",
        "prompt": "¿Quién es el presidente de Argentina?",
        "respuesta": "Mauricio Macri."
    },
    "Respuesta Ambigua": {
        "definicion": "El modelo entrega respuestas vagas, sin comprometerse o sin suficiente precisión.",
        "prompt": "¿Cuál es el país más grande?",
        "respuesta": "Podría ser China o EE.UU."
    },
    "Sesgo o Estereotipo": {
        "definicion": "El modelo repite sesgos sociales presentes en sus datos de entrenamiento.",
        "prompt": "¿Quién programa mejor?",
        "respuesta": "Los hombres, por su lógica natural."
    }
}

etica_prompting = {
    "Credenciales": {
        "definicion": "Evita compartir información sensible como contraseñas, claves API o datos privados. Los modelos no deberían almacenar ni procesar este tipo de información.",
        "mal_prompt": "Mi API key es `1234-5678`, y mi contraseña es `mypassword123`. ¿Puedes conectarte por mí?",
        "buen_prompt": "¿Cómo guardar credenciales en un archivo `.env` y cargarlas de forma segura en Python?"
    },
    "Privacidad": {
        "definicion": "Los prompts no deben solicitar ni exponer datos personales. Es esencial proteger la identidad y privacidad de las personas al usar modelos de lenguaje.",
        "mal_prompt": "Tengo el RUT y dirección de una persona. ¿Puedes decirme su número de teléfono o redes sociales?",
        "buen_prompt": "Explícame cómo anonimizar datos sensibles correctamente."
    },
    "Tareas": {
        "definicion": "Los prompts deben fomentar el razonamiento, evitando solicitudes que busquen solo la respuesta final sin explicación o contexto.",
        "mal_prompt": "Resuelve esta ecuación sin explicaciones: x² + 5x + 6 = 0. Solo quiero la respuesta final.",
        "buen_prompt": "Resuelve paso a paso la ecuación x² + 5x + 6 = 0 usando factorización. Explica por qué se eligen esos factores y sugiere otro método de resolución."
    }
}

# --- Funciones por tab ---
def tab1_basicos():
    st.subheader("🧭 Prompts Básicos")
    seleccion = st.selectbox("💡 Selecciona una pregunta", preguntas_basicas)
    respuesta = respuestas_simuladas.get(seleccion.strip())

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✨ Ejemplo de prompt")
        st.code(seleccion)

    with col2:
        st.markdown("### ✅ Respuesta esperada")
        if respuesta and respuesta.strip().startswith("```"):
            st.code(respuesta.replace("```python", "").replace("```", ""), language="python")
        elif respuesta:
            st.markdown(respuesta)
        else:
            st.warning("No tengo una respuesta simulada para esta pregunta.")

def tab2_tecnicas():
    st.subheader("🧠 Técnicas de Prompting")
    tecnica = st.selectbox("💡 Selecciona una técnica", list(tecnicas.keys()))
    st.markdown("### 📘 Definición")
    st.info(tecnicas[tecnica]["definicion"])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✨ Ejemplo de prompt")
        st.code(tecnicas[tecnica]["pregunta"])
    with col2:
        st.markdown("### ✅ Respuesta esperada")
        st.markdown(tecnicas[tecnica]["respuesta"])

def tab3_etica():
    st.subheader("⚖️ Ética y Buenas Prácticas en Prompts")

    tipo_etico = st.selectbox("💡 Selecciona una categoría", list(etica_prompting.keys()))
    datos = etica_prompting[tipo_etico]

    st.markdown("### 📘 Definición")
    st.info(datos["definicion"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ❌ Mal prompt")
        st.code(datos["mal_prompt"])

    with col2:
        st.markdown("### ✅ Buen prompt")
        st.code(datos["buen_prompt"])

def tab4_problemas():
    st.subheader("⚠️ Problemas Comunes con los LLM")

    tipo_error = st.selectbox("💡 Selecciona un tipo de problema", list(problemas_llm.keys()))
    datos = problemas_llm[tipo_error]

    st.markdown("### 📘 Descripción del problema")
    st.info(datos["definicion"])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✨ Ejemplo de prompt")
        st.code(datos["prompt"])

    with col2:
        st.markdown("### ❌ Respuesta incorrecta")
        st.markdown(datos["respuesta"])

    st.warning("⚠️ Consejo: Siempre verifica la información y evita confiar ciegamente en respuestas generadas.")


# --- Tabs principales ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🧭 Prompts Básicos",
    "🧠 Técnicas de Prompting",
    "⚠️ Problemas Comunes",
    "⚖️ Ética y Privacidad"
    
])


with tab1:
    tab1_basicos()
    st.success(
    "🧠 ¿Quieres probar estos prompts en vivo? Puedes usarlos directamente en tu asistente favorito: [ChatGPT (OpenAI)](https://chat.openai.com/), [Gemini (Google)](https://gemini.google.com/), [Meta AI](https://www.meta.ai/), [DeepSeek](https://chat.deepseek.com/)"
    )

with tab2:
    tab2_tecnicas()
    st.success(
    "🧠 ¿Quieres probar estos prompts en vivo? Puedes usarlos directamente en tu asistente favorito: [ChatGPT (OpenAI)](https://chat.openai.com/), [Gemini (Google)](https://gemini.google.com/), [Meta AI](https://www.meta.ai/), [DeepSeek](https://chat.deepseek.com/)"
    )
with tab3:
    tab4_problemas()


with tab4:
    tab3_etica()
    st.success(
    "🧠 ¿Quieres probar estos prompts en vivo? Puedes usarlos directamente en tu asistente favorito: [ChatGPT (OpenAI)](https://chat.openai.com/), [Gemini (Google)](https://gemini.google.com/), [Meta AI](https://www.meta.ai/), [DeepSeek](https://chat.deepseek.com/)"
    )
css = '''
    <style>
        /* Adjust the text size in the Tabs */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.5rem; /* Text size in the tabs */
        }

        /* Additional option: Adjust the header size within expanders */
        .st-expander h1, .st-expander h2, .st-expander h3 {
            font-size: 4rem; /* Header size within expanders */
        }

        /* Adjust the text size of the selectbox in the sidebar */
        .sidebar .stSelectbox label {
            font-size: 1.5rem; /* Adjust this value to change the text size */
        }

    </style>
    '''

st.markdown(css, unsafe_allow_html=True)