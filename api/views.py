from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from api.models import BlogApi
from api.serializers import BlogSerializer

@csrf_exempt
def blog_list(request):
	try:
		blog = BlogApi.objects.all()
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)

	if request.method == "GET":
	    blogs = BlogApi.objects.all()
	    ser = BlogSerializer(blogs, many=True)
	    return JsonResponse(ser.data, safe=False)
	elif request.method == "POST":
		data = JSONParser().parse(request)
		ser = BlogSerializer(data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
		return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def blog_detail(request, blog_id):
	try:
		blog = BlogApi.objects.get(id=blog_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=400)

	if request.method == "GET":
		ser = BlogSerializer(blog)
		return JsonResponse(ser.data, safe=False)
	elif request.method == "PUT":
		data = JSONParser().parse(request)
		ser = BlogSerializer(blog, data=data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
	elif request.method == "DELETE":	
		blog.delete()
		ser = BlogSerializer(blog)
		return JsonResponse(ser.data, safe=False)
# Create your views here.
