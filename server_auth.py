# -*- coding: utf-8 -*-
from flask import Flask
from flask_spyne import Spyne
from spyne import String
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
import logging

from Entity.Branch import Branch
from Entity.BranchEmployee import BranchEmployee
from Entity.Member import Member
from Entity.PayMent import PayMent
from Entity.ProductBarCode import ProductBarCode
from Entity.SystemFunction import SystemFunction

h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

app = Flask(__name__)
spyne = Spyne(app)


class PosSoapService(spyne.Service):
    __service_url_path__ = '/poswebservices'
    __target_namespace__ = 'http://shangyi.weiliang.webservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()
    __wsse_conf__ = {
        'username': 'myusername',
        'password': 'mypassword'  # never store passwords directly in sources!
    }

    @spyne.rpc(Unicode, _returns=String)
    def get_branch_result(self, braid):
        branch = Branch(braid)
        rst = branch.get_remote_table_result_all()
        return rst

    @spyne.rpc(Unicode, Unicode, _returns=String)
    def get_product_by_barcode(self, branchcode, barcode):
        productbarcode = ProductBarCode(branchcode)
        rst = productbarcode.seek_branch_product_barcode(barcode)
        # barcode查询步到，使用prodid查询
        if len(rst) == 2:
            rst = productbarcode.seek_branch_product_proid(barcode)
        return rst

    @spyne.rpc(Unicode, Unicode, _returns=String)
    def get_product_by_proname(self, branchcode, proname):
        productbarcode = ProductBarCode(branchcode)
        rst = productbarcode.seek_branch_product_name(proname)
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def get_functionmenu_all(self, branchcode):
        fun_menu = SystemFunction(branchcode)
        rst = fun_menu.get_section_function_json()
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def Get_Branch_PayMent(self, branchcode):
        branchpayment = PayMent(branchcode)
        rst = branchpayment.get_branch_payment_all();
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def Get_Branch_Employee_all(self, branchcode):
        branchemployee = BranchEmployee(branchcode)
        rst = branchemployee.get_branch_employee_all()
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def Get_memeber_by_mobile(self, mobile):
        member = Member()
        rst = member.seek_memeber_by_mobile(mobile)
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def Get_memeber_by_bncid(self, bncid):
        member = Member()
        rst = member.seek_memeber_by_bncid(bncid)
        return rst

if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)