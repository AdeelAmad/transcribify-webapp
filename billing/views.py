from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import stripe
from .models import customer

stripe.api_key = "sk_test_51Mm4ynEJU8eUpQthxXeVWS6odrkxdZCBrWS9VAHlvDkD20BMq8IeY3yTJJumsvFudGNRB5u24oDIs3K3abytAJvN0083aRyWdN"


@login_required
def billing(request):
    customer_id = customer.objects.get(user=request.user).stripe_id
    session = stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url='http://127.0.0.1:8000/',
    )
    return redirect(session.url)