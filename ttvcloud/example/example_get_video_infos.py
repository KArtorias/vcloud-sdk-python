# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    vids = ['vid1', 'vid2', 'vid3']

    resp = vod_service.get_video_info(vids)
    print(resp)