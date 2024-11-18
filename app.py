import streamlit as st

def configure_interfaxe():
    st.title("Fake Docs")
    input_arquivo = st.file_uploader("Escolha um arquivo", type=['png', 'jpg', 'jpeg'])
    
    if input_arquivo is not None:
        file_name = input_arquivo.name
        
        blob_url = ''
        if blob_url:
            st.success('arquivo enviado com sucesso')
            credit_card_info = ''
            show_image_validation(blob_url, credit_card_info)
        else:
            st.warning('Erro ao enviar arquivo')
            
def show_image_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_column_width=True)
    st.write("Informações de cartão de crédito encontradas:")
    st.write(credit_card_info)




configure_interfaxe()