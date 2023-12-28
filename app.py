import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get a response from my Llama2 model
def getLlamaresponse(input_text,no_words,blog_style):

    # Llama2 model
    llm = CTransformers(model='D:/Generative AI/models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    #Prompt Template
    template="""
        Write a blog for target audience of {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                            template = template)
    
    #Generate response from the model 
    response = llm(prompt.format(blog_style= blog_style, input_text= input_text, no_words = no_words))
    print(response)
    
    return response



st.set_page_config(page_title = "Blog Builder",
                    page_icon= '🤖',
                    layout = 'centered',
                    initial_sidebar_state='collapsed')

st.header("Blog Builder 🤖")

input_text = st.text_input("Enter the Blog Topic: ")

# Creating two more columns for additional inputs from the user
col1,col2 =  st.columns([5,5])

with col1:
    no_words = st.text_input('Enter Number of Words: ')
with col2:
    blog_style = st.selectbox('Target Audience:',
                              ('Researchers','Data Scientists','Software Engineers','Other' ), index = 0)
    
submit = st.button("Build")

#Final Response
if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))

