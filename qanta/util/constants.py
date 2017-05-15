import string

from nltk.corpus import stopwords

ENGLISH_STOP_WORDS = set(stopwords.words('english'))
QB_STOP_WORDS = {"10", "ten", "points", "tenpoints", "one", "name", ",", ")", "``", "(", '"', ']',
                 '[', ":", "due", "!", "'s", "''", 'ftp'}
STOP_WORDS = ENGLISH_STOP_WORDS | QB_STOP_WORDS

PUNCTUATION = string.punctuation
GUESSER_REPORT_FOLDS = ['dev', 'test']
BUZZ_FOLDS = ['dev', 'test', 'expo']
ALL_FOLDS = ['train', 'dev', 'test']

COUNTRY_LIST_PATH = 'data/internal/country_list.txt'

SENTENCE_STATS = 'output/guesser/sentence_stats.pickle'

CLM_PATH = 'output/language_model'
CLM_TARGET = 'output/language_model.txt'

GLOVE_WE = 'data/external/deep/glove.6B.300d.txt'

GUESSER_TARGET_PREFIX = 'output/guesser'

QB_SOURCE_LOCATION = 'data/internal/source'

COMPARE_GUESSER_REPORT_PATH = 'output/guesser/guesser_comparison_report_{}.pdf'

PRED_TARGET = 'output/predictions/{0}.pred'
META_TARGET = 'output/vw_input/{0}.meta'

EXPO_BUZZ = 'output/expo/{}.buzz'
EXPO_FINAL = 'output/expo/{}.final'
EXPO_QUESTIONS = 'output/expo/{}.questions.csv'

KEN_LM = 'output/kenlm.binary'
