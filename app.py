import gradio as gr
import utility as ut
def selectLanguage(EnterText,selectLanguage):
    res= ut.translateIt(EnterText,"English",selectLanguage)
    return res.content
    
with gr.Blocks() as demo:

    gr.Interface(
        title="I am a language translator",
        fn=selectLanguage,    
        inputs=["text",gr.Radio(["Hindi","French","Spanish"])],
        outputs=["text"],
    )
    gr.Markdown("<p style='color:white;'>Created By: <span style ='color:yellow;'>Sunny Kumar</span>.</p>")
    gr.Markdown("<p style='color:white;'>Contact me at: <span style ='color:yellow;'>SunnyKumar1516@gmail.com</span>.</p>")
    gr.Markdown("<p style='color:white;'>Linkdin: <span style ='color:yellow;'>https://www.linkedin.com/in/sunny-kumar-b232417a/</span>.</p>")
    
demo.launch()
