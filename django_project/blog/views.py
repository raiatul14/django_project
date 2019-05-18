from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
			{
				'author' : 'Atul Rai',
				'title' : 'Blog Post',
				'content' : 'First Post',
				'date_posted' : '18 May 2019'
			},
			{
				'author' : 'Prime Suspect',
				'title' : 'Blog Post-1',
				'content' : 'Second Post',
				'date_posted' : '19 May 2019'
			},
		]
def home(request):
	context={
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)
def about(request):
	return render(request, 'blog/about.html', {'title':'About'})