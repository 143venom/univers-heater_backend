from rest_framework import viewsets
from rest_framework import status
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name", "description"]
    lookup_field = "slug"


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        site_owner_subject = "New Order Received"
        site_owner_message = render_to_string(
            "order_notification.html", {"order": order}
        )
        site_owner_recipient_list = [settings.SITE_OWNER_EMAIL]
        site_owner_reply_to = [settings.DEFAULT_REPLY_TO_EMAIL]
        try:
            send_mail(
                site_owner_subject,
                site_owner_message,
                settings.DEFAULT_FROM_EMAIL,
                site_owner_recipient_list,
                reply_to=site_owner_reply_to,
                html_message=site_owner_message,
            )
        except Exception as e:
            print(f"Failed to send email to site owner: {e}")
        if order.user and order.user.email:
            subject = "Order Confirmation"
            message = render_to_string("order_confirmation.html", {"order": order})
            recipient_list = [order.user.email]
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list,
                    html_message=message,
                )
            except Exception as e:
                print(f"Failed to send email to user {order.user.email}: {e}")
