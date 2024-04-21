from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    return '{0}/{1}'.format("recipe_photos",filename)

class recipe_data(models.Model):
    recipe_Id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100,blank=False, null=False )
    recipe_desc = models.CharField(max_length=255, blank=False, null=False)
    recipe_photo = models.ImageField(upload_to=user_directory_path, null = True, blank = True, verbose_name="")

    class Meta:
        db_table = 'recipes'