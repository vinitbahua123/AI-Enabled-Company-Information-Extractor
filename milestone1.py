
import openai
from langchain.llms import OpenAI as LangChainOpenAI
from langchain.prompts import PromptTemplate
import os
# Replace with your actual OpenAI API key
from dotenv import load_dotenv
# Load the .env file
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = LangChainOpenAI(openai_api_key=OPENAI_API_KEY)
template = PromptTemplate.from_template(
    "Extract the following information about the company {company_name} in the format 'Field: Value': "
    "email"
)

def get_company_info(company_name):
    llm_chain = template | llm
    response = llm_chain.invoke({"company_name": company_name})
    return response

def parse_company_info(raw_data):
    if raw_data:
        lines = raw_data.split('\n')
        info = {}
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                value = value.strip()
                if value.lower() == "not provided":
                    value = None
                info[key.strip().lower().replace(' ', '_')] = value
        return info
    return None

def main():
    company_name = input("Enter Company Name: ")
    raw_data = get_company_info(company_name)
    company_info = parse_company_info(raw_data)

    if company_info and any(company_info.values()):
        print("\nCompany Information:")
        for key, value in company_info.items():
            if value:
                print(f"{key.capitalize().replace('_', ' ')}: {value}")
    else:
        print("No data found regarding this company.")

if __name__ == "__main__":
    main()
