from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    text1 = text.replace(' ','')
    sptext = text.split()
    return render(request, 'result.html', {
        'text' : text,
        'total_len' : total_len,
        'no_blank_len' : len(text1),
        'word_len' : len(sptext),
    })