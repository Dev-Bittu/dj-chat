from django.shortcuts import render

# Create your views here.
def ws(request, group_name):
	return render(request, 'ws/index.html', {'group_name': group_name})