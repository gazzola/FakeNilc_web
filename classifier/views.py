from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from preprocess import bow, pos
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

#supress some warnings about type conversion
import warnings
with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	from nlpnet import POSTagger
tagger = POSTagger(r'var/nlpnet', language='pt')

vocabulary = joblib.load('var/vocabulary.pkl')
uni_clf = joblib.load('var/linearsvc_unigram-binary.pkl')
pos_clf = joblib.load('var/linearsvc_pos.pkl')

@require_http_methods(['POST'])
def check(request):
	text = request.POST['text']
	model = request.POST['model']

	# vectorizing received text
	if(model == 'pos'):
		vec = pos.vectorize(text, tagger)
		res = pos_clf.predict(vec.values)
	else:
		vec = bow.vectorize(text,vocabulary[:-1])
		res = uni_clf.predict(vec.values)

	# predicting
	#returning a response with prediction result
	data = {'result': res[0]}
	return JsonResponse(data)


def classif(request):
    return render(request, 'classif.html', {'resultado': False})	


def about(request):
	return render(request, 'about.html')	