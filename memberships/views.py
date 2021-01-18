from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserMembership
from .forms import UserMembershipForm

from checkout.models import Order


def membership(request):
    ''' Display the user's membership page '''
    membership = get_object_or_404(UserMembership, user=request.user)

    if request.method == 'POST':
        form = UserMembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(
                             request,
                             'Your details have been updated successfully'
                             )
        else:
            messages.error(
                           request,
                           'Unable to update info - please check for errors'
                           )
    form = UserMembershipForm(instance=membership)
    orders = membership.orders.all()

    template = 'memberships/membership.html'
    context = {
        'form': form,
        'orders': orders,
        'on_membership_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_membership': True,
    }

    return render(request, template, context)
