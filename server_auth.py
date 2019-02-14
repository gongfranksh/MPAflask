# -*- coding: utf-8 -*-
from logging.handlers import RotatingFileHandler

from flask import Flask, request
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
from Entity.PosMachine import PosMachine
from Entity.PosOrder import PosOrder
from Entity.ProductBarCode import ProductBarCode
from Entity.SystemFunction import SystemFunction

# h = logging.StreamHandler()
# rl = logging.getLogger()
# rl.setLevel(logging.DEBUG)
# rl.addHandler(h)
# from ShangYi.RequstFormatter import RequestFormatter

app = Flask(__name__)
spyne = Spyne(app)

# request_data = request.data

# @app.before_request
# def log_request_info():
#     app.logger.info('Headers: %s', request.headers)
#     app.logger.info('Body: %s', request.get_data())


@app.before_request
def before_request():
    print 'before request started'
    print request.url


@app.route("/log")
def logTest():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Code Handbook !! Log testing."





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
    def get_branch_result(self, branchcode):
        branch = Branch(branchcode)
        rst = branch.get_branch_all()
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
        app.logger.info('Get_Branch_PayMent')
        branchpayment = PayMent(branchcode)
        rst = branchpayment.get_branch_payment_all();
        return rst

    @spyne.rpc(Unicode, _returns=String)
    def Get_Branch_Employee_all(self, branchcode):
        # ip = request.remote_addr
        # app.logger.info('Get_Branch_Employee_all -%s' % ip)
        app.logger.info('Get_Branch_Employee_all' )
        branchemployee = BranchEmployee(branchcode)
        rst = branchemployee.get_branch_employee_all()
        return rst


    @spyne.rpc(Unicode, _returns=String)
    def get_branch_pos_machine_all(self, branchcode):
        app.logger.info('get_branch_pos_machine_all' )
        posmachine = PosMachine(branchcode)
        rst = posmachine.get_branch_pos_machine_all()
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

    @spyne.rpc(Unicode, _returns=String)
    def Pos_Submit_Order(self, transcation):
        posorder = PosOrder()
        rst=posorder.Submit_PosOrder(transcation)

        return rst


if __name__ == '__main__':
    # initialize the log handler
    # logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
    #
    # # set the log handler level
    # logHandler.setLevel(logging.DEBUG)
    #
    # # set the app logger level
    # app.logger.setLevel(logging.DEBUG)
    #
    # app.logger.addHandler(logHandler)

    app.debug = True
    handler = logging.FileHandler('info.log', encoding='UTF-8')
    handler.setLevel(logging.INFO)

    # formatter = RequestFormatter('[%(asctime)s] %(remote_addr)s -%levelname)s in %(module)s: %(message)s')
    # handler.setFormatter(formatter)
    logging_format = logging.Formatter(
        '%(asctime)-15s- %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s -%(threadName)s-%(process)d-%(pathname)s- %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)


    @app.before_request
    def log_request_info(self):
        app.logger.info('Headers: %s', request.headers)
        app.logger.info('Body: %s', request.get_data())




    app.run(host='0.0.0.0',debug=True)