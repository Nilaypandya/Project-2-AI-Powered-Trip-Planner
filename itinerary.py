from groq import Groq
from dotenv import load_dotenv
from rag import retrieve_data
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_itinerary(destination, days, budget, vibe, season):

    retrieved_data = retrieve_data(destination)

    prompt = f"""
    Use this travel information:

    {retrieved_data}

    Create a {days}-day travel itinerary for {destination}.

    Travel vibe: {vibe}

    Season: {season}

    Total budget: ₹{budget}

    Also include:
    - local festivals
    - seasonal attractions
    - famous local food
    - adventure or cultural activities
    - budget-friendly recommendations

    Return:
    1. Day-wise itinerary
    2. Budget travel tips
    3. Festival recommendations
    4. Seasonal recommendations
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content