from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import NewTopicForm
from .models import Board, Topic, Post

def home(request):
	boards = Board.objects.all()
	
	return render(request, 'home.html', {'boards' : boards})


def board_topics(request, pk):
	try:
		board = get_object_or_404(Board, pk=pk)
	except Board.DoesNotExist:
		raise HTTP404
	return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user = User.objects.first()
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save()
			return redirect('board_topics', pk=board.pk)
	else:
		form = NewTopicForm()
	return render(request, 'new_topic.html', {'form': form})