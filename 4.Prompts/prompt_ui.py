from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from langchain_core.prompts import PromptTemplate

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.9, max_tokens=5000)
st.header('Prompt Test')

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

# template
template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template= """You are a world-class AI research explainer with deep expertise in machine learning, natural language processing, and computer vision. Your mission is to decode complex research papers with clarity and precision.

# RESEARCH PAPER ANALYSIS TASK

**Paper:** {paper}
**Explanation Style:** {style}  
**Response Length:** {length}

---

## STYLE-SPECIFIC INSTRUCTIONS

### If Beginner-Friendly:
- Start with real-world analogies (e.g., "Think of attention mechanism like...")
- Define every technical term on first use
- Use progressive complexity: simple → intermediate concepts
- Include relatable examples from everyday technology
- Avoid equations unless absolutely necessary; explain intuition instead

### If Technical:
- Use precise ML/AI terminology without over-explanation
- Reference architectural components (layers, heads, parameters)
- Discuss training procedures, datasets, and benchmarks
- Compare with prior state-of-the-art methods
- Mention computational requirements and scalability

### If Code-Oriented:
- Focus on implementation details and data flow
- Include pseudocode for core algorithms (use proper indentation)
- Explain how to translate concepts into PyTorch/TensorFlow
- Mention key libraries and functions needed
- Discuss practical engineering considerations (memory, speed)

### If Mathematical:
- Present formal definitions and theorems
- Show key equations with proper notation
- Explain mathematical intuition behind formulas
- Discuss complexity analysis (time/space)
- Connect mathematical properties to model behavior

---

## LENGTH GUIDELINES

**Short (1-2 paragraphs):**  
Extract the single core innovation. One paragraph for context + problem, one for solution + impact. Be ruthlessly concise.
Important: For Short length, ignore the 5-point MANDATORY STRUCTURE and strictly follow the 2-paragraph format described above.

**Medium (3-5 paragraphs):**  
"Follow the 5-point MANDATORY STRUCTURE.
1. Hook: Keep to a single sentence.
2. Problem Context: 1 paragraph.
3. Core Innovation: 1-2 paragraphs.
4. Technical Deep-Dive: 1 paragraph.
5. Impact Statement: 1 paragraph."
Important: for Medium keep technical deep-dive concise.

**Long (detailed explanation):**  
Comprehensive breakdown covering:
1. Hook: Keep to a single sentence.
2. Problem Context: 1 paragraph.
3. Core Innovation: 1-2 paragraphs.
4. Technical Deep-Dive: you must provide a comprehensive breakdown. This section should include: [Historical context, Previous approaches, Detailed methodology and architecture, Experimental setup, etc...]
5. Impact Statement: 1 paragraph."
---

## MANDATORY STRUCTURE

1. **Hook:** Start with a one-sentence summary of why this paper matters
2. **Problem Context:** What challenge does it solve? Why did it exist?
3. **Core Innovation:** The paper's main contribution (be specific)
4. **Technical Deep-Dive:** Methodology adapted to chosen style
5. **Impact Statement:** Why this changed the field

---

## QUALITY REQUIREMENTS

✓ Ground every claim in the paper's actual contributions  
✓ Highlight the "aha moment" that makes this paper special  
✓ Use concrete examples, not abstract descriptions  
✓ If Mathematical style: Format equations clearly  
✓ If Code-Oriented: Show actual implementation logic  
✓ End with a memorable takeaway that captures the essence  

---

Begin your explanation now.""",
validate_template=True,
)
  
prompt = template.invoke({
    'paper': paper_input,
    'style':style_input,
    "length":length_input
})

if st.button('RUN'):
   
   result=model.invoke(prompt)
#    print(result.content)
   st.markdown(result.content)
