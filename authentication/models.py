from django.db import models

class Item(models.Model):
          name=models.CharField(max_length=100)
          desc=models.ImageField(upload_to='blogi_mages/')
          def __str__(self):
                  return self.name
class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments',null=True)
    cmt = models.TextField(max_length=100, )

    def __str__(self):
        return self.cmt
