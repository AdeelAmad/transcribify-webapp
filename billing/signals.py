from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import stripe
from .models import customer

stripe.api_key = "sk_test_51Mm4ynEJU8eUpQthxXeVWS6odrkxdZCBrWS9VAHlvDkD20BMq8IeY3yTJJumsvFudGNRB5u24oDIs3K3abytAJvN0083aRyWdN"

@receiver(post_save, sender=User)
def createCustomer(sender, instance, created, **kwargs):
    if created:
        c = stripe.Customer.create(
            email=instance.email,
            name=instance.username,
            metadata={"id": instance.id},
        )

        customer.objects.create(user=instance, stripe_id=c.id)

        stripe.Subscription.create(
            customer=c.id,
            items=[{"price": "price_1Mm5UhEJU8eUpQthWQKmrqhy"}],
        )