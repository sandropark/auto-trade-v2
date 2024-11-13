from common.env_type import EnvType
import common.kis_common as common
import common.chat_client as chat_client
import time

# 영상과는 다르게 이 부분을 앞에 배치했습니다
time_info = time.gmtime()
m_hour = time_info.tm_hour

# 9시에만 내게 메시지를 보냅니다
# if m_hour == 0:
# chat_client.send_message("Server is OK")

chat_client.send_message("Server is OK")

# 실 계좌 모의 계좌의 토큰 값을 받아서 파일에 저장합니다.
common.make_token()
common.set_change_mode(EnvType.V)
common.make_token()
common.set_change_mode(EnvType.R)
