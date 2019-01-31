# -*- coding: utf-8 -*-
from Entity.jsEntity import JsEntity


class Branch(JsEntity):

    def __init__(self,branchcode):
        JsEntity.__init__(self, "BRANCH",branchcode)

