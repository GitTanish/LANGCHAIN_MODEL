from langchain_groq import ChatGroq # The main LLM wrapper for Groq
from dotenv import load_dotenv      # tO lOad the API key from my .env file
import streamlit as st              # simple ui        
load_dotenv()                       # Load this before I init the model
from langchain_core.prompts import PromptTemplate, load_prompt # 'load_prompt' is the key here

# --- Model and UI Setup ---

# Init the model. Using gpt-oss 'cause it's solid.
# Temp is high (0.9) for more creative/less robotic explanations.
# Max tokens cranked to 5000 to handle the "Long" detailed requests.
model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.9, max_tokens=5000)

# Simple title
st.header('Dunder Mifflin Summary Company')

# --- User Inputs ---
# These 3 selectboxes will provide the variables for the prompt.
paper_input = st.selectbox(
    "Select Research Paper Name", ["Select...",
        "Attention is All You Need", "BERT: Pre-Training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"
        ])

style_input = st.selectbox("Select Explanation Style",[
    "Begineer-Friendly","Technical ","Code-Oriented","Mathematical"
])


length_input = st.selectbox("Select Explanation Length",[
    "Short (1-2 paragraphs)","Medium (3-5 paragraph)","Long (detailed explanation)"
])


# --- Prompt Loading ---
# This is the whole point of making it modular.
# Instead of that massive hardcoded template string cluttering up this file,
# I just load the 'template.json'.
# That .json file is created and saved by my *other* script, 'prompt_generator.py'.
# Much cleaner.
template = load_prompt('template.json')

# --- App Logic ---

# Fill the loaded template with the values from the UI.
# The keys here ('paper', 'style', 'length') MUST match the
# # 'input_variables' I defined in the generator script.
# prompt = template.invoke({
#     'paper': paper_input,
#     'style':style_input,
#     "length":length_input
# })


if st.button('RUN'):
    chain = template | model
    result = chain.invoke({
    'paper': paper_input,
    'style':style_input,
    "length":length_input

    })
    if paper_input =='Select...':
        st.warning('Please Select a research paper first!')
    else:
# 3. NOW: Show the spinner *before* you do the slow work
        with st.spinner("Processing..."):
            
            # 4. Define the chain and do the SLOW part (the API call)
            #    *inside* the spinner
            chain = template | model
            result = chain.invoke({
                'paper': paper_input,
                'style': style_input,
                "length": length_input
            })
            
            # 5. NOW: Write the result. The spinner will automatically stop.
            st.write(result.content)