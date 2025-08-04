import streamlit as st

# Configuración general
st.set_page_config(
    page_title="EMMA USM 2025 - Ejemplos LaTeX",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📄",
)

st.title("👑 EMMA USM 2025 - Explorador de Prompts")

# --- Ejemplos básicos ---
ejemplos_basicos = {
    "Conceptos Básicos": {
        "teoria": "Todo documento LaTeX comienza con la declaración de clase (`\\documentclass`) y el entorno `\\begin{document}` ... `\\end{document}`.",
        "codigo": r"""
\documentclass{article}
\usepackage{amsmath}

\begin{document}
\title{Ejemplo de Documento en \LaTeX}
\author{Francisco Alfaro, Valeska Canales}
\date{\today}
\maketitle

\section{Ecuaciones en \LaTeX}
Ejemplo de una ecuación matemática:

\begin{equation}
E = mc^2
\end{equation}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example1.png"
    },
    "Tablas Bonitas": {
        "teoria": "LaTeX permite crear tablas con precisión usando `booktabs` para una presentación profesional.",
        "codigo": r"""
\documentclass{article}
\usepackage{booktabs}

\begin{document}
\section{Tabla con Estilo}

\begin{tabular}{lcr}
\toprule
Nombre & Edad & Ciudad \\
\midrule
Ana & 23 & Valparaíso \\
Luis & 31 & Santiago \\
Valeska & 28 & Concepción \\
\bottomrule
\end{tabular}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example2.png"
    },
    "Colores y Texto": {
        "teoria": "Con `xcolor` puedes aplicar colores a textos, definir tonos personalizados y mejorar la presentación.",
        "codigo": r"""
\documentclass{article}
\usepackage{xcolor}

\begin{document}

\section*{Texto con Colores}

El texto puede ser \textcolor{blue}{azul}, \textcolor{red}{rojo}, o \textbf{\textcolor{orange}{resaltado}}.

También se pueden definir colores personalizados:
\textcolor[rgb]{0.1,0.6,0.1}{Verde especial.}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example3.png"
    },
    "Lógica Matemática": {
        "teoria": "LaTeX es ideal para escribir fórmulas matemáticas complejas, especialmente en lógica y teoría de conjuntos, gracias a `amsmath`.",
        "codigo": r"""
\documentclass{article}
\usepackage{amsmath}

\begin{document}

\section*{Lógica Proposicional}

Sea $P \Rightarrow Q$ la implicación. Podemos expresar su tabla de verdad como:

\[
\begin{array}{c|c|c}
P & Q & P \Rightarrow Q \\
\hline
V & V & V \\
V & F & F \\
F & V & V \\
F & F & V \\
\end{array}
\]

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example4.png"
    },
    "Listas Personalizadas": {
        "teoria": "Las listas ordenadas y no ordenadas se personalizan con `enumitem`, permitiendo cambiar símbolos, márgenes o mezclar listas anidadas.",
        "codigo": r"""
\documentclass{article}
\usepackage{enumitem}

\begin{document}

\section*{Lista con símbolo personalizado}

\begin{itemize}[label=\textbullet]
  \item Primera tarea completada
  \item Segunda tarea pendiente
  \item Tercera tarea en progreso
\end{itemize}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example5.png"
    }
}

# --- Ejemplos avanzados ---
ejemplos_avanzados = {
    "Presentación Beamer": {
        "teoria": "`beamer` permite crear presentaciones tipo PowerPoint, pero en PDF y con control total del contenido.",
        "codigo": r"""
\documentclass{beamer}
\usetheme{Madrid}
\usepackage{amsmath}

\title{Introducción a \LaTeX}
\author{Valeska Canales}
\date{\today}

\begin{document}

\frame{\titlepage}

\begin{frame}{Ecuación Clásica}
\begin{itemize}
  \item Física y matemáticas se ven mejor en LaTeX.
  \item Por ejemplo:
\end{itemize}

\[
E = mc^2
\]

\end{frame}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example61.png"
    },
    "Currículum con moderncv": {
        "teoria": "Con `moderncv` puedes diseñar CVs elegantes usando estilos, colores y secciones personalizadas.",
        "codigo": r"""
\documentclass[11pt,a4paper]{moderncv}
\moderncvstyle{classic}
\moderncvcolor{blue}

\name{Valeska}{Canales}
\title{Data Scientist - Charlista}
\email{valeska@example.com}
\phone[mobile]{+56~9~1234~5678}

\begin{document}

\makecvtitle

\section{Educación}
\cventry{2024--2025}{Diplomado en Docencia Universitaria}{Universidad Técnica Federico Santa María}{Chile}{}{}
\cventry{2024--2025}{Diplomado en Inteligencia Artificial para Educación}{Universidad Técnica Federico Santa María}{Chile}{}{}

\section{Experiencia}
\cventry{2024--2025}{Socia fundadora}{Seth\&Nut}{Chile}{}{
Cofundadora de una iniciativa educativa enfocada en democratizar el acceso al aprendizaje de programación y ciencia de datos. Diseño e imparto talleres interactivos para estudiantes y docentes, integrando herramientas como Python, Streamlit y Quarto para fomentar la enseñanza creativa y accesible.
}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example71.png"
    },
    "Póster con tikzposter": {
        "teoria": "`tikzposter` es ideal para pósteres científicos en gran formato. Permite bloques, colores y diseños precisos.",
        "codigo": r"""
\documentclass[a0paper,landscape,blockverticalspace=5mm]{tikzposter}

\title{Título del Póster}
\author{Francisco Alfaro, Valeska Canales}
\institute{UTFSM}

\usetheme{Default}
\usecolorstyle{Germany}

\begin{document}
\maketitle

\block{Introducción}{
LaTeX es ideal para pósteres científicos. Su tipografía profesional mejora el diseño.
}

\block{Objetivos}{
\begin{itemize}
  \item Crear pósteres con LaTeX.
  \item Personalizar colores y bloques.
  \item Incluir ecuaciones e imágenes.
\end{itemize}
}

\block{Ejemplo de ecuación}{
\[
E = mc^2
\]
}

\block{Conclusiones}{
\begin{itemize}
  \item Compilable en Overleaf.
  \item Resultado profesional.
\end{itemize}
}

\end{document}
""",
        "imagen": "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example8.png"
    }
}

# --- INTERFAZ ---
tab1, tab2 = st.tabs(["📘 Ejemplos Básicos", "🚀 Ejemplos Avanzados"])

with tab1:
    ejemplo = st.selectbox("Selecciona un ejemplo básico", list(ejemplos_basicos.keys()))
    datos = ejemplos_basicos[ejemplo]

    st.markdown("### 🧠 Teoría")
    st.info(datos["teoria"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💻 Código")
        st.code(datos["codigo"], language="latex")

    with col2:
        st.markdown("### 🖼️ Salida")
        st.image(datos["imagen"], width=700)
    
    st.success("📂 Puedes encontrar todos estos ejemplos en Overleaf: [Ver proyecto en línea](https://www.overleaf.com/read/ypdqgxpmzpzv#b87019)")


with tab2:
    ejemplo = st.selectbox("Selecciona un ejemplo avanzado", list(ejemplos_avanzados.keys()))
    datos = ejemplos_avanzados[ejemplo]

    st.markdown("### 🧠 Teoría")
    st.info(datos["teoria"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💻 Código")
        st.code(datos["codigo"], language="latex")

    with col2:
        st.markdown("### 🖼️ Salida")
        if datos["imagen"] == "https://raw.githubusercontent.com/Seth-Nut/talks/refs/heads/main/latex_2025/images/example8.png":
            st.image(datos["imagen"], width=1000)
        else:
            st.image(datos["imagen"], width=700)
    
    st.success("📂 Puedes encontrar todos estos ejemplos en Overleaf: [Ver proyecto en línea](https://www.overleaf.com/read/ypdqgxpmzpzv#b87019)")



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