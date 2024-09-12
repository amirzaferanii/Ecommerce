from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from .models import Category, Comment, Like

from product.models import Product


class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        like = Like.objects.filter(product=product)
        if request.user.is_authenticated:
            is_like = Like.objects.filter(product=product, user=request.user).exists()
            product_likes = Like.objects.filter(user=request.user)
        else:
            is_like = False
            product_likes = Like.objects.none()
        context = {'product': product, 'is_like': is_like, 'like': like, 'product_likes': product_likes}
        return render(request, 'product/product_details.html', context)


    def post(self, request, pk):
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        product = get_object_or_404(Product, pk=pk)
        Comment.objects.create(body=body, product=product, user=request.user, parent_id=parent_id)
        context = {'product': product}
        return render(request, 'product/product_details.html', context)



class CategoryRenderPartial(TemplateView):
    template_name = 'includes/main_navbar.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryRenderPartial, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(status=True)






def Category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()
    return render(request, "product/product_list.html", {"products": products})






class SearchProductView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Product.objects.filter(title__icontains=q)
        return Product.objects.all()




class LikeProductView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = request.user
        if user.is_authenticated:
            if Like.objects.filter(product=product, user=user).exists():
                Like.objects.filter(product=product, user=user).delete()
                return redirect('product:product_detail', pk)
            else:
                Like.objects.create(product=product, user=user)
        return redirect('product:product_detail', pk)



class ProductLikers(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        liker = Like.objects.filter(product=product)
        context = {'liker': liker}
        return render(request, 'product/product_likers.html', context)