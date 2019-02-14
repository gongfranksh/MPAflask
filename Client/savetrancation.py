# -*- coding: utf-8 -*-
from Entity.PosOrder import PosOrder

# trans = """
#     {"branch":"{\"PinYin\":\"lezhixuhuidian\",\"braid\":\"01002\",\"braname\":\"乐之徐汇店\",\"brasname\":\"乐之徐汇店\"}","operator":"{\"Braid\":\"01002\",\"Discount\":1.0,\"Domain\":\"\",\"EmpName\":\"1楼乐之\",\"Empid\":\"80023\",\"Password\":\"00000000\",\"Pinyin\":\"1loulezhi\"}","saledaily":"[{\"BarCode\":\"050036344494\",\"NormalPrice\":499.0,\"ProId\":\"2000000268996\",\"ProName\":\"无线蓝牙运动耳机\",\"SaleAmt\":499.0,\"SaleQty\":1.0},{\"BarCode\":\"2000000299761\",\"NormalPrice\":3898.0,\"ProId\":\"2000000299761\",\"ProName\":\"B\\u0026O H9i\",\"SaleAmt\":3898.0,\"SaleQty\":1.0}]","payment":"[{\"CadType\":\"none\",\"PayMentId\":2,\"PayMentName\":\"现金\",\"PayModeId\":\"111\",\"PayMoney\":2360.0},{\"CadType\":\"none\",\"PayMentId\":3,\"PayMentName\":\"银行卡\",\"PayModeId\":\"111\",\"PayMoney\":250.0},{\"CadType\":\"none\",\"PayMentId\":7,\"PayMentName\":\"支付宝\",\"PayModeId\":\"111\",\"PayMoney\":360.0},{\"CadType\":\"none\",\"PayMentId\":11,\"PayMentName\":\"微信\",\"PayModeId\":\"111\",\"PayMoney\":360.0},{\"CadType\":\"none\",\"PayMentId\":4,\"PayMentName\":\"购物券\",\"PayModeId\":\"111\",\"PayMoney\":250.0},{\"CadType\":\"none\",\"PayMentId\":6,\"PayMentName\":\"优惠券\",\"PayModeId\":\"111\",\"PayMoney\":670.0},{\"CadType\":\"none\",\"PayMentId\":5,\"PayMentName\":\"其他收款\",\"PayModeId\":\"111\",\"PayMoney\":147.0}]"}
# """

trans = """
{"branch": {"PinYin":"lezhixuhuidian","braid":"01002","braname":"乐之徐汇店","brasname":"乐之徐汇店"}}
"""

# trans.replace('\"', '"')
posorder = PosOrder()
posorder.Submit_PosOrder(trans)
