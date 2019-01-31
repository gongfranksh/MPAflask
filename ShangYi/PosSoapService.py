from spyne.protocol.soap import Soap11

from server_auth import spyne


class POSSoapService(spyne.Service):
    __service_url_path__ = '/soap/posservice'
    __target_namespace__ = 'http://shangyi.weiliang.webservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()
    __wsse_conf__ = {
        'username': 'myusername',
        'password': 'mypassword'  # never store passwords directly in sources!
    }