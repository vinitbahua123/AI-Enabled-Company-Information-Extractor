import os
from dotenv import load_dotenv
import streamlit as st
from langchain import OpenAI, PromptTemplate
from langchain.agents import load_tools, initialize_agent, AgentType
import json
import re

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI LLM
@st.cache_resource
def get_llm():
    return OpenAI(api_key=openai_api_key)

# Load tools (only serpapi)
@st.cache_resource
def get_tools():
    llm = get_llm()
    return load_tools(["serpapi"], llm=llm)

# Initialize agent
@st.cache_resource
def get_agent():
    llm = get_llm()
    tools = get_tools()
    return initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

# Define PromptTemplate for basic company information
# Define PromptTemplate for basic company information
basic_info_template = PromptTemplate.from_template(
    "Retrieve detailed information for the company {company_name}. The details should include:\n"
    "- Company Name\n"
    "- Email\n"
    "- Phone number\n"
    "- Website\n"
    "- Postal code\n"
    "- Address\n"
    "- City\n"
    "- Products\n"
    "- Services\n"
    "- Revenue\n"
    "- Competitors\n"
    "- Branches\n"
    "- Careers\n"
    "Also retrieve:\n"
    "- Email address\n"
    "- Phone number\n"
    "Please ensure the information is accurate and up-to-date. Format the output as a Python dictionary with keys and values."
)


# Streamlit app
st.title("Company Information Extractor")

st.markdown("""
Discover detailed information about companies using AI. Simply enter a company name below and click 'Get Information' to see the details""")

# Get the company name from the user
company_name = st.text_input("Enter the company name:")

# Define key_order globally
key_order = ["Company Name", "Email", "Phone number", "Website", "Postal code", "Address", "City", "Products", "Services", "Revenue", "Competitors", "Branches", "Careers"]

if st.button("Get Information"):
    if company_name:
        with st.spinner("Retrieving information..."):
            agent = get_agent()
            basic_info_prompt = basic_info_template.format(company_name=company_name)
            basic_info_result = agent.run(basic_info_prompt)

            # Print or display basic_info_result for debugging
            #st.write("Response from AI model:", basic_info_result)

            # Extract the dictionary from the result
            match = re.search(r'\{.*\}', basic_info_result, re.DOTALL)
            if match:
                try:
                    company_info = json.loads(match.group(0).replace("'", '"'))
                    
                    # Display success message
                    st.success("Information successfully retrieved!")
                    
                    # Display the information
                    st.markdown("### Company Information:")
                    for key in key_order:
                        if key in company_info:
                            st.markdown(f"**{key}:** {company_info[key]}")
                except json.JSONDecodeError as e:
                    st.error(f"Error decoding JSON: {str(e)}")
            else:
                st.error("Error: Could not extract company information. No valid JSON-like content found.")
    else:
        st.warning("Please enter a company name.")

# Add a footer
st.markdown("---")
st.markdown("Created using Streamlit and LangChain")
