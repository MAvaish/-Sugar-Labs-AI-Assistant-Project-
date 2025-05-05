from transformers import pipeline
import logging

class AIAssistant:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.model = pipeline(
            "text-generation",
            model="distilgpt2",
            device="cpu",
            framework="pt"
        )
        logging.info("AI Assistant ready!")

    def get_suggestion(self, text):
        try:
            output = self.model(
                text,
                max_new_tokens=30,
                temperature=0.7
            )
            return output[0]['generated_text']
        except Exception as e:
            logging.error(f"AI Error: {str(e)}")
            return "AI suggestion unavailable"