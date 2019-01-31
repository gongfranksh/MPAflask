# -*- coding: utf-8 -*-
from spyne import ServiceBase, Unicode, rpc, String, Iterable, Mandatory

from Entity.Branch import Branch
from Entity.BranchEmployee import BranchEmployee
from Entity.Member import Member
from Entity.PayMent import PayMent
from Entity.ProductBarCode import ProductBarCode
from Entity.SystemFunction import SystemFunction


class JsService(ServiceBase):

    @rpc(Unicode, _returns=String)
    def get_branch_result(self, braid):
        branch = Branch(braid)
        rst = branch.get_remote_table_result_all()
        return rst

    @rpc(Unicode, Unicode, _returns=String)
    def get_product_by_barcode(self, branchcode, barcode):
        productbarcode = ProductBarCode(branchcode)
        rst = productbarcode.seek_branch_product_barcode(barcode)
        # barcode查询步到，使用prodid查询
        if len(rst) == 2:
            rst = productbarcode.seek_branch_product_proid(barcode)
        return rst

    @rpc(Unicode, Unicode, _returns=String)
    def get_product_by_proname(self, branchcode, proname):
        productbarcode = ProductBarCode(branchcode)
        rst = productbarcode.seek_branch_product_name(proname)
        return rst

    @rpc(Unicode, _returns=String)
    def get_functionmenu_all(self, branchcode):
        fun_menu = SystemFunction(branchcode)
        rst = fun_menu.get_section_function_json()
        return rst

    @rpc(Unicode, _returns=String)
    def Get_Branch_PayMent(self, branchcode):
        branchpayment = PayMent(branchcode)
        rst = branchpayment.get_branch_payment_all();
        return rst

    @rpc(Unicode, _returns=String)
    def Get_Branch_Employee_all(self, branchcode):
        branchemployee = BranchEmployee(branchcode)
        rst = branchemployee.get_branch_employee_all()
        return rst

    @rpc(Unicode, _returns=String)
    def Get_memeber_by_mobile(self, mobile):
        member = Member()
        rst = member.seek_memeber_by_mobile(mobile)
        return rst

    @rpc(Unicode, _returns=String)
    def Get_memeber_by_bncid(self, bncid):
        member = Member()
        rst = member.seek_memeber_by_bncid(bncid)
        return rst


