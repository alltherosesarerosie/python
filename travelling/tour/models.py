from django.db import models

class Tour(models.Model):
    TYPE = (
        ('Приключенческий', 'Приключенческий'),
        ('Культурный', 'Культурный'),
        ('Романтический', 'Романтический'),
    )

    tour_name = models.CharField(max_length=30)
    description = models.TextField()
    tour_type = models.CharField(max_length=100, choices=TYPE, default=TYPE[0], null=True)
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Поле для хранения цены
    video = models.URLField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.tour_name

class ReviewTour(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    title_tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.title_tour}"