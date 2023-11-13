# views.py
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomerCL, TagCL, ProductCL, OrderCL
from .forms import OrderForm

class TagView(View):
    template_name = 'tag.html'

    def get(self, request, tag_name):
        products = ProductCL.objects.filter(tag__name=tag_name)
        return render(request, self.template_name, {'products': products, 'tag_name': tag_name})





class AllProductsView(View):
    template_name = 'products.html'

    def get(self, request):
        products = ProductCL.objects.all()
        return render(request, self.template_name, {'products': products})

class CreateOrderView(View):
    template_name = 'create_order.html'
    form_class = OrderForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_products')  # Перенаправление после успешного создания заказа
        return render(request, self.template_name, {'form': form})

class OrderListView(View):
    template_name = 'order_list.html'

    def get(self, request):
        orders = OrderCL.objects.all()
        return render(request, self.template_name, {'orders': orders})

class CustomerOrderView(View):
    template_name = 'customer_order.html'

    def get(self, request, customer_id):
        customer = CustomerCL.objects.get(id=customer_id)
        orders = OrderCL.objects.filter(customer=customer)
        return render(request, self.template_name, {'customer': customer, 'orders': orders})
