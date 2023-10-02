import google.generativeai as palm #uses Palm LLM by Google

# Function to use Palm API 
def custom_chatbot(user_input):
    
    palm.configure(api_key='API KEY')
    #Use Palm API Key
    
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    
    prompt = user_input

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )

    return(completion.result)