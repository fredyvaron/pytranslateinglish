# 📖 pytranslateinglish
🔄 Traducción de inglés a español y viceversa (texto y PDFs) con IA.




## ✨ Características
✅ Traducción entre inglés y español usando modelos de IA.
✅ Traduce texto o archivos PDF completos.
✅ Mantiene el formato del PDF al traducir.

## 🚀 Instalación
Instala la librería desde PyPI:


``` 
pip install pytranslateinglish

```

## 📝 Uso
📌 1. Traducción de texto
```
from pytranslateinglish import PyTranslateInglish

translator = PyTranslateInglish()
translated_text = translator.translate_text("Hello, how are you?", direction="en-es")
print(translated_text)  # "Hola, ¿cómo estás?"

```
📌 Parámetros:

text → Texto a traducir.
direction → "en-es" (inglés → español) o "es-en" (español → inglés).
📌 2. Traducción de PDF

translator.translate_pdf("documento.pdf", "translated.pdf", direction="es-en")
📌 Parámetros:

```
input_pdf → Nombre del archivo PDF de entrada.
output_pdf → Nombre del PDF traducido.
direction → "en-es" o "es-en".
```

## 🛠 Requisitos
torch
transformers
pymupdf
(Se instalan automáticamente con pip install pytranslateinglish 🎉)

