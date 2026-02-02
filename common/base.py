import base64
import streamlit as st

def _img2str(imageLoc):
    with open(imageLoc,'rb') as f:
        img_bytes = f.read()
    base64_str = base64.b64encode(img_bytes).decode("utf-8")
    return base64_str

def st_image(imageLoc):
    img_str = _img2str(imageLoc)
    st.markdown(
        f'<img src="data:image/jpg;base64,{img_str}" style="width:100%; max-width:800px;">',
        unsafe_allow_html=True
    )
    # image_bytes = base64.b64decode(img_str)
    # img_obj = Image.open(BytesIO(image_bytes))
    # st.image(img_obj)

def stylePage(width:int,defaultMAPI:str=None):
    st.set_page_config(initial_sidebar_state='collapsed')
    css_StrA = """
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                max-width: """
    css_StrB = """px;
                margins: 0;
            }
            .st-emotion-cache-tn0cau {
                gap : 0.3rem;    
            }
            hr { 
                border: none;
                height: 2px;
                margin: 1rem;
            }
            .st-emotion-cache-4rsbii {
                display : block;
            }


        </style>
    """
    finalStr = css_StrA+str(width)+css_StrB
    st.markdown(finalStr, unsafe_allow_html=True)

    mapi_key = st.query_params.get("mapiKey",defaultMAPI)
    
    if 'mapiKey' not in st.session_state:
        st.session_state['mapiKey'] = mapi_key

    if not mapi_key:
        
        st.markdown(
                """
                <div style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-size: 15px;
                    font-weight: 400;
                ">
                    ⚠️ Please check the API connection of CIVIL NX and restart the plugin
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # st.warning('Please check the API connection of CIVIL NX and restart the plugin')
        st.stop()