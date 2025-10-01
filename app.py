# app.py
import streamlit as st
import pandas as pd
from pathlib import Path

# Load CSV (ensure filenames match)
DATA_DIR = Path(".")
yoruba_csv = DATA_DIR / "yoruba_emoji.csv"
emoji_csv = DATA_DIR / "emoji_to_yoruba.csv"

# Page Configuration
st.set_page_config(page_title="Bi-Directional Yoruba ↔ Emoji Translator",
                   page_icon="🌟",
                   layout="centered")

# Banner
st.image("banner.png", use_container_width=True)

# Sidebar (About Author)
st.sidebar.image("author.jpg.PNG", caption="👤 Samuel Babatunde Adedeji", use_container_width=True)
st.sidebar.markdown("### 📧 Contact Information")
st.sidebar.write("✉️ *Email:* [badedeji190@gmail.com](mailto:badedeji190@gmail.com)")
st.sidebar.write("🐙 *GitHub:* [yoruba-emoji-translation](https://github.com/SamuelAdedeji190/yoruba-emoji-translation)")
st.sidebar.write("🔗 *LinkedIn:* [Babatunde Adedeji](http://linkedin.com/in/babatunde-adedeji-7157b9253)")

# File checks
if not yoruba_csv.exists() or not emoji_csv.exists():
    st.sidebar.error("⚠️ Missing CSV files. Place *yoruba_emoji.csv* and *emoji_to_yoruba.csv* in the same folder as app.py.")
else:
    df_yoruba = pd.read_csv(yoruba_csv)
    df_emoji = pd.read_csv(emoji_csv)

    # Dictionaries
    yoruba_to_emoji = {str(k).strip().lower(): str(v).strip()
                       for k, v in zip(df_yoruba["Yoruba"], df_yoruba["Emoji"])}
    emoji_to_yoruba = {str(row["Emoji"]).strip(): [w.strip() for w in str(row["Yoruba"]).split(" / ")]
                       for _, row in df_emoji.iterrows()}

    # Translation Functions
    def yoruba_to_emoji_translate(text: str) -> str:
        if not text:
            return "🤔 (No input)"
        key = text.strip().lower()
        return yoruba_to_emoji.get(key, "🤔 (No emoji found)")

    def emoji_to_yoruba_translate(text: str) -> str:
        if not text:
            return "🤔 (No input)"
        key = text.strip()
        vals = emoji_to_yoruba.get(key)
        if vals:
            return " / ".join(vals)
        return "🤔 (No Yoruba mapping found)"

    # Main UI
    col_logo, col_title = st.columns([1, 5])
    with col_logo:
        st.image("ui_logo.png.png", width=80)
    with col_title:
        st.title("🌟 Bi-Directional Yoruba ↔ Emoji Translator 🌟")

    st.markdown("Enter a *Yoruba word* or an *emoji sequence* and choose a direction. Click *Translate* to get results instantly.")

    # Direction selector
    direction = st.radio("Select translation direction:", ["Yoruba → Emoji", "Emoji → Yoruba"])

    # Input field
    text_input = st.text_input("Enter your text or emoji sequence here:")

    # Translate button
    if st.button("Translate"):
        if direction == "Yoruba → Emoji":
            result = yoruba_to_emoji_translate(text_input)
        else:
            result = emoji_to_yoruba_translate(text_input)

        st.subheader("✅ Translation Result")
        st.code(result, language="")
   
    # Quick Examples
    st.markdown("---")
    st.subheader("⚡ Quick Examples")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Example: Inú mi dùn gan →"):
            st.write("Input: Inú mi dùn gan")
            st.code(yoruba_to_emoji_translate("Inú mi dùn gan"))
        if st.button("Example: Mo fẹ́ jẹun →"):
            st.write("Input: Mo fẹ́ jẹun")
            st.code(yoruba_to_emoji_translate("Mo fẹ́ jẹun"))

    with col2:
        if st.button("Example: 🙂❤️ →"):
            st.write("Input: 🙂❤️")
            st.code(emoji_to_yoruba_translate("🙂❤️"))
        if st.button("Example: 🍽️🍲 →"):
            st.write("Input: 🍽️🍲")
            st.code(emoji_to_yoruba_translate("🍽️🍲"))
    
    # Dataset Transparency
    st.markdown("---")
    if st.checkbox("📂 Show Yoruba→Emoji dataset"):
        st.dataframe(df_yoruba, use_container_width=True)

    if st.checkbox("📂 Show Emoji→Yoruba dataset"):
        st.dataframe(df_emoji, use_container_width=True)
   
    # Footer
    st.markdown("---")

    st.caption("🚀 Developed by *Samuel Babatunde Adedeji* | Yoruba ↔ Emoji Translator | CSV-driven rule-based NLP project.")
