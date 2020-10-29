# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.models.vod_media_pb2 import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    req = GetRecommendedPostersRequest()
    req.Vids.append("vid")
    req.Vids.append("vid1")
    req.Vids.append("vid2")

    try:
        resp = vod_service.get_recommended_posters(req)
    except Exception:
        raise
    else:
        print(resp)
        if resp.ResponseMetadata.Error.Code != '':
            print(resp.ResponseMetadata.Error)