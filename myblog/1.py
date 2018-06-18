#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/16 9:17

NOTE：
安装Django: pip install Django==1.10.2;下载源码，进入根目录执行python setup.py install
查看Django :python -m django --version
在创建目录的cmd窗口输入django-admin startproject myblog,创建一个名为myblog的项目
在manage.py的同级，创建blog应用 python manage.py startapp blog，并在settings.py的INSTALLED_APPS中添加blog

编辑views.py
	每个响应对应一个函数，函数必须返回一个响应
	函数必须存在一个参数，一般约定为request
	每个响应（函数）对应一个URL
编辑urls.py
	每个URL都以url的形式写出来
	url函数放在urlpatterns列表中
	url函数三个参数：URL（正则），对应方法，名称
包含其他URL
	在根urls.py中引入include
	在APP目录下创建urls.py文件，格式与根urls.py相同
	根urls.py中url函数第二个参数改为include('blog.urls')
注意事项
	根urls.py针对APP配置的URL名称，是该APP所有URL的总路径
Django模板语言，Django Template Language,DTL
	render函数中支持一个dict类型参数
	该字典是后台传递到模板的参数，键为参数名
	在模板中使用{{参数名}}来直接使用
	Django按照INSTALLED_APPS中添加顺序查找Templates,不同APP下Templates目录中的同名.html文件会造成冲突，解决方法是
	在APP的Template目录下创建以APP名为名称的目录，将html文件放入新创建的目录下。
Django中的Models是什么？
	通常，一个Model对应数据库的一张数据表，Django中Models以类的形式表现，它包含了一些基本字段以及数据的一些行为
	ORM，Object Relation Mapping 对象关系映射，实现了对象和数据库之间的映射，隐藏了数据访问的细节，不需要编写SQL语句
	在应用根目录下创建models.py并引入models模块，创建类，集成models.Model，该类即使一张数据表；
	在类中创建字段,字段即类中的属性，attr = models.CharField(max_length=64)
Models生成数据表（生成ORM框架）
	执行python manage.py makemigrations app名（可选），再执行python manage.py migrate会在app/migrations/目录下
	生成移植文件；查看生成数据表的sql语句，执行python manage.py sqlmigrate 应用名 文件id
查看并编辑db.sqlite3（编辑数据库）
	使用第三方软件SQLite Expert Personal
页面呈现数据
	views.py中import models,article = models.Article.objects.get(pk=1)，render(request,page,{'article':article})
	前端步骤
admin
	自动化数据管理界面，管理数据库，定制功能
	创建超级用户 python manage.py createsuperuser
配置APP
	在应用下admin.py中引入自身的models模块，编辑admin.py:admin.site.register(models.Article)
修改数据默认显示名称
	在Article类下添加一个方法，根据Python版本选择__str__(self)或__unicode__(self),return self.title
博客页面设计
	博客主页面，博客文章内容页面，博客撰写页面
博客主页面
	文章标题列表，超链接，发表博客按钮；文章列表编写思路：取出数据库中所有文章对象，将文章对象们打包成列表，传递到前端，
	前端页面把文章以标题超链接的形式逐个列出
博客文章页面
	标题，文章内容，修改文章按钮（超链接）
Django中的超链接(个人理解：在index.html中添加超链接，相当于是在index.html触发views.py的article_page响应)
	超链接目标地址，href后面是目标地址，template中可以用“{% url 'app_name(namespace=):url_name(name=)' param %}”,
	其中app_name和url_name都在url中配置
url函数的名称参数
	根urls,写在include()的第二个参数位置，namespace='blog';或在应用下则写在url()的第三个参数位置，name = 'article'；
	使用哪种写法主要取决于是否使用include引用了另一个url配置文件。
博客撰写页面
	标题编辑栏，文章内容编辑区域，提交按钮
	编辑响应函数：使用request.POST['参数名']获取表达数据，models.Article.objects.create(title,content)创建对象
Templates过滤器
	写在模板中，属于Django模板语言，可以修改模板中的变量，从而显示不同的内容
	{{value | filter1 |filter2 | ...}}
Django Shell
	Python交互式命令行程序，自动引入项目环境，可以与项目交互，python manage.py shell，可以用来调试工作，测试未知方法
Admin
	创建admin配置类，class ArticleAdmin(admin.ModelAdmin),注册：admin.site.register(Article,ArticleAdmin)



'''
