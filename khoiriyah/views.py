from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from anis.models import Produk
from .keranjang import Khoiriyah
from .forms import KhoiriyahAddProductForm

@require_POST
def khoiriyah_add(request, product_id):
    khoiriyah = Khoiriyah(request) # create a new cart object passing it the request object 
    product = get_object_or_404(Produk, id=product_id) 
    quantity = int(request.POST.get('quantity'))
    form = KhoiriyahAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        khoiriyah.add(product=product, quantity=quantity, update_quantity=cd['update'])
    return redirect('khoiriyah_detail')

def khoiriyah_remove(request, product_id):
    khoiriyah = Khoiriyah(request)
    product = get_object_or_404(Produk, id=product_id)
    khoiriyah.remove(product)
    return redirect('khoiriyah_detail')

def khoiriyah_detail(request):
    khoiriyah = Khoiriyah(request)
    context = {
            'judul': 'Halaman Pemesanan Produk',
            'khoiriyah':khoiriyah
        }
    for item in khoiriyah:
        item['update_quantity_form'] = KhoiriyahAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'pemesanan.html',context)

