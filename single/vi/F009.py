# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""single/vi/F009.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import single.vi.BASE_TPL
    reload(single.vi.BASE_TPL)
from single.vi.BASE_TPL             import cBASE_TPL


class cF009(cBASE_TPL):
    
    def setClassName(self):
        self.dl_name = 'F009_dl'


    def specialinit(self):


        self.navTitle = '图片管理'


    def initPagiUrl(self):
        qqid = self.REQUEST.get('qqid','')
        url = self.sUrl
        if qqid:
            url += "&qqid=%s" % qqid
        return url

    def goPartList(self):
        self.getBreadcrumb()  # 获取面包屑
        self.assign('NL',self.dl.GNL)
        PL,L = self.dl.mRight()
        self.assign('dataList',L)
        self.getPagination(PL)
        s = self.runApp('F009_list.html')
        return s
    
    def goPartLocalfrm(self):
        self.navTitle = '批量图片'
        self.getBreadcrumb()  # 获取面包屑
        self.initHiddenLocal()#初始隐藏域
        self.getBackBtn()
        s = self.runApp('F009_local.html')
        return s


    def goPartDel_pic(self):
        dR = self.dl.delete_qiniu_pic_data()
        return self.jsons(dR)

