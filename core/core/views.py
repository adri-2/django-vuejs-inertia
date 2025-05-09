from inertia import render
# from .models import Event

def index(request):
  return render(request, 'Index', props={'events': "Django+inertia+vue"})

# def home(request):
#   return render(request, 'Index', props={'events': "Django+inertia+vue home"})