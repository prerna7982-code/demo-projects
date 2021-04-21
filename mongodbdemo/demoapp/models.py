from djongo import models
# Create your models here.

class Posts(models.Model):
    _id=models.ObjectIdField()
    post_title=models.CharField(max_length=255)
    post_description=models.TextField()
    comment=models.JSONField()
    tags=models.JSONField()
    username=models.CharField(default = 'anonymous', null=True, blank = True, max_length=255)
    objects=models.DjongoManager()