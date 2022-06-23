from django.db import models
from django.urls import reverse

STATUS = (
(0,"Draft"),
(1,"Publish")
)
class Post(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey('auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def Meta(self):
        ordering_on = ['-created_on']

    def __str__(self):
        return self.title

#john = Post(title='hey dude')
    def get_absolute_url(self):

        return reverse('post_detail',args=[str(self.id)])
