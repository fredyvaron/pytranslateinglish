import torch
from transformers import MarianMTModel, MarianTokenizer
import fitz  # PyMuPDF
import io

class PyTranslateInglish:
    MODEL_NAMES = {
        "en-es": "Helsinki-NLP/opus-mt-en-es",
        "es-en": "Helsinki-NLP/opus-mt-es-en"
    }

    def __init__(self):
        self.models = {direction: MarianMTModel.from_pretrained(name) for direction, name in self.MODEL_NAMES.items()}
        self.tokenizers = {direction: MarianTokenizer.from_pretrained(name) for direction, name in self.MODEL_NAMES.items()}
        for model in self.models.values():
            model.eval()

    def translate_text(self, text: str, direction: str) -> str:
        if direction not in self.models:
            raise ValueError("Invalid translation direction. Use 'en-es' or 'es-en'.")

        model = self.models[direction]
        tokenizer = self.tokenizers[direction]

        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            output = model.generate(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"])
        
        return tokenizer.decode(output[0], skip_special_tokens=True)

    def translate_pdf(self, file_content: bytes, direction: str) -> bytes:
        if direction not in self.models:
            raise ValueError("Invalid translation direction. Use 'en-es' or 'es-en'.")

        model = self.models[direction]
        tokenizer = self.tokenizers[direction]

        pdf_document = fitz.open(stream=file_content, filetype="pdf")
        output_pdf = fitz.open()

        for page in pdf_document:
            new_page = output_pdf.new_page(width=page.rect.width, height=page.rect.height)
            text_blocks = []

            for block in page.get_text("dict")["blocks"]:
                block_text = []
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        block_text.append(span["text"])
                
                if block_text:
                    text_blocks.append("\n".join(block_text))

            translated_blocks = []
            for block in text_blocks:
                inputs = tokenizer(block, return_tensors="pt", truncation=True, padding=True, max_length=512)
                with torch.no_grad():
                    output = model.generate(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"])
                translated_blocks.append(tokenizer.decode(output[0], skip_special_tokens=True))

            y_position = 50
            for translated_text in translated_blocks:
                new_page.insert_text((50, y_position), translated_text, fontsize=12)
                y_position += 20

        pdf_bytes = io.BytesIO()
        output_pdf.save(pdf_bytes)
        output_pdf.close()
        pdf_bytes.seek(0)

        return pdf_bytes.getvalue()