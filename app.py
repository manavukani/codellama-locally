import requests
import json
import gradio as gr

# API endpoint URL
url="http://localhost:11434/api/generate"

# Headers for the HTTP request
headers={

    'Content-Type':'application/json'
}

# Keep track of input prompts
history=[]

def generate_response(prompt):
    history.append(prompt)
    new_prompt="\n".join(history)

    # Data to be sent in the request
    data={
        "model":"codehelper",
        "prompt":new_prompt,
        "stream":False
    }
    
    # Send POST request to the API endpoint
    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("Error:",response.text)


# Create Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, label="Enter your prompt here", placeholder="Enter your Prompt"),
    outputs=gr.Textbox(label="Generated Code", placeholder="Generated code will appear here."),
    title="Code Generation",
    description="This tool generates code based on your prompt using a pre-trained model.",
    theme="compact",
    layout="vertical",
    capture_session=True,
    allow_flagging=False
)

# Launch the interface
interface.launch()
