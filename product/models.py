from django.db import models

class Unit(models.Model):
    title = models.CharField('Unit', max_length=25)

    def __str__(self):
        return self.title

class ProductType(models.Model):
    title = models.CharField('Product Type', max_length=50)

    def __str__(self):
        return self.title

class ProductCatagory(models.Model):
    title = models.CharField('Product Catagory', max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products', verbose_name='Product Type')
    catagory = models.ForeignKey(ProductCatagory, on_delete=models.CASCADE, related_name='products', verbose_name='Product Catagory')
    title = models.CharField('Title', max_length=50)
    sku = models.CharField('SKU', max_length=50)
    description = models.CharField('Description', max_length=200, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='products', verbose_name='Unit')
    purchase_price = models.IntegerField('Purchase Price', null=True, blank=True)
    sale_price = models.IntegerField('Sale Price', null=True, blank=True)
    date_created = models.DateField('Date Created', auto_now_add=True)

    def __str__(self):
        return self.title