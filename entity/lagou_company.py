# coding=utf-8


class LagouCompany(object):
    """
    拉钩公司数据实体类
    """

    id = None  # 主键

    city = None  # 所在城市      来源拉钩  不做处理

    company_name = None  # 公司全名 不做处理

    company_name_short = None  # 公司简称  不做处理

    lagou_company_id = None  # 拉勾网公司id

    finance_stage = None  # 融资情况

    company_type = None  # 公司类型  公司标签

    data_status = None  # 数据状态     正常： NOR      失效： INV

    DATA_STATUS_NORMAL = "NOR"

    DATA_STATUS_INVALID = "IVA"

    def set_attr(self, city=None, company_name=None, company_name_short=None, lagou_company_id=None, finance_stage=None,
                 company_type=None, data_status=DATA_STATUS_NORMAL):
        self.city = city
        self.company_name = company_name
        self.company_name_short = company_name_short
        self.lagou_company_id = lagou_company_id
        self.finance_stage = finance_stage
        self.company_type = company_type
        self.data_status = data_status
        return self

    def save_to_db(self, connection):
        """
        save to mysql
        :param connection:
        :return:
        """
        sql = "insert into tb_lagou_company(city, company_name, company_name_short, lagou_company_id, finance_stage," \
              " company_type, data_status,created_time) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', now())" % \
              (self.city, self.company_name, self.company_name_short, self.lagou_company_id, self.finance_stage,
               self.company_type, self.data_status)
        return connection.insertOne(sql)
