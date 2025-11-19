from agents import QueryAgent, SummarizerAgent, ResponseAgent

class EduMatePipeline:
    def __init__(self):
        self.q = QueryAgent()
        self.s = SummarizerAgent()
        self.r = ResponseAgent()

    def run(self, question):
        q = self.q.run(question)
        s = self.s.run(q["query"])
        return self.r.run(s)
