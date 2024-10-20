from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError





class Product(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    product_image = models.ImageField(
        upload_to="shop/product_image", blank=True, null=True
    )
    stock_quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            existing_product = Product.objects.get(pk=self.pk)
            if existing_product.name != self.name:
                self.slug = slugify(self.name)
        else:
            if not self.slug and self.name:
                self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Product"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the order is being updated
            existing_order = Order.objects.get(pk=self.pk)
            if existing_order.product != self.product or existing_order.quantity != self.quantity:
                # Update stock quantity for the previous product
                old_product = existing_order.product
                old_product.stock_quantity += existing_order.quantity
                old_product.save()
                
                # Update stock quantity for the new product
                new_product = self.product
                if new_product.stock_quantity < self.quantity:
                    raise ValidationError("Not enough stock available for the new product.")
                new_product.stock_quantity -= self.quantity
                new_product.save()
        else:
            # Handle stock quantity when a new order is created
            product = self.product
            if product.stock_quantity < self.quantity:
                raise ValidationError("Not enough stock available.")
            product.stock_quantity -= self.quantity
            product.save()
        
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.product} by {self.company_name}"

    class Meta:
        verbose_name_plural = "Orders"
