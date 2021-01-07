from django.shortcuts import render, get_object_or_404
from .models import TNS_Class


# Create your views here.
def all_classes(request):
    ''' A view to show all available classes '''

    all_classes = TNS_Class.objects.all()

    context = {
        'all_classes': all_classes,
    }

    return render(request, 'tnsclasses/classes.html', context)


def class_detail(request, class_id):
    ''' A view to show an individual class '''

    the_class = get_object_or_404(TNS_Class, pk=class_id)

    context = {
        'the_class': the_class,
    }

    return render(request, 'tnsclasses/class_detail.html', context)
