# coding=utf-8


class JavaBook(object):
    url = None  # 详情链接
    title = None  # 标题
    content = None  # 正文
    push_date = None  # 网站更新时间
    synopsis = None  # 简介
    catalogs = None  # 目录
    resource = None  # 资源信息
    status = "VALIDE"  # 状态        有效 VALIDE 无效 INVALIDE

    def __init__(self, url=None, title=None, content=None, push_date=None, synopsis=None, catalog=None, resource=None,
                 status="VALIDE"):
        self.url = url
        self.title = title
        self.content = content
        self.push_date = push_date
        self.synopsis = synopsis
        self.catalogs = catalog
        self.resource = resource
        self.status = status

    def set_attr(self, url=None, title=None, content=None, push_date=None, synopsis=None, catalog=None, resource=None,
                 status="VALIDE"):
        self.url = url
        self.title = title
        self.content = content
        self.push_date = push_date
        self.synopsis = synopsis
        self.catalogs = catalog
        self.resource = resource
        self.status = status
        return self

    def save_to_db(self, connection):
        sql = "insert into tb_spider_data_javabook(url, title, content, push_date, synopsis, catalogs, resource," \
              " status, created_time ) values('%s','%s','%s','%s','%s','%s','%s','%s', now())" \
              % (self.url, self.title, self.content, self.push_date, self.synopsis, self.catalogs, self.resource, self.status)
        return connection.insertOne(sql)
