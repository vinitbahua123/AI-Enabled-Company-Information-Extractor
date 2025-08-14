
# AI-Enabled Company Information Extractor

## Overview

In today’s fast-paced business environment, having accurate company information is essential for informed decision-making. However, finding this information using traditional methods can be time-consuming and inefficient. **AI-Enabled Company Information Extractor** solves this problem by providing a quick, reliable, and user-friendly way to access essential company details such as the CEO, website, products, and services.

By integrating advanced technologies like **OpenAI API**, **SerpAPI**, and **LangChain**, and delivering them through a **Streamlit**-based interface, the system ensures accurate and real-time company data retrieval in seconds.

---

## Features

* **Real-Time Data Retrieval** – Instantly fetch accurate company details from the internet.
* **Natural Language Query Processing** – Use OpenAI API to interpret and refine search queries.
* **Structured Data Management** – Utilize LangChain for efficient data processing.
* **Simple Search Interface** – Enter a company name and receive all relevant details in one organized output.
* **Error Handling** – Robust validation and handling for smooth user experience.
* **Organized Presentation** – Clear and easy-to-read results.

---

## Technology Stack

* **OpenAI API** – Natural language understanding and query processing.
* **SerpAPI** – Real-time web data retrieval.
* **LangChain** – Structured data processing and chaining results.
* **Streamlit** – Interactive and intuitive web-based interface.
* **Google Colab** – Development and experimentation environment.

---

## System Requirements

* Python 3.8+
* Streamlit
* OpenAI API Key
* SerpAPI Key
* LangChain library

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/vinitbahua123/AI-Enabled-Company-Information-Extractor.git
   cd AI-Enabled-Company-Information-Extractor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file and add:

   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPAPI_KEY=your_serpapi_key
   ```

4. **Run the application**

   ```bash
   streamlit run Company_info_extractor.py
   ```

---

## How It Works

1. **User Input** – Enter the company name into the search bar.
2. **Data Retrieval** – SerpAPI fetches relevant web data in real-time.
3. **Data Processing** – LangChain organizes and structures the retrieved data.
4. **Presentation** – Streamlit displays the results in a clean, easy-to-read format.

---

## Output Example

For a given company, the tool can return:

* **CEO Name**
* **Website**
* **Products & Services**
* **Brief Overview**
* **Additional Key Facts**

Data Retreival for company INFOSYS
 <img width="826" height="778" alt="image" src="https://github.com/user-attachments/assets/440990f9-37cb-494a-99e6-c1bf5fa45880" />


Data Retreival for company AMD
<img width="805" height="817" alt="image" src="https://github.com/user-attachments/assets/ba1f6408-365b-4544-b995-0df6d2a25e05" />


---

## Conclusion

The AI-Enabled Company Information Extractor streamlines the process of retrieving critical company information by combining AI, real-time search APIs, and an intuitive interface. The tool enables faster, more accurate decision-making and showcases the potential of AI-powered information retrieval systems.

