from django.db import models

class regular_pizza(models.Model):
  name = models.CharField(max_length=50)
  price_one = models.DecimalField(max_digits=5, decimal_places=2)
  price_two = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.price_one}) - large({self.price_two})"

class silican_pizza(models.Model):
  name = models.CharField(max_length=50)
  price_one = models.DecimalField(max_digits=5, decimal_places=2)
  price_two = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.price_one}) - large({self.price_two})"

class toppings(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name}"

class subs(models.Model):
  name = models.CharField(max_length=50)
  price_one = models.DecimalField(max_digits=5, decimal_places=2)
  price_two = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.price_one}) - large({self.price_two})"

class pasta(models.Model):
  name = models.CharField(max_length=40)
  price = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} -- ({self.price})"

class salads(models.Model):
  name = models.CharField(max_length=40)
  price = models.DecimalField(max_digits=5,decimal_places=2)

  def __str___(self):
    return f"{self.name} -- ({self.price})"

class dinner_platters(models.Model):
  name = models.CharField(max_length=20)
  price_one = models.DecimalField(max_digits=5, decimal_places=2)
  price_two = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.price_one}) - large({self.price_two})"
