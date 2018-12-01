#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import click
import hashlib,sys,click,re,base64,binascii,json,os
from Crypto.Cipher import AES
from http import cookiejar
import math,random,codecs
from seleinum import get_cookies
class Encrypto():
    # def __init__(self):
    #     self.modulus='b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    #     self.pubkey = '010001'
    #     self.nonce = '0CoJUm6Qyw8W8jud'

    # def get_random_str(self):
    #     '''
    #     获取随机16个字符串
    #     :return:
    #     '''
    #     res = ''
    #     for x in range(16):
    #         index = math.floor(random.random() * len(self.modulus))
    #         res+=self.modulus[index]
    #     # print(res)
    #     # print(bytes(res,encoding='utf-8'))
    #     return bytes(res,encoding='utf-8')

    # def get_random_str(self, size):
    #     return binascii.hexlify(os.urandom(size))[:16]
    #
    #
    # def aes_crypto(self,text,key):
    #     '''
    #     :param text:加密内容
    #     :param key:
    #     :return:
    #     '''
    #     pad = 16 - len(text) % 16
    #     text = text + chr(pad) * pad
    #     encrypto = AES.new(key.encode('utf-8'),AES.MODE_CBC,b'0102030405060708')
    #     ciphertext = encrypto.encrypt(text.encode('utf-8'))
    #     ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    #     return ciphertext
    # def rsa_encrpt(self,text,pubkey,modulus):
    #     text = text[::-1]
    #     rs = pow(int(binascii.hexlify(text),16),int(pubkey,16),int(modulus,16))
    #     return format(rs,'x').zfill(256)
    # def get_encry_request(self,text):
    #     text = json.dumps(text)
    #     sec_key = self.get_random_str(16)
    #     enc_text = self.aes_crypto(self.aes_crypto(text,self.nonce),sec_key.decode('utf-8'))
    #     enc_sec_key = self.rsa_encrpt(sec_key,self.pubkey,self.modulus)
    #     data={'params': enc_text,
    #           'encSecKey': enc_sec_key}
    #     print(data)
    #     return data


    def __init__(self):
        self.modulus='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce='0CoJUm6Qyw8W8jud'
        self.pub_key='010001'
        # 登录加密算法, 基于https://github.com/stkevintan/nw_musicbox脚本实现

    def encrypted_request(self, text):
        text=json.dumps(text)
        sec_key=self.create_secret_key(16)
        enc_text=self.aes_encrypt(self.aes_encrypt(text, self.nonce), sec_key.decode('utf-8'))
        enc_sec_key=self.rsa_encrpt(sec_key, self.pub_key, self.modulus)
        data={'params': enc_text, 'encSecKey': enc_sec_key}
        return data

    def aes_encrypt(self, text, secKey):
        pad=16 - len(text) % 16
        text=text + chr(pad) * pad
        encryptor=AES.new(secKey.encode('utf-8'), AES.MODE_CBC, b'0102030405060708')
        ciphertext=encryptor.encrypt(text.encode('utf-8'))
        ciphertext=base64.b64encode(ciphertext).decode('utf-8')
        return ciphertext

    def rsa_encrpt(self, text, pubKey, modulus):
        text=text[::-1]
        rs=pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def create_secret_key(self, size):
        return binascii.hexlify(os.urandom(size))[:16]





class Song():
    '''
    歌曲信息：
    '''
    def __init__(self):
        self.song_id = song_id
        self.song_name = song_name
        self.song_num = song_num
        self.song_url = '' if song_url else None



class Crawl():
    '''
    163 API
    '''
    def __init__(self,timeout=60,cookie_path='.'):
        self.headers ={
            'Accept':'*/*',
            'Connection':'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host':'music.163.com',
            'Origin':'https://music.163.com',
            'Referer':'https://music.163.com/search/',
            'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'
        }
        self.session = requests.session()
        self.session.headers.update(self.headers)
        cookie = get_cookies()
        self.session.cookies.update(cookie)
        # cookie_path = self.cookie_to_txt(cookie_path,)
        # self.session.cookies.load(f0ilename=twcookie_path,ignore_discard=True)
        self.Downing_session = requests.session()
        self.timeout = timeout
        self.ep = Encrypto()
    def post_request(self,url,param):
        data = self.ep.encrypted_request(param)
        res = self.session.post(url,timeout=self.timeout,data=data)
        result = res.json()
        if res.status_code != 200:
            print('请求失败....')
        else:
            # print(result)
            return result
    def search_songs(self,name,limit=9,quite=True):
        params={'s': name, 'type': 1, 'offset': 0, 'sub': 'false', 'limit': limit}

        url='http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        result = self.post_request(url,params)
        if int(result['result']['songCount']) <= 0:
            print(f'没有搜索到{name}歌曲.......：')
        else:
            songs = result['result']['songs']
            if quite:
                song ={
                    'song_id':songs[0]['id'],
                    'song_name':songs[0]['name'],
                    # 'song_num':song_num
                }
                print(song)
                return song

    def get_song_url(self, name,bit_rate=320000):
        """
        获得歌曲的下载地址
        :params song_id: 音乐ID<int>.
        :params bit_rate: {'MD 128k': 128000, 'HD 320k': 320000}
        :return: 歌曲下载地址
        """
        url='http://music.163.com/weapi/song/enhance/player/url?csrf_token='
        csrf=""
        self.song = self.search_songs(name)
        # params={'ids': int(song['song_id']), 'br': bit_rate,'csrf_token': csrf}
        #553755659  1316256535
        params = {"ids": [self.song['song_id']],"br": bit_rate,"csrf_token": csrf}
        #http://m10.music.126.net/20181122111255/ba3063d4a368f5e4d2006b1e3fc6adb4/ymusic/341e/9cc2/7c4f/b13ac6e62d3625524dde95fd1b1628bf.mp3
        result=self.post_request(url, params)
        # 歌曲下载地址
        song_url = result['data'][0]['url']
        # 歌曲不存在
        if song_url is None:
            print(f'Song {self.song["song_name"]} is not available due to copyright issue.')
        else:
            self.song_url = song_url
            return self.song_url
    def get_song_file(self,song_path,song_num):
        if not os.path.exists(song_path):
            os.mkdir(song_path)
        fpath = os.path.join(song_path,str(song_num)+ '_'+ self.song['song_name'] + '.mp3')

        resp = self.Downing_session.get(url=self.song_url,timeout=self.timeout,stream=True)
        length = int(resp.headers.get('content-length'))
        lable = f'正在下载{self.song["song_name"]} {int(length/1024/1024)}Mb'
        with click.progressbar(length=length,label=lable) as progress:
            with open(fpath,'wb') as f:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                            f.write(chunk)
                            progress.update(1024)
    def get_song_list(self,url):
        '''
        获取歌单
        :param url: 歌单地址
        :return: 歌单详情
        '''
        headers= \
            {
                'Accept': '*/*',
                'Connection': 'keep-alive',
                # 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'music.163.com',
                'Referer': 'https://music.163.com',
                # 'Cookie': 'JSESSIONID-WYYY=61uNhw%2F7lJWI81%2FetZG%2Bm%2BU40hGQ03TenC5MXj%2BklHMDgIjhWBRQYXKaUChc7j05hXDRheC7Dfv5bby%5C2hIfhDtSJkv2ekIYJDASrEJy7VUIzubTvsrO4ol7DBMyw%2FJ2C8u4EiU0OFYT16CmqWy6MYhCVXYQ5RT0dyE%5CCEea4b2jZ8j2%3A1542953060135; _iuqxldmzr_=32; _ntes_nnid=25e41a1bd9229a2ebde3d102091fe7b4,1542951260192; _ntes_nuid=25e41a1bd9229a2ebde3d102091fe7b4; __utma=94650624.1755983951.1542951261.1542951261.1542951261.1; __utmc=94650624; __utmz=94650624.1542951261.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=kT6v3t8zt8GtbeL5dVlkPw5dd2n0AkPJy6XzCXypvrwVGUNYCXwMiZh4TNjVlG%2FJ1UAuq2xMQGv%2F5GZ32v4xP%2B9mDOJU7PWdUs0wKOGs2TXNlrR3%2BxPpxJGcWNeLjXSvWXc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82fb5b82eca193d88086b08ba2d55a979f8b85b76fbcabbfb6e121f1a9bb82b82af0fea7c3b92aa98cfa97b280fca6bcd9c680a2bb84d6e75eb0b5a098b870a8eea2d1c4619496b7d7db728188b791f57ab58a89b6cd538188b9aeec52acec9cafe95eb099e1abb45f83abbfd3fb479399bad0b84d9aedfe97b77494f5f78ec7458a8bf9b1d67097ad0098ca4585adfeb5db46b0ae9ed4aa7494b0b8abc6699592abade95491aa99b9e237e2a3; WM_TID=%2BN8I9s5U0AtAVARREFcsKkq6RLr2greo; __utmb=94650624.9.10.1542951261',
                'Referer': 'https://music.163.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

            }
        res=self.session.get(url=url,headers=headers)
        # res=requests.get(url=url, headers=headers)
        html=res.text
        res=re.findall(r'<li><a href=".*?">(.*?)</a></li>', html, re.S)[0:-2]
        with open('/soft/demo/music_list', 'a+') as f:
            for i in res:
                f.writelines(i + '\n')

if __name__ == '__main__':
    Wangyi = Crawl()
    URL = 'https://music.163.com/playlist?id=2201873658'
    Wangyi.get_song_list(url=URL)
    with open('/soft/demo/music_list', 'r') as f:
        music_list=list(map(lambda x: x.strip(), f.readlines()))
    for song_num, song_name in enumerate(music_list):
        Wangyi.get_song_url(song_name)
        Wangyi.get_song_file('/soft/demo/songs/',song_num)


  #https://music.163.com/#/artist?id=8103  #'http://m10.music.126.net/20181122113251/69f80996d95213995fb02711eb515d21/ymusic/535c/510c/555d/d610670c7effa1916ca9b76a232293c5.mp3'
    # Wangyi.search_songs()
    # URL = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='

    # Wangyi.post_request(url,params)


