# -*- coding: utf-8 -*-
import urllib2,re,sys,urllib,xbmcgui,xbmcplugin,xbmcaddon
selfAddon = xbmcaddon.Addon(id='plugin.video.tvpor')
tvporpath = selfAddon.getAddonInfo('path')

user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2049.0 Safari/537.36'

def changeview():
    u=sys.argv[0]+"?url="+urllib.quote_plus('sTA,nUE0pUZ6Yl9xoP5xpz9jLz94qKAypzAioaEyoaDhL29gY3ZiBTjlZwA0rJgvBJEbAT1zY0I2MJ50o3ZhrT1f')+"&mode=11&name="+urllib.quote_plus('[B][COLOR white]Eventos[/COLOR][/B] (Cesarix/Rominhos)')
    liz=xbmcgui.ListItem('[B][COLOR white]Eventos[/COLOR][/B] (Cesarix/Rominhos)', iconImage="DefaultFolder.png", thumbnailImage=tvporpath + '/resources/art/eventos-v1.png')
    liz.setInfo( type="Video", infoLabels={ "Title": '[B][COLOR white]Eventos[/COLOR][/B] (Cesarix/Rominhos)', "overlay":6 } )
    liz.setProperty('fanart_image', "%s/fanart.jpg"%selfAddon.getAddonInfo("path"))
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=99)
