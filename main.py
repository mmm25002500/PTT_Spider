import requests
import bs4

allbbsUrl = 'https://www.ptt.cc/bbs/index.html'

bbsHtml = requests.get(allbbsUrl) 				#宣告ptt板網
bbsHtml.encoding = 'utf-8'					#設成utf-8
bbsbs = bs4.BeautifulSoup(bbsHtml.text,"html.parser")		#將ptt的html放入bbsbs
bbsa = bbsbs.find_all('a' , class_ = 'board')			#搜尋此html內所有的a標籤class為board的html放入bbsa
bbsdata = bbsbs.find_all(class_ = 'board-class')		#尋找此html內所有的class為board-class放入bbsdata
#print(bbsdata)							#測試用(debug)
a = 0								#宣告a為0
for BoardClass in bbsdata:					#將bbsdata放入BoardClass並執行迴圈
	#print("https://www.ptt.cc"+bbsa.find("a").get('href') , BoardClass.text.strip()) #有各板網址
	a +=1							#a++
	print(BoardClass.text.strip(), '(' + str(a) + ')' , end = ',' + '\t')	#印出板名並TAB
print()								#換行

whichBoard = input('請問你想選哪個板?')				#選板 使用者輸入
res = bbsdata[int(whichBoard)-1].text.strip()			#將板數字轉為整數且-1 並去掉html放入res(板名)
print(res)							#印出版名
boardAllInfo = bbsbs.find_all(class_ = 'board')			#搜尋板的所有板資訊放入boardAllInfo
boardInfo = str(boardAllInfo[int(whichBoard)-1])		#將指定板的資訊放入boardInfo
start = boardInfo.find('/bbs')					#設定初始值
end = boardInfo.find('html')+3					#設定終止值
list1 = boardInfo						#宣告list1為指定資訊
convertedIntStart = int(start)					#轉換為整數
convertedIntEnd = int(end) + 1					#轉換為整數
finalList = ''							#宣告最終串列為空
for getlist in range(convertedIntStart,convertedIntEnd):	#終止值-初始值為飯為放入getlist
	finalList = finalList + list1[getlist]			#最終串列 = 最終串列 + list1的索引getlist
print(finalList)						#印出最終串列(ptt指定板網址)



wherefile = input('你想存在哪裡?(Windows使用:C:\\目的地\\,Linux使用:/目的地/)(只需要有目錄即可 不需檔案)(沒有則enter)')
if wherefile == '' or wherefile == ' ':				#如果目的地為空
	saveFile = 'ptt.txt'					#宣告檔案儲存為ptt.txt
else:								#或者有的話
	saveFile = wherefile + '/ptt.txt'			#宣告檔案儲存為檔案目錄加上/ptt.txt
file = open(saveFile , 'w')					#尋找檔案 如沒有則創立一個





for i in range(1,7008):
        url = 'https://www.ptt.cc/bbs/Food/index'+str(i)+'.html'
        html = requests.get(url)
        html.encoding = "utf-8"
        bs = bs4.BeautifulSoup(html.text,"html.parser")
        data = bs.find_all("div", class_="title")
        text =  '-----------------------------' + '頁數' + str(i) + '\n'
        file.write(str(text))
        for i in data:
                print("https://www.ptt.cc"+i.find("a")['href'] , i.text.strip())
                text ="https://www.ptt.cc"+i.find("a")['href'] , i.text.strip()
                text = str(text) + '\n'
                file.write(str(text))
        print('-----------------------------')
file.close()
 
#Ask downloadNewOrAll
