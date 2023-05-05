from django.conf import settings
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(
        max_length=255, verbose_name='Descrição Resumida')
    description_full = models.TextField(verbose_name='Descrição Completa')
    image = models.ImageField(upload_to='product_image/%Y/%m/', blank=True,
                              null=True, verbose_name='Imagem')
    slug = models.SlugField(unique=True, blank=True, null=True)
    price = models.DecimalField(
        verbose_name='Preço', max_digits=7, decimal_places=2)
    price_promotional = models.DecimalField(default=0,
                                            verbose_name='Preço Promocional',
                                            max_digits=7, decimal_places=2)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_price_format(self):
        return utils.format_price(self.price)
    get_price_format.short_description = 'Preço'

    def get_price_promo_format(self):
        return utils.format_price(self.price_promotional)
    get_price_promo_format.short_description = 'Preço Promocional'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Variation(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Produto')
    name = models.CharField(max_length=50, blank=True,
                            null=True, verbose_name='Nome')
    price = models.DecimalField(
        verbose_name='Preço', max_digits=7, decimal_places=2)
    price_promotional = models.DecimalField(default=0,
                                            verbose_name='Preço Promocional',
                                            max_digits=7, decimal_places=2)
    stock = models.PositiveIntegerField(default=1, verbose_name='Estoque')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
