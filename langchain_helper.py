from langchain.llms import openai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
load_dotenv()


def generateDescription(name, sample1, sample2, sample3, sample4) -> str:
    llm = openai.OpenAI(temperature=1)
    prompt_template = PromptTemplate(
        input_variables=["name", "sample1", "sample2", "sample3", "sample4"],
        template="""My name is {name}. And I want to effectively describe my skills inorder to gain more client in feild of programming, I have some samples please see these samples and create a better one for me with my name, use same skills described in samples:
        Sample1:
        {sample1}
        Sample2:
        {sample2}
        Sample3:
        {sample3}
        Sample4:
        {sample4}
        Please use bullet points and make it precise and clear"""
    )

    name = LLMChain(prompt=prompt_template, llm=llm)
    response = name({'name': name, 'sample1': sample1,
                    "sample2": sample2, "sample3": sample3, "sample4": sample4})
    return response["text"]


if __name__ == "__main__":
    print(generateDescription("dog", "black"))
