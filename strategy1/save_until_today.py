#coding: utf-8

from db import get_hs300_tickers,get_ticker_info_by_id,save_ticker_into_db,fresh_last_updated_date,get_last_updated_date
import datetime


if __name__ == '__main__':
	#hs300的id
	ticker_info = get_hs300_tickers()
	for i in range(len(ticker_info)):
		ticker = ticker_info[i]
		ticker_id = ticker[1]
		ticker_name = ticker[2]
		vendor_id = i;

		print '============== %s ====== 正在获取%s == %s ================'%(i,ticker_name,ticker_id)

		#更新last_update_date
		fresh_last_updated_date(ticker_id)

		#获取
		ticker_data = get_ticker_info_by_id(ticker_id)

		#存储
		save_ticker_into_db(ticker_id,ticker_data,vendor_id)
		break
