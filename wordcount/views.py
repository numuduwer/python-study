from django.shortcuts import render

# Create your views here.
# render 함수는 3개까지 인자를받음
# 1번 인자 : 고정적으로 request를 받아주고
# 2번 인자 : template를 받아준다.
# 3번 인자 : 사전적(dictionary)형 객체를 받을 수 있다.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}
    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dic': word_dic.items()})
