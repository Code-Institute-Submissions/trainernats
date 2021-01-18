from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import TNS_Class, Day, TNS_Class
from .forms import TNS_ClassForm


# Create your views here.
def all_classes(request):
    ''' A view to show all available classes '''

    all_classes = TNS_Class.objects.all()

    context = {
        'all_classes': all_classes,
    }

    return render(request, 'tnsclasses/classes.html', context)


def class_detail(request, theclass_id):
    ''' A view to show an individual class '''

    theclass = get_object_or_404(TNS_Class, pk=theclass_id)

    context = {
        'theclass': theclass,
    }

    return render(request, 'tnsclasses/class_detail.html', context)


@login_required
def add_class(request):
    """ Add a class to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Only site administrators can add a new class')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = TNS_ClassForm(request.POST, request.FILES)
        if form.is_valid():
            theclass = form.save()
            messages.success(request, 'Successfully added a new class!')
            return redirect(reverse('class_detail', args=[theclass.id]))
        else:
            messages.error(request, 'Could not add this new class - please ensure the form is valid.')
    else:
        form = TNS_ClassForm()
        
    template = 'tnsclasses/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_class(request, theclass_id):
    """ Edit an existing class """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    theclass = get_object_or_404(TNS_Class, pk=theclass_id)
    if request.method == 'POST':
        form = TNS_ClassForm(request.POST, request.FILES, instance=theclass)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('class_detail', args=[theclass.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = TNS_ClassForm(instance=theclass)
        messages.info(request, f'You are editing {theclass.class_name}')

    template = 'tnsclasses/edit_class.html'
    context = {
        'form': form,
        'theclass': theclass,
    }

    return render(request, template, context)