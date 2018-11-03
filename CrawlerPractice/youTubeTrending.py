import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from openpyxl import load_workbook

# parse DOM to 2 by 2 array
def _buildDataFrame(domList):
    dataList = []
    for dom in domList:
        aTagList = dom.find_all('a')
        liTagList = dom.find_all('li')

        title = aTagList[0]['title']
        link = aTagList[0]['href']
        channel = aTagList[1].text
        hits = int(liTagList[1].text.split('：')[1].split(' ')[0].replace(',', ''))
        startDate = liTagList[0].text

        dataList.append([title, 'www.youtube.com' + link, channel, hits, startDate])
    return dataList

# save to Excel with sheet name
def _saveToExcel(dataFrame, fileName, sheetName):
    exWriter = pd.ExcelWriter(fileName, engine='openpyxl')
    try:
        exBook = load_workbook(fileName)
        exWriter.book = exBook
        exWriter.sheets = dict((ws.title, ws) for ws in exBook.worksheets)
        dataFrame.to_excel(exWriter, sheetName)
    except:
        # if file not existed
        dataFrame.to_excel(exWriter, sheetName)
    finally:
        exWriter.save()
    _adjustColWidth(fileName)
    print('save to ' + fileName + ' success.')

# adjust Columns Width
def _adjustColWidth(fileName):
    mywb = load_workbook(fileName)
    mysheet = mywb.active
    mysheet.column_dimensions['A'].width = 5
    mysheet.column_dimensions['B'].width = 100
    mysheet.column_dimensions['C'].width = 40
    mysheet.column_dimensions['D'].width = 15
    mysheet.column_dimensions['E'].width = 15
    mywb.save(fileName)

# crawler
res = rq.get('https://www.youtube.com/feed/trending')
soup = BeautifulSoup(res.text, 'lxml')
domList = soup.select('.yt-lockup-content') #find all link of viedo tag
dataList = _buildDataFrame(domList)

# io, save to file
df = pd.DataFrame(dataList, columns=['Title', 'Link', 'Channel', 'Hits', 'StartDate'])
fileName = 'YouTubeTrending.xlsx'
today = datetime.date.today()
todayStr = today.year.__str__() + today.month.__str__() + today.day.__str__()
_saveToExcel(df, fileName, todayStr)