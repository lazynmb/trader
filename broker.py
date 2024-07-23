import openai

class Broker:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_report(self, report):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Analyze the following report and provide investment advice:\n\n{report}",
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def generate_advice(self, report):
        analysis = self.analyze_report(report)
        return f"Investment Advice Report:\n\n{analysis}"
