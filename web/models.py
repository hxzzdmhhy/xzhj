from django.db import models

# Create your models here.

#文件列表
class Search_Filelist(models.Model):
    info_hash = models.CharField(max_length=40, primary_key=True, null=False)
    file_list = models.TextField(null=False)

    class Meta:
        db_table = "search_filelist"


#Hash列表
class Search_Hash(models.Model):
    id = models.AutoField(primary_key=True)
    info_hash = models.CharField(max_length=40, unique=True)
    category = models.CharField(max_length=20)
    data_hash = models.CharField(max_length=32)
    name = models.CharField(max_length=200)
    extension = models.CharField(max_length=20)
    classified = models.BooleanField(default=False)
    source_ip = models.CharField(max_length=20)
    tagged = models.BooleanField(default=False)
    length = models.BigIntegerField()
    create_time = models.DateTimeField()
    last_seen = models.DateTimeField()
    requests = models.IntegerField()
    comment = models.CharField(max_length=100)
    creator = models.CharField(max_length=20)
    class Meta:
        db_table = "search_hash"



#首页推荐
class Search_Keywords(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=20, null=False, unique=True)
    order = models.IntegerField(null=False)
    pic = models.CharField(max_length=100, null=False)
    score = models.CharField(max_length=10, null=False)
    class Meta:
        db_table = "search_keywords"


#搜索记录
class Search_Tags(models.Model):

    id = models.AutoField(primary_key=True, null=False,)
    tag = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        db_table = "search_tags"


#爬取统计
class Search_Statusreport(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(null=False)
    new_hashes = models.IntegerField(null=False)
    total_requests = models.IntegerField(null=False)
    valid_requests = models.IntegerField(null=False)
    class Meta:
        db_table = "search_statusreport"

#用户表
class User(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "user"







