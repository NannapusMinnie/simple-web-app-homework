from mistralai import Mistral

import dotenv
import os

dotenv.load_dotenv() 

# Initialize ClientZ
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

# Make the API call
def text_to_expression(user_text):
    prompt = f"""
        Convert the user's request into plotting parameters.

        Return ONE LINE in this exact format:
        expression ; a ; b ; color

        Rules:
        - Use variable x
        - Use math module if needed
        - a and b must be numbers
        - If interval not given, use 0 and 10
        - If color not given, use blue
        - NO extra text

        Examples:
        "sine wave" -> math.sin(x); 0; 10; blue
        "red cosine from 0 to 5" -> math.cos(x); 0; 5; red
        "x squared from -2 to 2" -> x**2; -2; 2; blue

        User request:
        {user_text}
        """
            
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    try:
        expr, a, b, color = [x.strip() for x in result.split(";")]
        a = float(a)
        b = float(b)
    except Exception:
        raise ValueError(f"Invalid LLM output: {result}")

    return expr, a, b, color