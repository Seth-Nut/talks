import streamlit as st
from openai import OpenAI

# Configuración
st.set_page_config(page_title="Explorador de Prompts", layout="centered")
st.title("🤖 Explorador de Prompts + Chatbot")

# Ingreso de API Key
st.session_state.api_key = st.text_input(
    "🔑 Ingresa tu OpenAI API Key (no se guarda):", type="password", placeholder="sk-..."
)

# --- CLIENTE ---
if st.session_state.api_key.startswith("sk-"):
    client = OpenAI(api_key=st.session_state.api_key)

# --- CATEGORÍAS Y TIPOS ---
categorias = {
    "🧭 Prompt directo o instrucción": [
        "Pregunta directa",
        "Instrucción",
        "Comando",
    ],
    "🧠 Técnicas de prompting": [
        "Zero-shot",
        "Few-shot",
        "CoT (Chain-of-Thought)",
        "Chaining",
    ],
    "⚖️ Ética y privacidad": [
        "Credenciales",
        "Privacidad",
        "Tareas",
    ]
}

explicaciones = {
    "Pregunta directa": "Un prompt que hace una pregunta específica esperando una respuesta concreta.",
    "Instrucción": "Solicita realizar una tarea. Ejemplo: 'Redacta una carta formal'.",
    "Comando": "Da una orden clara. Ejemplo: 'Genera un código Python para...'",

    "Zero-shot": "El modelo responde sin ejemplos previos. Ej: '¿Qué es la fotosíntesis?'",
    "Few-shot": "Se entregan algunos ejemplos para guiar la respuesta.",
    "CoT (Chain-of-Thought)": "Se pide razonamiento paso a paso para llegar a la respuesta.",
    "Chaining": "Se divide una tarea en pasos encadenados. El output de uno es el input del siguiente.",

    "Credenciales": "Evita pedir claves o datos sensibles. Usa prompts que promuevan buenas prácticas.",
    "Privacidad": "Protege información personal. No uses datos reales en tus prompts.",
    "Tareas": "Promueve aprendizaje. Evita respuestas sin explicación o con atajos.",
}

ejemplos = {
    "Pregunta directa": ["¿Qué es la inteligencia artificial?"],
    "Instrucción": ["Escribe una historia corta sobre un viaje al espacio."],
    "Comando": ["Genera un código Python para calcular el promedio de una lista."],

    "Zero-shot": ["¿Qué es la fotosíntesis?"],
    "Few-shot": ["Traduce las siguientes frases al francés:\n- Hello → Bonjour\n- Thank you → Merci\n- Good morning → ?"],
    "CoT (Chain-of-Thought)": [
        "Si un tren viaja a 80 km/h y recorre 240 km, ¿cuánto tiempo tarda? Explica tu razonamiento."
    ],
    "Chaining": [
        "Paso 1: Resume en 3 frases la Revolución Industrial.\nPaso 2: Expande cada frase en un párrafo detallado."
    ],

    "Credenciales": ["¿Cómo guardar credenciales en un archivo `.env` y cargarlas de forma segura en Python?"],
    "Privacidad": ["Explícame cómo anonimizar datos sensibles correctamente."],
    "Tareas": ["Resuelve paso a paso la ecuación x² + 5x + 6 = 0 usando factorización."]
}

# Sidebar: selección de categoría y tipo
st.sidebar.title("📚 Tipos de Prompt")
categoria = st.sidebar.radio("Selecciona una categoría", list(categorias.keys()))
tipo = st.sidebar.radio("Selecciona un tipo", categorias[categoria])

# Mostrar explicación
st.subheader(f"🧩 Tipo: {tipo}")
st.markdown(f"🔍 **Descripción:** {explicaciones.get(tipo, 'Descripción no disponible')}")

# Botones con ejemplos sugeridos
st.subheader("💡 Ejemplos sugeridos")
for i, ejemplo in enumerate(ejemplos[tipo]):
    if st.button(f"Usar ejemplo #{i+1}"):
        st.session_state.user_prompt = ejemplo

# Caja de texto editable
st.subheader("✍️ Escribe o edita tu prompt")
user_input = st.text_area("Prompt", st.session_state.get("user_prompt", ""), height=150)

# Chat real con OpenAI
if st.session_state.api_key.startswith("sk-"):

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "Eres un asistente educativo experto en prompts."}]

    if st.button("💬 Enviar al asistente"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Pensando..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.success("✅ Respuesta generada")
                st.markdown(f"**🤖 Respuesta:**\n\n{reply}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    with st.expander("🕑 Historial"):
        for m in st.session_state.messages[1:]:
            st.markdown(f"**{m['role'].capitalize()}**: {m['content']}")
else:
    st.warning("Ingresa tu OpenAI API Key para utilizar el asistente.")
