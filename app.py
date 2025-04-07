import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

llm = CTransformers(
    model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
    config={"max_new_tokens": 512, "temperature": 0.7}
)

    # Prompt Template
    template = """
    Write a blog for a {blog_style} job profile on the topic "{input_text}",
    within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    # Generate the response from the LLama 2 model
    final_prompt = prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    )
    
    response = llm(final_prompt)
    return response


# Streamlit UI Setup
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Blogs 🤖")

# User inputs
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("No. of Words")
with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People"),
        index=0
    )

submit = st.button("Generate")

# Generate and display blog
if submit:
    if input_text and no_words:
        try:
            with st.spinner("Generating..."):
                output = getLLamaresponse(input_text, no_words, blog_style)
                st.success("Here's your blog:")
                st.write(output)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please fill in all fields.")

'''import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model
   llm = CTransformers(
    model="TheBloke/Llama-2-7B-Chat-GGML",
    model_file="llama-2-7b-chat.ggmlv3.q8_0.bin",
    config={"max_new_tokens": 512, "temperature": 0.7}
)
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))'''
