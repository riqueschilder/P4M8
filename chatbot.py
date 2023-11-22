from transformers import GPT2LMHeadModel, GPT2Tokenizer
import gradio as gr

# Escolha um modelo diferente, por exemplo, GPT-2
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Defina o prompt de sistema para contextualizar as respostas
SYSTEM_PROMPT = "Em relação às normas de segurança em ambientes industriais, posso te ajudar com as seguintes informações:"

# Função para interagir com o modelo de linguagem
def interagir(prompt):
    input_text = SYSTEM_PROMPT + '\n' + prompt
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Geração de texto
    output = model.generate(input_ids, max_length=150, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

    return tokenizer.decode(output[0], skip_special_tokens=True)

# Crie a interface gráfica com gradio
iface = gr.Interface(fn=interagir, inputs="text", outputs="text")
iface.launch()
