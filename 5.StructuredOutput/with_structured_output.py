from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b', temperature=0.9,)


# schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review list"]
    summary: Annotated[str, "write a summary within 100 words"]
    sentiment: Annotated[str, "Return Sentiment of the review either negative positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the postitive points"]
    cons: Annotated[Optional[list[str]], "Write down all the negative points"]

structured_model =model.with_structured_output(Review)

review_text = """

"""

result = structured_model.invoke("""
This is a Review:
Yoshiyuki Sadamoto's Neon Genesis Evangelion manga is an analytical marvel, not because it's a faithful adaptation, but precisely because it isn't. It's a parallel narrative, a deliberate and meticulous 14-year dialogue with Hideaki Anno's seminal, chaotic masterpiece. Where the anime was a raw, psycho-analytic scream broadcast through a lens of 'monster-of-the-week' deconstruction, Sadamoto's manga is a quieter, more terrestrial tragedy, recasting the story as a character-focused humanist drama rather than an abstract-expressionist event.
its quest for narrative coherence and character clarity, it demystifies some of the anime's most potent, abstract horror. It provides answers where Anno offered only questions. The result is an ending that is definitive, concrete, and deeply melancholic, but it lacks the boundary-pushing, fourth-wall-shattering audacity of The End of Evangelion.
""") # returns json in python looks like dictionary


print(result['summary'])
print(f"Sentiment: "+result['sentiment']) 
print(result['pros'])
print(result['cons'])