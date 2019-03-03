# import urllib.request
#
# import json
#
# typeOfCurrency = "145"
# print(typeOfCurrency)
# api_endpoint = "http://www.nbrb.by/API/ExRates"
#
# url = api_endpoint + "/Rates/Dynamics/"+typeOfCurrency+"?startDate=2018-9-1&endDate=2018-9-30"
# response = urllib.request.urlopen(url)
# parseResponse = json.loads(response.read())
# Ratelist = []
# Dates = []
# getInf = ""
# for rate in parseResponse:
#     Ratelist.append(float(rate['Cur_OfficialRate']))
# for date in parseResponse:
#     Dates.append(str(date['Date'])[:10])
# if Ratelist[-1]>=Ratelist[-2]:
#     getInf = "возрастет"
# else:
#     getInf = "упадет"
