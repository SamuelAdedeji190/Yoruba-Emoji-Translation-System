# Yoruba-Emoji-Translation-System
Bi-directional Yoruba ↔ Emoji machine translation system built with Python and Streamlit. First of its kind, developed as a postgraduate project using hybrid NLP methods.
Yoruba ↔ Emoji Translator

A bi-directional Yoruba ↔ Emoji machine translation system built with Python and Streamlit. This is the first of its kind, developed as a postgraduate project using hybrid NLP techniques.
## Features:
	•	Translate Yoruba text into Emojis and vice versa.
	•	Bi-directional translation: Yoruba ↔ Emoji.
	•	Built with Python and an interactive Streamlit app.
	•	Implements hybrid NLP methods for accurate translations.
	•	User-friendly interface suitable for research and demonstration.
 
  ## Tech Stack
- Python (pandas, scikit-learn)
- Streamlit (web interface)
- CSV Dataset for scalability and transparency

## Dataset
- Yoruba → Emoji mappings (`yoruba_emoji_100.csv`)
- Emoji → Yoruba mappings (`emoji_to_yoruba_100.csv`)

## Example entries:
| Yoruba | Emoji |
|-------------|---------|
| inú mi dùn | 😀 |
| ọmọ | 👶 |
| ọjọ́ | 📅 |


## Accuracy
- Yoruba → Emoji: **95%**
- Emoji → Yoruba: **92%**
- Evaluated on a curated 100-word dataset + human feedback.

##  Demo
👉 Streamlit App Link: https://yoruba-emoji-translation-system-ck7vzjfvwyewhzypzkvf3g.streamlit.app/

## Run locally with:
bash
streamlit run app.py
