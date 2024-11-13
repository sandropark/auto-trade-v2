from common import kis_common as common
from common import kis_api_helper_us as kis_us
from common import kis_api_helper_kr as kis_kr

import pprint
import time

from common.env_type import EnvType

#통합증거금을 사용하시는 분은 강의 영상을 잘 봐주세요!!

#REAL 실계좌 VIRTUAL 모의 계좌
# common.set_change_mode("REAL") 


#현재 장이 열렸는지 여부
# if kis_us.IsMarketOpen() == True:
#     print("Maket is Open!!")
# else:
#     print("Maket is Closed!!")

# common.set_change_mode(EnvType.V)

# print(common.get_now_dist())

# print(common.get_app_key())

# print(common.get_token())
'''

print("                                     ")
print("-----------삼성 전자 일봉 -------------")
print("                                     ")

#삼성전자의 일봉 정보를 100개까지 가져올 수 있다
pprint.pprint(kis_kr.GetOhlcv("005930","D"))

print("                                     ")
print("-----------삼성 전자 월봉 -------------")
print("                                     ")


pprint.pprint(kis_kr.GetOhlcv("005930","M"))

print("                                     ")
print("-----------삼성 전자 년봉 -------------")
print("                                     ")


pprint.pprint(kis_kr.GetOhlcv("005930","Y"))



print("                                     ")
print("----------애플 일봉---------------")
print("                                     ")


#애플의 일봉 정보를 100개까지 가져올 수 있다
pprint.pprint(kis_us.GetOhlcv("AAPL","D"))



print("                                     ")
print("----------애플 월봉---------------")
print("                                     ")


pprint.pprint(kis_us.GetOhlcv("AAPL","M"))


print("                                     ")
print("----------애플 년봉---------------")
print("                                     ")
print(" 이건 가져올 수 없음 ")
#영상과는 다르게 미국주식의 경우 년봉은 가져올 수 없어요
#내부적으로 수정주가(액면분할 반영)를 가져오도록 API를 변경했기 때문이예요 (해당 API가 년봉 미지원)
#pprint.pprint(kis_us.GetOhlcv("AAPL","Y"))
'''
'''

print("                                     ")
print("--------TQQQ는 한투에 없다 -------------")
print("                                     ")



pprint.pprint(kis_us.GetOhlcv("TQQQ","D"))




print("                                     ")
print("----------삼성전자 일봉 가져오기--------------")
print("                                     ")

print(" 한투 ")
pprint.pprint(kis_kr.GetOhlcv("005930","D"))

print(" FinanceDataReader ")

pprint.pprint(common.GetOhlcv1("KR","005930"))

print(" Yahoo ")

pprint.pprint(common.GetOhlcv2("KR","005930"))





print("                                     ")
print("----------애플 일봉 가져오기--------------")
print("                                     ")

print(" 한투 ")
pprint.pprint(kis_us.GetOhlcv("AAPL","D"))

print(" FinanceDataReader ") 
# 22년 10월 24일 현재 FinanceDataReader가 사용하는 인베스팅 닷컴의 크롤링이 막힌 상태입니다.
# https://github.com/financedata-org/FinanceDataReader/issues/166 여기를 참고하세요!
# https://github.com/financedata-org/FinanceDataReader/wiki/Release-Note-0.9.50 이 버전으로 해결이 되며 아래 라인이 만약에 에러가 나면
# sudo pip3 install --upgrade finance-datareader 로 업데이트 해주세요!
pprint.pprint(common.GetOhlcv1("US","AAPL"))

print(" Yahoo ")

pprint.pprint(common.GetOhlcv2("US","AAPL"))
'''




# pprint.pprint(common.GetOhlcv("KR","005930"))
# pprint.pprint(common.GetOhlcv("US","TQQQ"))


