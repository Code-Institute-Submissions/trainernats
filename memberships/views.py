from django.shortcuts import render


def membership(request):
    """ Display the users membership """

    template = 'memberships/membership.html'
    context = {}

    return render(request, template, context)
