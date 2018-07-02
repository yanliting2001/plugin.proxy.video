# -*- coding: utf8 -*-

from simpleplugin import Plugin
import xbmc
import xbmcaddon
import json
from api import VideoAPIClass

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_DATA_PATH = xbmc.translatePath("special://profile/addon_data/%s" % ADDON_ID).decode("utf-8")


plugin = Plugin()
VIDEOAPI = VideoAPIClass()


@plugin.action()
def pptv_play(params):
    if not xbmc.getCondVisibility('system.platform.Android'):
        xbmc.Player().play("C:/Download/20160810-111059351.mkv", windowed=True)
        xbmc.executebuiltin("ActivateWindow(fullscreenvideo)")
        return
    cid = params.cid
    vid = params.vid
    json_query = {"cmp": {"pkg": "com.pptv.ott.sdk", "class": "com.pptv.ott.sdk.PlayerActivity"},
                  "extra": {"PLAY_TYPE": 0, "PLAY_CID": vid, "PLAY_VID": cid, "USERNAME": "", "TOKEN": ""}}
    xbmc.executebuiltin('XBMC.StartAndroidActivityByJsonIntent("{json_query}")'.format(json_query=json.dumps(json_query)))
    print "start play"


@plugin.action()
def cctv_play(params):
    cid = params.cid
    vid = params.vid
    play_url = get_playinfo_from_cctv(vid)
    if play_url:
        xbmc.Player().play(play_url, windowed=True)
        xbmc.executebuiltin("ActivateWindow(fullscreenvideo)")
    else:
        print "this url can't play"


def get_playinfo_from_cctv(vid):
    data = VIDEOAPI.get_cctv_playinfo(vid)
    data = json.loads(data)
    if data and data.get('code') == 2000 and "data" in data:
        play_url = data['data']['hdUrl']
        return play_url
    return None
