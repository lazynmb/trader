import os
from dotenv import load_dotenv
from researcher import Researcher

load_dotenv()

if __name__ == "__main__":
    company_name = "Apple Inc"

    # Tworzenie raportu przez Researchera
    researcher = Researcher(company_name)
    researcher.create_report()
    print(f"Reports created for {company_name}. Check the following files:")
    print(f"- Actions Log: {company_name}_actions_log.txt")
    print(f"- Research Report: {company_name}_research_report.txt")
