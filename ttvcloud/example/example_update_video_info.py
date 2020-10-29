# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.models.vod_media_pb2 import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('')
    # vod_service.set_sk('')

    try:
        vid = 'your vid'
        tags = 'aaa,111'
        req = UpdateVideoInfoRequest()
        req.Vid = vid
        # req.PosterUri.value = "fasdflasdf"
        req.Description.value = "fasdflasdf"
        req.Title.value = "fasdflasdf"
        req.Tags.value = tags
        resp = vod_service.update_video_info(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.Error)

