from .keranjang import Khoiriyah

def keranjang(request):
    return {'keranjang': Khoiriyah(request)}
