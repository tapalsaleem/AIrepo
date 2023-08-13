import os
import openai
import gradio as gr
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
#openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = 'https://tapalsaleemai2.openai.azure.com/' # Add your endpoint here
openai.api_key = 'ef3ed9da5a4f4b5696053eb41b07a0f4'  # Add your api key here

start_sequence = "\nAI"
restart_sequence = "\nHuman"

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

def openai_create(prompt):
    conversation.append({"role": "user", "content": prompt})
    response:str = openai.ChatCompletion.create(
        engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-turbo or GPT-4 model.
        messages=conversation,
        temperature=0.7,
         max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
    )
    return response["choices"][0]["message"]["content"]

def conversation_history(input, history):
    history = history or []
    s = list(sum(history,()))
    s.append(input)
    #inp = ''.join(s)
    output = openai_create(input)
    #print("check output",output)
    history.append((input,output))
    return history, history

blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
   # message = gr.Textbox(placeholder=conversation)
    message = gr.Textbox(placeholder=" ")
    state = gr.State()
    submit = gr.Button("prompt")
    submit.click(conversation_history,inputs=[message,state],outputs=[chatbot,state])
    
blocks.launch(debug=True)


    



