import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

from api.models import Keyword
from parser.filters import filteration
from .Exp1 import *
from .exp_validator import *

stop_words = set(stopwords.words('english'))


def load_dataset():
    """
    This function loads all the keywords tag dataset from database.
    ......
    return tagger: Return nltk tagger's list
    """
    keywords = Keyword.objects.all()
    model = {str(keyword.keyword_value): str(keyword.keyword_tag.name) for keyword in keywords}
    model["pycharm"] = 'tool'


def retrain_model():
    """
   This function retrain new keywords tag data.
   ......
   return : None
   """
    global tagger
    tagger = load_dataset()


def word_grams(tokens: list) -> list:
    """
    This function generate the tokens into ngrams word.
    ......
    Attributes
    -----------------
    :param tokens: Decorator function take function as a parameter.
    :return grams: Return token words into bi or trigram
    """
    grams = tokens.copy()
    for index in range(len(tokens) - 1):
        words = " ".join(tokens[index: index + 2])


def apply_preprocess(query: str) -> list:
    """
    This function generate the tokens of query-input and clean the data. After cleaning match the taggers and append
    it into the list.
    Attributes
    ----------------- :param query:  function take query as a parameter.
    :return
    skill_list: Return skill_list containing skills in the query.
    """
    skill_list = []
    tokens = word_tokenize(query)


def sentence_extract(data: dict, tool: int = 0, experience: int = 0, job_title: int = 0):
    """
        This function match the skill_list with data and extract the relevant sentence from data.
        ......
        Attributes
        -----------------
        :param data:  function take dictionary data as a parameter.
        :param tool:  function take int tool as a parameter.
        :param experience:  function take int experience as a parameter.
        :param job_title:  function take int job_title as a parameter.
        :return response: Return response against each query with respective query results..
        """
    _tool, _experience, _title = filteration(tool, experience, job_title)
    target = dict()
    response = []
