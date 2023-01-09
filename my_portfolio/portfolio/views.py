from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os


def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'message': message,
        }
        message = '''
                New message: {}
                From: {}
                '''.format(data['message'], data['email'])
        subject = None

        send_mail(subject, message, '', ['reni91boyanova@gmail.com'])
        return redirect('index page')
    else:
        request.session['view_counter'] +=1

    context = {
        'number_of_views': request.session['view_counter']
    }

    return render(request, 'index.html', context)


def download_resume(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Reni Boyanova Resume.pdf'
    filepath = base_dir + '/download_file/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(thefile)[0])

    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Description'] = f'Attachement;{filename}'
    return response


