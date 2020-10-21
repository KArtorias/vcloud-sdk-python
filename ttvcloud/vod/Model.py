# coding : utf-8


class UpdateVideoPublishStatusRequest(object):
    def __init__(self, vid='', status=''):
        self.vid = vid
        self.status = status

    def set_vid(self, vid):
        self.vid = vid

    def set_status(self, status):
        self.status = status

    def get_vid(self):
        return self.vid

    def get_status(self):
        return self.status


class UpdateVideoInfoRequest(object):
    def __init__(self, vid='', poster_uri=None, title=None, description=None, tags=None):
        self.vid = vid
        self.poster_uri = poster_uri
        self.title = title
        self.description = description
        self.tags = tags

    def set_vid(self, vid):
        self.vid = vid

    def set_poster_uri(self, poster_uri):
        self.poster_uri = poster_uri

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_tags(self, tags):
        self.tags = tags

    def get_vid(self):
        return self.vid

    def get_poster_uri(self):
        return self.poster_uri

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_tags(self):
        return self.tags


class GetVideoInfosRequest(object):
    def __init__(self, vids=[]):
        self.vids = vids

    def set_vids(self, vids):
        self.vids = vids

    def get_vids(self):
        return self.vids


class AudioStreamMeta(object):
    def __init__(self):
        self.Codec = None
        self.Duration = None
        self.SampleRate = None
        self.Bitrate = None

    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Duration = params.get("Duration")
        self.SampleRate = params.get("SampleRate")
        self.Bitrate = params.get("Bitrate")


class VideoStreamMeta(object):
    def __init__(self):
        self.Codec = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Definition = None
        self.Bitrate= None
        self.Fps = None

    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Fps = params.get("Fps")


class TranscodeInfo(object):
    def __init__(self):
        self.FileId = None
        self.Md5 = None
        self.FileType = None
        self.LogoType = None
        self.Encrypt = None
        self.Format = None
        self.Duration = None
        self.Size = None
        self.StoreUri = None
        self.VideoStreamMeta = None
        self.AudioStreamMeta = None
        self.CreateTime = None

    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Md5 = params.get("Md5")
        self.FileType = params.get("FileType")
        self.LogoType = params.get("LogoType")
        self.Encrypt = params.get("Encrypt")
        self.Format = params.get("Format")
        self.Duration = params.get("Duration")
        self.Size = params.get("Size")
        self.StoreUri = params.get("StoreUri")
        if params.get("VideoStreamMeta") is not None:
            self.VideoStreamMeta = VideoStreamMeta()
            self.VideoStreamMeta._deserialize(params.get("VideoStreamMeta"))
        if params.get("AudioStreamMeta") is not None:
            self.AudioStreamMeta = AudioStreamMeta()
            self.AudioStreamMeta._deserialize(params.get("AudioStreamMeta"))
        self.CreateTime = params.get("CreateTime")


class SourceInfo(object):
    def __init__(self):
        self.FileId = None
        self.Md5 = None
        self.FileType = None
        self.Codec = None
        self.Height = None
        self.Width = None
        self.Format = None
        self.Duration = None
        self.Size = None
        self.StoreUri = None
        self.Definition = None
        self.Bitrate = None
        self.Fps = None
        self.CreateTime = None

    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Md5 = params.get("Md5")
        self.FileType = params.get("FileType")
        self.Codec = params.get("Codec")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Format = params.get("Format")
        self.Duration = params.get("Duration")
        self.Size = params.get("Size")
        self.StoreUri = params.get("StoreUri")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Fps = params.get("Fps")
        self.CreateTime = params.get("CreateTime")


class BasicInfo(object):
    def __init__(self):
        self.SpaceName = None
        self.Vid = None
        self.Title = None
        self.Description = None
        self.PosterUri = None
        self.PublishStatus = None
        self.AuditStatus = None
        self.Tags = None
        self.CreateTime = None

    def _deserialize(self, params):
        self.SpaceName = params.get("SpaceName")
        self.Vid = params.get("Vid")
        self.Title = params.get("Title")
        self.Description = params.get("Description")
        self.PosterUri = params.get("PosterUri")
        self.PublishStatus = params.get("PublishStatus")
        self.AuditStatus = params.get("AuditStatus")
        self.Tags = params.get("Tags")
        self.CreateTime = params.get("CreateTime")


class VideoInfo(object):
    def __init__(self):
        self.BasicInfo = None
        self.SourceInfo = None
        self.TranscodeInfos = None

    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = BasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("SourceInfo") is not None:
            self.SourceInfo = SourceInfo()
            self.SourceInfo._deserialize(params.get("SourceInfo"))
        if params.get("TranscodeInfos") is not None:
            self.TranscodeInfos = list()
            for row in params.get("TranscodeInfos"):
                if row is None:
                    continue
                re_row = TranscodeInfo()
                re_row._deserialize(row)
                self.TranscodeInfos.append(re_row)


class GetVideoInfosResponse(object):
    def __init__(self):
        self.VideoInfoList = None
        self.NotExistVids = None

    def _deserialize(self, params):
        if params.get("VideoInfoList") is not None:
            self.VideoInfoList = list()
            for row in params.get("VideoInfoList"):
                if row is None:
                    continue
                re_row = VideoInfo()
                re_row._deserialize(row)
                self.VideoInfoList.append(re_row)
        self.NotExistVids = params.get("NotExistVids")


class GetRecommendedPostersRequest(object):
    def __init__(self, vids=[]):
        self.vids = vids

    def set_vids(self, vids):
        self.vids = vids

    def get_vids(self):
        return self.vids


class GetRecommendedPostersResponse(object):
    def __init__(self):
        self.StoreUriGroups = None
        self.NotExistVids = None

    def _deserialize(self, params):
        self.StoreUriGroups = params.get("StoreUriGroups")
        self.NotExistVids = params.get("NotExistVids")