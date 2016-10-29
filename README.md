# bizmsg-client-python

bizmsg object 선언시 api_key 삽입

ex) bizmsg = Bizmsg(api_key=TEST_API_KEY)

send_bizmsg 사용시 전화번호, 메세지, 메세지 템플릿 코드 3가지 인풋

ex) result = bizmsg.send_bizmsg(PHONE_NUM, MSG, TEMPLATE_CODE)
