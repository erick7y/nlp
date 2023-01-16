'''
Este script aplica conceitos básicos de NLP (natural language processing).
'''

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

lemma = WordNetLemmatizer()

def tokenize(text):
  '''
  Tokeniza o texto.
  '''
  return word_tokenize(text)

def remove_punctuation(tokens):
  '''
  Remove os tokens de pontuação.
  '''
  return [word for word in tokens if word.isalpha()]

def to_lower_case(tokens):
  '''
  Converte todos os tokens para letras minúsculas.
  '''
  return [word.lower() for word in tokens]

def remove_stop_words(tokens):
  '''
  Remove todos os tokens que representam palavras de parada.
  '''
  return [word for word in tokens if not word in stopwords.words("english")]

def normalize(tokens):
  '''
  Normaliza os tokens.
  '''

  '''
  Verbos.
  '''
  i = 0
  tokens_length = len(tokens)
  while i < tokens_length:
    tokens[i] = lemma.lemmatize(tokens[i], pos='v')
    i += 1

  '''
  Substantivos.
  '''
  i = 0
  tokens_length = len(tokens)
  while i < tokens_length:
    tokens[i] = lemma.lemmatize(tokens[i], pos='n')
    i += 1

  return tokens

if __name__ == '__main__':
  text = '''A corpus is a collection of authentic text or audio organized into datasets. Authentic here means text written or audio spoken by a native of the language or dialect. A corpus can be made up of everything from newspapers, novels, recipes, radio broadcasts to television shows, movies, and tweets.'''

  tokens = tokenize(text)
  tokens = remove_punctuation(tokens)
  tokens = to_lower_case(tokens)
  tokens = remove_stop_words(tokens)
  tokens = normalize(tokens)

  print(tokens)
