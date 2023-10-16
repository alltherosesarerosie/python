from django.db import models


class pr_lan(models.Model):
    ACTUALITY = (
        ('Actual', 'Actual'),
        ('50 to 50', '50 to 50'),
        ('old', 'old'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    actuality = models.CharField(max_length=100, choices=ACTUALITY, default='Actual', null=True)
    video = models.URLField(null=True)


    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

