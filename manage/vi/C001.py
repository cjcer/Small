# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""manage/vi/C001.py"""

from imp import reload
from basic.publicw import DEBUG
if DEBUG == '1':
    import manage.vi.BASE_TPL
    reload(manage.vi.BASE_TPL)
from manage.vi.BASE_TPL             import cBASE_TPL


class cC001(cBASE_TPL):
    
    def setClassName(self):
        self.dl_name = 'C001_dl'

    def goPartList(self):
        
        self.assign('NL',self.dl.GNL)
        self.navTitle = '商品分类'
        self.getBreadcrumb() #获取面包屑
        PL,L = self.dl.mRight()
        self.assign('dataList',L)
        self.getPagination(PL)

        fl = self.dl.setfllist()
        fllist = self.Html.select(fl, 'pid', self.dl.GP('pid', ''), {'class': 'form-control','onchange':"this.form.pageNo.value=1;this.form.submit();"})
        self.assign('fllist', fllist)
        return self.runApp('C001_list.html')
    
    def initPagiUrl(self):
        lb_code = self.REQUEST.get('lb_code','')
        brand_id = self.REQUEST.get('brand_id','')
        status = self.REQUEST.get('status','')
        ctype = self.REQUEST.get('ctype','')
        qqid = self.REQUEST.get('qqid','')
        url = self.sUrl
        if qqid:
            url += "&qqid=%s" % qqid
        if lb_code:
            url += "&lb_code=%s" % lb_code
        if brand_id:
            url += "&brand_id=%s" % brand_id
        if status:
            url += "&status=%s" % status
        if ctype:
            url += "&ctype=%s" % ctype
        return url
    
    def goPartLocalfrm(self):
        self.navTitle = ''
        self.getBreadcrumb() #获取面包屑
        self.initHiddenLocal()#初始隐藏域
        
        self.getBackBtn()

        self.item = self.dl.get_local_data()
        self.assign('item', self.item)
        # 上级分类select
        fl=self.dl.getfllist()
        fllist=self.Html.select(fl,'pid',self.item.get('pid',''),{'class': 'form-control'})
        self.assign('fllist', fllist)

        return self.runApp('C001_local.html')

    
    
        
 