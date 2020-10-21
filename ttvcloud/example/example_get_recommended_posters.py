# coding:utf-8
from __future__ import print_function

from ttvcloud.vod.VodService import VodService
from ttvcloud.vod.Model import *

if __name__ == '__main__':
    vod_service = VodService()

    # call below method if you dont set ak and sk in $HOME/.vcloud/config
    # vod_service.set_ak('your ak')
    # vod_service.set_sk('your sk')

    vids = ['vid1', 'vid2', 'vid3']
    req = GetRecommendedPostersRequest()
    req.set_vids(vids)

    resp = vod_service.get_recommended_posters(req)
    print(resp.StoreUriGroups)
    print(resp.NotExistVids)