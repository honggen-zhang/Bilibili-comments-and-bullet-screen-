#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:57:27 2021

@author: hongggenzhang
"""

import requests
import os
import re
import jieba
import sys
import wordcloud
import time
from bs4 import BeautifulSoup
import pandas as pd
class Bilibili:
	def __init__(self, videourl,page):

		#self.img_path=img_path
		self.baseurl=videourl.split('?')[0]
	# scraping comments and bullet screen 
	def getAidAndCid(self):
		cidurl=self.baseurl+"?p="+page
		cidRegx='{"cid":([\d]+),"page":%s,'%(page)
		aidRegx='"aid":([\d]+),'
		r=requests.get(cidurl)
		r.encoding='utf-8'
		try:

			self.cid=re.findall(cidRegx, r.text)[0]
			self.aid=re.findall(aidRegx, r.text)[int(page)-1]
		except:
			print('The no. of video is not right！')
			time.sleep(3)
			sys.exit()


	def getBarrage(self):
		print('Scraping......')
		
		commentUrl='https://comment.bilibili.com/'+self.cid+'.xml'
		r=requests.get(commentUrl)
		r.encoding='utf-8'
		content=r.text
		comment_list=re.findall('>(.*?)</d><d ',content)
		text_all = []
		for com in comment_list:
            
			data = {}
			data['barrage'] = com
			text_all.append(data)
		df = pd.DataFrame.from_dict(text_all)
		df.to_csv('/Users/hongggenzhang/Desktop/yezhang/text/barrage_2.csv')
		self.barrage="".join(comment_list)

	def getComment(self,x,y):
		text_all = []
		#file1 =  open('/Users/hongggenzhang/Desktop/yezhang/text/file.txt','rb')
		for i in range(x,y+1):
			r=requests.get('https://api.bilibili.com/x/v2/reply?pn={}&type=1&oid={}&sort=2'.format(i,self.aid)).json()
			replies=r['data']['replies']
			print('------comments sheet------')
			for repliy in replies:
				data = {}
				data['comment'] = repliy['content']['message']
				text_all.append(data)
				#file1.writelines(repliy['content']['message']+'\n')
				#print(repliy['content']['message']+'\n')
		df = pd.DataFrame.from_dict(text_all)
		df.to_csv('/Users/hongggenzhang/Desktop/yezhang/text/comments_2.csv')
                

		pass

def checkUrl(url):
	try:
		r=requests.get(url)
	except:
		return 0
	r.encoding='utf-8'
	regx='"part":"(.*?)"'
	r.encoding='utf-8'
	result=re.findall(regx, r.text)
	count=0
	if len(result)>0:
		print('------video sheet------')
		for i in result:
			count+=1
			print("video"+str(count)+" : "+i)
		return 1
	return 0
		
if __name__=='__main__':
	videourl=input("please input url")

	if checkUrl(videourl):
		print('------valid------')
		page=input('no. video：')
		start_time=time.time()
		b=Bilibili(videourl, page)
		b.getAidAndCid()

		# get bullet screen 
		#b.getBarrage()

		# get comments from staring to end page
		b.getComment(1, 200)


		print('Success，Time costing:{:.2f}s'.format(time.time()-start_time))
	else:
		print('Invalid video')





