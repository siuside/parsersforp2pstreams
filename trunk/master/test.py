 # -*- coding: utf-8 -*-
import xbmc,urllib

all_modules = [ 'https://code.google.com/p/parsersforp2pstreams/source/browse/branches/P2P-STREAMS-Parsers/1Torrent.tv/onetorrenttv.tar.gz','https://code.google.com/p/parsersforp2pstreams/source/browse/branches/P2P-STREAMS-Parsers/Arenavision.in/arenavision.tar.gz','https://code.google.com/p/parsersforp2pstreams/source/browse/branches/P2P-STREAMS-Parsers/Livefootball.ws/livefootballws.tar.gz']

for parser in all_modules:
    xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
    xbmc.sleep(1000)

xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('P2P-Streams', "All parsers imported",1,''))