# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Sina Corporation
# All Rights Reserved.
# Author: Zhongyue Luo <lzyeval@gmail.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova import flags
from novaclient.v1_1 import client


FLAGS = flags.FLAGS

NOVA_CLIENT = client.Client(FLAGS.keystone_username,
                            FLAGS.keystone_password,
                            FLAGS.keystone_tenant_name,
                            FLAGS.keystone_auth_url,
                            service_type="compute")


def is_running(floating_ip_uuid):
    return not is_terminated(floating_ip_uuid)


def is_terminated(floating_ip_uuid):
    # TODO(lzyeval): handle error
    # NOTE(yaguang): handle exception when floating ip is released by user
    #                we can not get info from novaclient
    try:
        floating_ip = NOVA_CLIENT.floating_ips.get(floating_ip_uuid)
    except Exception:
        return True
    return False


def get_usage(floating_ip_uuid, datetime_from, datetime_to, order_size):
    return order_size
