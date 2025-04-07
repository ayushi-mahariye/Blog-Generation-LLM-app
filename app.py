import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os

# Function to get response from LLaMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # Local path to your model file (uploaded in repo under /models/)
    model_path = os.path.join("models", "llama-2-7b-chat.ggmlv3.q8_0.bin")

    # Load LLaMA model
    llm = CTransformers(
        model=model_path,
        config={"max_new_tokens": 512, "temperature": 0.7}
    )

    # Prompt template
    template = """
    Write a blog for a {blog_style} job profile on the topic "{input_text}",
    within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    # Format and send prompt
    final_prompt = prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    )

    response = llm(final_prompt)
    return response


# Streamlit App UI
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Blogs 🤖")

# Inputs
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns(2)
with col1:
    no_words = st.text_input("No. of Words")
with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People"),
        index=0
    )

submit = st.button("Generate")

# Final Output
if submit:
    if input_text and no_words:
        try:
            with st.spinner("Generating your blog..."):
                output = getLLamaresponse(input_text, no_words, blog_style)
                st.success("Here's your blog:")
                st.write(output)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please fill in all the fields.")
