from inertia import render
# from .models import Event

def index(request):
  return render(request, 'Index', props={'tevents': "django xhello"})