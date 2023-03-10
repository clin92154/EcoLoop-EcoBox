from django.db import models

# Create your models here.
class User_Info(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')         #user_id
    name = models.CharField(max_length=255,blank=True,null=False)       #LINE名字
    pic_url = models.CharField(max_length=255,null=False)               #大頭貼網址
    text = models.CharField(max_length=255,blank=True,null=False)      #文字訊息紀錄
    dateTime = models.DateTimeField(auto_now=True)                           #物件儲存的日期時間

    def __str__(self):
        return self.uid