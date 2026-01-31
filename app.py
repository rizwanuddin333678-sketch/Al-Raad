import gradio as gr

def greet(name):
    return f"Hello {name}! Welcome to my AI Portfolio 🚀"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Al-Raad AI Portfolio",
    description="My first Hugging Face Space"
)

demo.launch()
