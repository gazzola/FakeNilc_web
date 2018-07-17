from django.http import JsonResponse
from django.shortcuts import render

from preprocess import bow, pos
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

vocabulary = joblib.load('var/vocabulary.pkl')
uni_clf = joblib.load('var/linearsvc_unigram-binary.pkl')
pos_clf = joblib.load('var/linearsvc_pos.pkl')

def check(request):
	text = request.GET['text']
	model = request.GET['model']

	# vectorizing received text
	if(model == 'pos'):
		vec = pos.vectorize(text)
		res = pos_clf.predict(vec.values)
	else:
		vec = bow.vectorize(text,vocabulary[:-1])
		res = uni_clf.predict(vec.values)

	# predicting
	#returning a response with prediction result
	data = {'result': res[0]}
	return JsonResponse(data)


def index(request):
    return render(request, 'index.html', {'resultado': False})	