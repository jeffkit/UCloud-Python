#encoding=utf-8

version = '0.1'

import hashlib
import urllib2
from urllib import urlencode
import json
import logging


def _verfy_ac(private_key, params):
    items = params.items()
    items.sort()

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data+private_key

    hash_new = hashlib.sha1()
    hash_new.update(params_data)
    hash_value = hash_new.hexdigest()
    return hash_value


class UCloudClient(object):
    """
    ucloud = UCloudClient(pubkey, prikey)
    rs = ucloud.CreateUHostInstance(Region='', ImageId='')
    if rs['RetCode'] == 0:
        print 'success'
    """

    def __init__(self, public_key, private_key,
                 host='http://api.spark.ucloud.cn'):
        self.host = host
        self.public_key = public_key
        self.private_key = private_key

    def _get(self, action, **params):
        _params = dict({'PublicKey': self.public_key, 'Action': action},
                       **params)
        _params['Signature'] = _verfy_ac(self.private_key, _params)
        try:
            rsp = urllib2.urlopen(self.host + '/',
                                  data=urlencode(_params)).read()
            data = json.loads(rsp)
            return data
        except:
            # 未知的错误
            logging.error('request api fail', exc_info=True)
            return {'RetCode': '-9999', 'Message': 'unkown error'}

    def __getattr__(self, attr):
        def wrap(**kwargs):
            return self._get(attr, **kwargs)
        return wrap
