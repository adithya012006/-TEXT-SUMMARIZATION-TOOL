import spacy
from heapq import nlargest

def summarize_text(text, summary_length=3):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    word_freq = {}
    for token in doc:
        if token.is_alpha and not token.is_stop:
            word = token.text.lower()
            word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word.text.lower()]

    summary_sentences = nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary = " ".join([sent.text for sent in summary_sentences])
    return summary

if _name_ == "_main_":
    long_text = """Replace this with your lengthy article text. The tool will process the text and provide a concise summary using NLP techniques like word frequency analysis and sentence ranking."""
    print("Original Text:\n", long_text)
    print("\nSummary:\n", summarize_text(long_text))
