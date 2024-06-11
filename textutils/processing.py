# textutils/processing.py

import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    """
    Nettoie le texte en le convertissant en minuscules, en supprimant les caractères non alphabétiques
    et en supprimant les espaces superflus.

    Args:
        text (str): Le texte à nettoyer.

    Returns:
        str: Le texte nettoyé.
    """
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text.strip()

def word_count(text):
    """
    Compte la fréquence de chaque mot dans le texte.

    Args:
        text (str): Le texte dont les mots doivent être comptés.

    Returns:
        collections.Counter: Un compteur des mots avec leur fréquence.
    """
    words = text.split()
    return Counter(words)

def remove_stopwords(text):
    """
    Supprime les stop words du texte.

    Args:
        text (str): Le texte dont les stop words doivent être supprimés.

    Returns:
        str: Le texte sans stop words.
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def lemmatize_text(text):
    """
    Lemmatiser chaque mot dans le texte.

    Args:
        text (str): Le texte à lemmatiser.

    Returns:
        str: Le texte lemmatisé.
    """
    lemmatizer = WordNetLemmatizer()
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)


text = "This is a sample text, with stopwords and various forms of words."

# Nettoyage du texte
cleaned_text = clean_text(text)
print("Cleaned Text:", cleaned_text)

# Comptage des mots
count = word_count(cleaned_text)
print("Word Count:", count)

# Suppression des stop words
no_stopwords = remove_stopwords(cleaned_text)
print("Text without Stopwords:", no_stopwords)

# Lemmatisation du texte
lemmatized = lemmatize_text(no_stopwords)
print("Lemmatized Text:", lemmatized)