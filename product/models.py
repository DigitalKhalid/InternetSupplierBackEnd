from django.db import models

class Unit(models.Model):
    title = models.CharField('Unit', max_length=25)
    value = models.IntegerField('Value', default=0)

    def __str__(self):
        return self.title

class ProductType(models.Model):
    title = models.CharField('Product Type', max_length=50)

    def __str__(self):
        return self.title

class ProductCatagory(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='catagories', verbose_name='Type')
    title = models.CharField('Product Catagory', max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    # type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products', verbose_name='Product Type')
    catagory = models.ForeignKey(ProductCatagory, on_delete=models.CASCADE, related_name='products', verbose_name='Product Catagory')
    title = models.CharField('Title', max_length=50)
    sku = models.CharField('SKU', max_length=50)
    description = models.CharField('Description', max_length=200, null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='products', verbose_name='Unit')
    purchase_price = models.IntegerField('Purchase Price', default=0)
    sale_price = models.IntegerField('Sale Price', default=0)
    date_created = models.DateField('Date Created', auto_now_add=True)

    def __str__(self):
        return self.title