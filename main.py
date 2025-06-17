import os
import sys
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():

    load_dotenv()

    # Create an argparse object to check for arguments and flags
    parser = argparse.ArgumentParser(
        prog="AI-Agent",
        description="Toy version of Claude Code using Google's Gemini API"
    )
    parser.add_argument("user_prompt")
    parser.add_argument("--verbose",
                        action="store_true")

    # Gather command line arguments - if no arguments, exit with status code 1
    args = parser.parse_args()
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    # Load API key from environment variable
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create new instance of Gemini client
    client = genai.Client(api_key=api_key)

    # Store user prompt in a list
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)]),
    ]

    # Call function to generate content based on client and command prompt arguments
    generate_content(client, messages, args)


# Function to handle generating content
def generate_content(client, messages, args):

    # Generate a response from gemini-2.0-flash-001 model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )
    if args.verbose:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Print response to console
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()