#!/usr/bin/env python
# coding=utf8

import util


class VideoAPIClass():
    CCTV_HOST = "m.pt1905.gitv.tv"
    CCTV_PLAY_API = 'http://' + CCTV_HOST + '/film/play/'
    MAC_ADDRESS = "d6:1c:54:42:4e:1b"

    def get_cctv_playinfo(self, vid):
        url = self.CCTV_PLAY_API + "{vid}?token&serverId={serverId}&channel_version={channel_version}&userId={userId}&mac={mac}&launcher_version={launcher_version}&sn={sn}&client_id={client_id}&home_version={home_version}&from=lunbo"
        url = url.format(
            vid=vid,
            serverId=102,
            channel_version=102,
            userId=9130180,
            mac=self.MAC_ADDRESS,
            launcher_version="9000.1.05",
            sn="not_found",
            client_id=1080109,
            home_version=110)
        return util.GetHttpData(url)
