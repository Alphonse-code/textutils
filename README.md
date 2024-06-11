# TextUtils

TextUtils est une bibliothèque Python pour la manipulation de texte. Elle permet de nettoyer du texte, de compter les mots, de supprimer les stop words et de lemmatiser le texte.

# exemple d'utilisation de la bibliothèque
```python
from textutils.processing import clean_text, word_count, remove_stopwords, lemmatize_text

text = "This is a sample text, with stopwords and various forms of words."

cleaned_text = clean_text(text)
print("Cleaned Text:", cleaned_text)

count = word_count(cleaned_text)
print("Word Count:", count)

no_stopwords = remove_stopwords(cleaned_text)
print("Text without Stopwords:", no_stopwords)

lemmatized = lemmatize_text(no_stopwords)
print("Lemmatized Text:", lemmatized)
