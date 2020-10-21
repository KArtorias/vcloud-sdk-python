# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.Model import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    vid = 'vid'
    publish_status = 'Published'
    unpublish_status = 'Unpublished'
    req = UpdateVideoPublishStatusRequest()
    req.set_vid(vid)
    req.set_status(unpublish_status)
    try:
        vod_service.update_video_publish_status(req)
    except Exception as e:
        print(e)
