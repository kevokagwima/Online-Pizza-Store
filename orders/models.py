from django.db import models
from django.db.models.deletion import CASCADE

class regular_pizza(models.Model):
  name = models.CharField(max_length=50)
  small = models.DecimalField(max_digits=5, decimal_places=2)
  large = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.small}) - large({self.large})"

class silican_pizza(models.Model):
  name = models.CharField(max_length=50)
  small = models.DecimalField(max_digits=5, decimal_places=2)
  large = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.small}) - large({self.large})"

class toppings(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name}"

class subs(models.Model):
  name = models.CharField(max_length=50)
  small = models.DecimalField(max_digits=5, decimal_places=2)
  large = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.small}) - large({self.large})"

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
  small = models.DecimalField(max_digits=5, decimal_places=2)
  large = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f"{self.name} - small({self.small}) - large({self.large})"

class order_items(models.Model):
  product_one = models.OneToOneField(regular_pizza, blank=True, on_delete=CASCADE, related_name="regular_pizza")
  product_two = models.OneToOneField(silican_pizza,blank=True, on_delete=CASCADE, related_name="silican_pizza")
  product_three = models.OneToOneField(toppings, blank=True, on_delete=CASCADE, related_name="topping")
  product_four = models.OneToOneField(subs, blank=True, on_delete=CASCADE, related_name="subs")
  product_five = models.OneToOneField(pasta, blank=True, on_delete=CASCADE, related_name="pasta")
  product_six = models.OneToOneField(salads, blank=True, on_delete=CASCADE, related_name="pasta")
  product_seven = models.OneToOneField(salads, blank=True, on_delete=CASCADE, related_name="salads")
  product_eight = models.OneToOneField(dinner_platters, blank=True, on_delete=CASCADE, related_name="dinner_platters")

class order(models.Model):
  name = models.CharField(max_length=64)
  items = models.ForeignKey(order_items, on_delete=CASCADE)
  date_ordered = models.DateTimeField(auto_now=True)
