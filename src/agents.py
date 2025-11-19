import openai

class QueryAgent:
    def run(self, query):
        return {"query": query.strip()}

class SummarizerAgent:
    def run(self, text):
        return text[:500]

class ResponseAgent:
    def run(self, data):
        return f"Here is a simple explanation: {data}"
