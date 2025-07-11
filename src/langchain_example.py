from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    # This template will take a 'product' variable and ask AI to generate a company name
    prompt = ChatPromptTemplate.from_template(
        "What is a good name for a company that makes {product}?"
    )

    # Initialize the OpenAI LLM
    # It uses API key defined in OPENAI_API_KEY environment variable
    llm = OpenAI(temperature=0.9)

    # Pipe the prompt to the llm, and then to a string output parser
    chain = prompt | llm | StrOutputParser()

    # Define the product we want a company name for
    product_query = "colorful socks"

    print(f"Generating a company name for a company that makes: {product_query}")

    # Run the chain with our product query as a dictionary
    company_name = chain.invoke({"product": product_query})

    print(f"Generated Company Name: {company_name.strip()}")

if __name__ == "__main__":
    main()
