import gradio as gr
from tag import tag_urdu_sentence


with gr.Blocks() as demo:
    gr.Markdown("## 🏷️ Urdu Part-of-Speech Tagger")
    gr.Markdown("Enter an Urdu sentence below to see word-level POS tags:")

    with gr.Row():
        with gr.Column():
            sentence_input = gr.Textbox(
                label="Input Urdu Sentence", placeholder="مثال: آج موسم اچھا ہے"
            )
            submit_btn = gr.Button("Tag Sentence")
        with gr.Column():
            output_table = gr.Dataframe(
                headers=["Word", "PoS Tag"],
                datatype=["str", "str"],
                label="Tagged Output",
            )

    submit_btn.click(fn=tag_urdu_sentence, inputs=sentence_input, outputs=output_table)

demo.launch()
