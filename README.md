1.django环境搭建

2.从GitHub复制项目到本地

3.Git环境搭建, git remote add origin https://github.com/Maizix/web
    创建并切换到dev分支,写.gitignore

4.使用Pycharm
    设置settings
    配置数据库
    配置MEDIA_ROOT和MEDIA_URL,'upload'
    创建用户admin@admin.com, pw:admin
    简单修改admin中各项list_display

5.按需求说明开始[首页]的搭建
    1.广告:views中设定global_setting()用以获取数据, settings中增加'common.views.global_setting'
        前端for循环展示数据,url中写入cid,可通过cid找到对应数据

    2.搜索:Keywords在global_setting()中获取, search方法GET用户输入字符,返回json,此处用chain链接两个Queryset
        前端用ajax取json

    3.课程:获取全部is_homeshow=1的课程list,将list对应3个标签做3个排序的list,用Paginator写分页

    4.名师:获取user分组为'老师'的用户做展示.

    5.推荐阅读: 按分类获取文章list.

6.git add ,commit, push