# -*- coding: utf-8 -*-

""" 
This plugin is 3rd party and not part of p2p-streams addon

Wiziwig.tv

"""
import sys,os
current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)
from peertopeerutils.webutils import *
from peertopeerutils.pluginxbmc import *
from peertopeerutils.directoryhandle import *
from peertopeerutils.timeutils import translate_months

WiziwigURL = 'http://www.wiziwig.tv'  

def module_tree(name,url,iconimage,mode,parser,parserfunction):
	if not parserfunction: wiziwig_cats()
	elif parserfunction == 'events': wiziwig_events(url)
	elif parserfunction == 'servers': wiziwig_servers(url)

def wiziwig_cats():
    addDir(translate(40009),WiziwigURL + '/index.php?part=sports',401,os.path.join(current_dir,'icon.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40010),WiziwigURL + '/competition.php?part=sports&discipline=americanfootball&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','americanfootball.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40011),WiziwigURL + '/competition.php?part=sports&discipline=football&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','football.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40012),WiziwigURL + '/competition.php?part=sports&discipline=basketball&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Basketball.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40013),WiziwigURL + '/competition.php?part=sports&discipline=icehockey&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','IceHockey.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40014),WiziwigURL + '/competition.php?part=sports&discipline=baseball&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Baseball.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40015),WiziwigURL + '/competition.php?part=sports&discipline=tennis&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Tennis.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40016),WiziwigURL + '/competition.php?part=sports&discipline=motorsports&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Racing.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40017),WiziwigURL + '/competition.php?part=sports&discipline=rugby&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Rugby.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40018),WiziwigURL + '/competition.php?part=sports&discipline=golf&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Golf.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40019),WiziwigURL + '/competition.php?part=sports&discipline=cricket&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Cricket.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40020),WiziwigURL + '/competition.php?part=sports&discipline=cycling&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Cycling.png'),1,True,parser='wiziwig',parserfunction='events')
    addDir(translate(40021),WiziwigURL + '/competition.php?part=sports&discipline=other&archive=no&allowedDays=1,2,3,4,5,6,7',401,os.path.join(addonpath,'resources','art','Other_white.png'),1,True,parser='wiziwig',parserfunction='events')
    xbmc.executebuiltin("Container.SetViewMode(51)")
    
def wiziwig_events(url):
    conteudo=clean(get_page_source(url))    
    eventos=re.compile('<div class="date" [^>]+>([^<]+)</div>\s*<span class="time" rel=[^>]+>([^<]+)</span> -\s*<span class="time" rel=[^>]+>([^<]+)</span>\s*</td>\s*<td class="home".+?<img[^>]* src="([^"]*)"[^>]*>([^<]+)<img [^>]+></td>(.*?)<td class="broadcast"><a class="broadcast" href="([^"]+)">Live</a></td>').findall(conteudo)
    for date,time1,time2,icon,team1,palha,url in eventos:
        if re.search('<td class="away">',palha):
            try:team2=' - ' + re.compile('<td class="away"><img.+?>(.+?)<img class="flag"').findall(palha)[0]
            except:team2=''
        else: team2=''
        datefinal=date.split(', ')
	try:
		month_day = re.compile('(.+?) (.*)').findall(datefinal[1])
		monthname = translate_months(month_day[0][0])
		dayname = int(month_day[0][1])
		hourname = int(time1.split(':')[0])
		minutesname = int(time1.split(':')[1])

		import datetime
                from peertopeerutils import pytzimp
                d = pytzimp.timezone(str(pytzimp.timezone('Europe/Madrid'))).localize(datetime.datetime(2014, monthname, dayname, hour=hourname, minute=minutesname))
                timezona= settings.getSetting('timezone_new')
                my_location=pytzimp.timezone(pytzimp.all_timezones[int(timezona)])
                convertido=d.astimezone(my_location)
                fmt = "%m-%d %H:%M"
                time=convertido.strftime(fmt)
		addDir('[B](' + str(time) + ')[/B] ' + team1 + team2,WiziwigURL + url,401,WiziwigURL + icon,len(eventos),True,parser='wiziwig',parserfunction='servers')
	except: addDir('[B](' + datefinal[1] + ' ' + time1 + ')[/B] ' + team1 + team2,WiziwigURL + url,401,WiziwigURL + icon,len(eventos),True,parser='wiziwig',parserfunction='servers')
    page_check = re.compile('<div class="stat">(.+?)pages(.+?)items</div>').findall(conteudo)
    if page_check:
        match = re.compile('.*href="(.+?)">&raquo;</a></li>').findall(conteudo)
        if match:
            addDir('[B][COLOR orange]Next page >>[/B][/COLOR]',WiziwigURL + match[0],401,os.path.join(current_dir,'icon.png'),1,True,parser='wiziwig',parserfunction='events')
    xbmc.executebuiltin("Container.SetViewMode(51)")
    
    
def wiziwig_servers(url):
	conteudo=clean(get_page_source(url))
	if re.search('Sorry, streams will only appear',conteudo):
		try:nrestacoes='[B]' + re.compile('</h2><p>There.+?<strong>(.+?) ').findall(conteudo)[0] + ' stations[/B] will broadcast the match.'
		except:nrestacoes=''
		xbmcgui.Dialog().ok(translate(40000),'Match links will only appear','one hour before the match',nrestacoes)
		sys.exit(0)
	ender=[]
	titulo=[]
	station_name=re.findall('stationname">(.+?)</td>(.*?)<td></td></tr><(?:tr class="broadcast|/tbody>)', conteudo, re.DOTALL)
	for station,html_trunk in station_name:
		streams=re.compile('.*?<tr class="streamrow[^"]*">\s*<td>\s*([^\s]+)\s*</td>\s*<td>\s*<a class="broadcast go" href="((?!adserver|http://torrent-tv.ru|forum|www\.bet365|BWIN)[^"]+)" target="_blank">Play now!</a>\s*<a[^>]*>[^>]*</a>\s*</td>\s*<td>([^<]+)</td>').findall(html_trunk)
		for nome,chid,quality in streams:
			if re.search('Sopcast',nome,re.IGNORECASE) or re.search('Acestream',nome,re.IGNORECASE) or re.search('TorrentStream',nome,re.IGNORECASE):
				if quality.replace(" Kbps","")[-1] != "1":
					titulo.append('['+station+'] ' + '[B][COLOR orange]' + nome +'[/B][/COLOR]'+ ' ('+quality+')')
					ender.append(chid)
				else: pass
	if len(ender)==0:xbmcgui.Dialog().ok(translate(40000),translate(40022));sys.exit(0)
	else:
		for i in xrange(0,len(titulo)):
			if re.search('acestream',titulo[i],re.IGNORECASE) or re.search('TorrentStream',titulo[i],re.IGNORECASE):
				addDir(titulo[i],ender[i],1,os.path.join(current_dir,'icon.png'),1,False)
			elif re.search('sopcast',titulo[i],re.IGNORECASE):
				addDir(titulo[i],ender[i],2,os.path.join(current_dir,'icon.png'),1,False)
	xbmc.executebuiltin("Container.SetViewMode(51)") 
