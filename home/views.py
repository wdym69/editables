from django.shortcuts import render, HttpResponse 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  return HttpResponse("this is a home page")

def index(request):
  return render(request, 'display_text.html')
  # return HttpResponse("this is a home page")

def get_text_file(request):
    # Read the text file and return its contents as a response
    with open('translated_text.txt', 'r', encoding='utf-8') as file:
        text_content = file.read()
    return HttpResponse(text_content, content_type='text/plain')

@csrf_exempt  # Consider CSRF protection for production use
def save_text_file(request):
    if request.method == "POST":
        try:
            edited_text = request.body.decode("utf-8")  # Decode the text data
            with open('translated_text.txt', 'w', encoding='utf-8') as file:
                file.write(edited_text)  # Write the edited text back to the file
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=405)