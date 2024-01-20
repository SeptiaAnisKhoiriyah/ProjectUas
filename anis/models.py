from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

class Kategori(models.Model):
    nama = models.CharField(max_length=200, blank=True, null=False)
    aktif = models.BooleanField(default= True)
    banner_satu = ResizedImageField(size=[575, 200], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (575 x 200 pixel)")
    banner_dua = ResizedImageField(size=[575, 200], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (575 x 200 pixel)")
    slug = models.SlugField(max_length=200, null=True,blank=True, unique=True)
    class Meta:
        verbose_name_plural ="Data Kategori"

    def __str__(self):
        return f"Nama: {self.nama}"
    
    @property
    def get_produk(self):
        return Produk.objects.filter(kategori__slug=self.slug)
#         
    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(self.nama)
    #     return super().save(*args, **kwargs)

class Produk(models.Model):
    KETERANGAN=(
        ('Baru', 'Baru'),
        ('Lama' , 'Lama'),
    )
    kategori = models.ForeignKey(Kategori, null=True, blank=True, related_name= "produks", on_delete= models.SET_NULL)
    nama_produk = models.CharField(max_length=200, blank=True, null=True)
    gambar = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    gambar_satu = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    gambar_dua = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    gambar_tiga = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    gambar_empat = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    gambar_lima = ResizedImageField(size=[270, 250], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (270 x 250 pixel)")
    slug = models.SlugField(max_length=200, unique=True)
    keterangan = RichTextField(blank=True, null=True)
    harga = models.PositiveIntegerField(blank=True, null=True)
    no_whatsApp = models.PositiveBigIntegerField(blank=True, null=True,)
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    diskon = models.IntegerField(default=0, blank=True, null=True, verbose_name="Diskon %")
    dibeli = models.IntegerField(default=0, blank=True, null=True)
    aktif = models.BooleanField(default=True)
    keterangan_barang = models.CharField(max_length=200, null=True, choices=KETERANGAN)
    class Meta:
        verbose_name_plural ="Data Produk"
    @property
    def setelah_diskon(self):
        if self.diskon == 0 :
            nilai_diskon = self.harga
        else:
            jml = self.diskon / 100
            nilai_diskon = self.harga - (jml * self.harga)
        return nilai_diskon
    def __str__(self):
        return self.nama_produk



class Slide(models.Model):
    teks_awal = models.CharField(max_length=200, blank=True, null=True)
    teks_dua = models.CharField(max_length=200, blank=True, null=True)
    teks_tiga = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = ResizedImageField(size=[475, 880], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (475 x 880 pixel)")
    aktif = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural ="Data Slide"

class Kontak(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    no_whatsApp = models.PositiveBigIntegerField(blank=True, null=True,)
    email = models.EmailField(max_length=200,blank=False, null=True)
    subject = models.CharField(max_length=200, blank=False, null=True)
    isi = models.TextField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Data Kontak"

class Profil(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    keterangan =  RichTextField(blank=True, null=True)
    gambar = ResizedImageField(size=[1920, 1200], quality=80,crop=['middle', 'center'] , upload_to='gambar/banner', blank=True,null=True, verbose_name="Gambar (1920 x 1200 pixel)")
    tanggal_upload= models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name_plural ="Data Profil"

class Statis(models.Model):
    alamat_kami = models.TextField(max_length=200, blank=False, null=True)
    telpon = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    class Meta:
        verbose_name_plural ="Data Statis"

class ChatID(models.Model):
    chatid = models.CharField(max_length=200, blank=False, null=True)
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default= True)

    class Meta:
        verbose_name_plural ="Data Chat ID"
