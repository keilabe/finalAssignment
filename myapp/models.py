from django.db import models


# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + "" + self.lastname


class Destinations(models.Model):
    Image = models.ImageField(upload_to='images/')
    dname = models.CharField(max_length=50)
    eprice = models.IntegerField(default=0)
    description = models.TextField()
    country = models.CharField(max_length=20)
<<<<<<< HEAD
=======
    # caption = models.CharField(max_length=255)
    # likes = models.ManyToManyField(User, related_name='image_likes')
    # created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 6fc92ba (My Bootcamp-SP project)

    def __str__(self):
        return self.dname


class Holidayreserve(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    startDate = models.DateField()
    endDate = models.DateField()
    no_of_adults = models.PositiveIntegerField()
    no_of_children = models.PositiveIntegerField()
    destination = models.CharField(max_length=100, default='Maasai Mara')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    # fields used to show on the receipt the day of booking
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def calculate_total_amount(self):
        # defining prices as per the selected destination
        destination_prices = {
            'Olongonot Crater': {'adult_price': 2000, 'children_price': 1000},
            'Diani Beaches': {'adult_price': 3000, 'children_price': 1500},
            'Amboseli National Park': {'adult_price': 2000, 'children_price': 1000},
            'Mt Kenya': {'adult_price': 2500, 'children_price': 1200},
            'Zanzibar Island': {'adult_price': 10000, 'children_price': 6500},
            'Maasai Mara': {'adult_price': 4000, 'children_price': 2500},
            'Dragons Teeth & Lestima Summit': {'adult_price': 2000, 'children_price': 1000},
            'Malindi & Watamu beaches': {'adult_price': 3200, 'children_price': 1800},
            'Meru National Park': {'adult_price': 2000, 'children_price': 1000},
        }
        # getting the prices for the selected destination
        destination_price = destination_prices.get(self.destination, {'adult_price': 0, 'children_price': 0})

        total_amount = (self.no_of_adults * destination_price['adult_price']) + (
                    self.no_of_children * destination_price['children_price'])

        return total_amount

    def __str__(self):
        return self.firstname + "" + self.lastname
class ContactMessage(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        message = models.TextField()
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
<<<<<<< HEAD
=======

# class Comment(models.Model):
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 6fc92ba (My Bootcamp-SP project)
