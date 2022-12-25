from django.db import models
from django.utils.text import slugify
from accounts.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
from ckeditor.fields import RichTextField 
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title =models.CharField(max_length = 255, null=False, blank =False) 
    body = RichTextField( null = True, blank = True)
    slug = models.SlugField(unique=True, blank=True,)
    image = models.ImageField(null=True, blank=True ,default ="post.jpg", upload_to="post_images")
    thumbnail =models.ImageField(blank=True, null=True, upload_to="post_images/")
    tags = models.CharField(max_length=100, blank=True, null=True )
    date_created = models.DateTimeField(auto_now_add =True)
    date_Updated = models.DateTimeField(auto_now =True)
    
    def save(self, *args, **kwargs):
        self.slug == slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    class Meta:
        db_table = 'posts'
        verbose_name_plural ='posts'
        ordering = ('-date_created',)
    
    def get_snippet (self):
        return self.body[:150 ] +"" +"......"


    def save(self, *args, **kwargs):        
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)


    def get_imagethumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240X249.jpg'


    def make_thumbnail(self, image, size=(300,300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io , name = image.name)
        return thumbnail

 
class Comment(models.Model):
    author = models.ForeignKey(User,on_delete =models.CASCADE, related_name ='user')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add =True)
    class Meta:
        verbose_name_plural ='comments'
        db_table ='comments'
        ordering = ('-date_created',)

    def __str__(self):
        return self.text[0:10]



   