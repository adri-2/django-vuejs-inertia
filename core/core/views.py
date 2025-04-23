# views.py
from inertia import render

def dashboard(request):
    return render(request, "Dashboard", props={
        "user": request.user.username,
        "notifications": 5,
    })
