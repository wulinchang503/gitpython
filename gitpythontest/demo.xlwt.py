# -*- coding: utf-8 -*-

from requests.api import request
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt.Formatting import Borders
from xlwt.Style import XFStyle

bk = open_workbook(r'd:\聚合数据.xls')  # bk是Book类的对象
sheet_read_only = bk.sheet_by_name('手机号码归属地')  # sheet 是Sheet类的对象
url = sheet_read_only.cell_value(2, 1)
request_type = sheet_read_only.cell_value(3, 1)


#实际在这里开始for，循环的取excel中的动态值

if sheet_read_only.cell_value(6, 2) == 'form':
    content_type = 'application/x-www-form-urlencoded'
else:
    content_type = 'application/json'

#把取出的值进行转字典
params = eval(sheet_read_only.cell_value(6, 3))
response = request(request_type, url, params=params)

rs = eval(response.text)  # 仅仅获得所有的返回值

if response.status_code == sheet_read_only.cell_value(6, 4) and rs['error_code'] == sheet_read_only.cell_value(6, 5):
    original_wb = open_workbook(r'd:\聚合数据.xls', formatting_info=True)
    new_wb = copy(original_wb)
    sheet = new_wb.get_sheet(0) 
    border = Borders()
    border.left = border.THIN
    border.right = border.THIN
    border.top = border.THIN
    border.bottom = border.THIN
    
    style = XFStyle()
    style.borders = border
    
    sheet.write(6, 6, '通过', style)
    new_wb.save(r'd:\聚合数据测试报告.xls')
