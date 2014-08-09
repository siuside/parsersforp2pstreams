# -*- coding: utf-8 -*-
import xbmc,urllib

all_modules = [ 'https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2F1Torrent.tv','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FArenavision.in','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FLivefootball.ws','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FLivefootballaol.com','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FLivefootballvideo.com','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FRojadirecta.me','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FSopCast.ucoz','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FTorrent-tv.ru%20all','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FTorrent-tv.ru%20sports','https://code.google.com/p/parsersforp2pstreams/source/browse/#svn%2Fbranches%2FP2P-STREAMS-Parsers%2FWiziwig.tv']

for parser in all_modules:
    xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
    xbmc.sleep(1000)

xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('P2P-Streams', "All parsers imported",1,''))

