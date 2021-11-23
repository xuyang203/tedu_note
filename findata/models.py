from django.db import models


class Fin(models.Model):
    copname = models.CharField('公司名称',max_length=30,unique=True)
    #create_time = models.DateTimeField('创建时间',auto_now_add=True)
    #update_time = models.DateTimeField('更新时间',auto_now=True)
    creditlevel = models.TextField('信用水平',default='')

    def _str_(self):
        return 'copname %s'%(self.copname)
# Create your models here.
