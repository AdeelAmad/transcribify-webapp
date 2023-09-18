from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import stripe
from django.views.decorators.csrf import csrf_exempt

from .models import customer

stripe.api_key = ""
endpoint_secret = ""

@login_required
def billing(request):
    customer_id = customer.objects.get(user=request.user).stripe_id
    session = stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url='http://transcribify.xyz/',
    )
    return redirect(session.url)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        event = None
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the checkout.session.completed event
        if event['type'] == 'customer.subscription.updated':
            user = customer.objects.get(stripe_id=event['data']['object']['customer']).user

            new_plan = event['data']['object']['items']['data'][0]['plan']['product']

            if new_plan == "":
                user.groups.add(1)
            elif new_plan == "":
                user.groups.remove(1)

        return HttpResponse(status=200)
    else:
        return redirect('upload')
