from django.shortcuts import redirect

def is_loggedin(viewfunc):
    def wrapperfunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return viewfunc(request, *args, **kwargs)
    return wrapperfunc
