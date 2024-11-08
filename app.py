import gradio as gr
import utility as ut
def selectLanguage(EnterText,selectLanguage):
    res= ut.translateIt(EnterText,"English",selectLanguage)
    return res.content
demo = gr.Interface(
   
    title="I am a language translator",
    fn=selectLanguage,
    
    inputs=["text",gr.Radio(["Hindi","French","Spanish"])],
    outputs=["text"],


)

demo.launch()