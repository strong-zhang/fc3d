# -*- coding: utf-8 -*-
# 读写xlsx
import openpyxl
#import lottery3d
import pprint
from lottery3d import get_drop_directly
from lottery3d import get_drop_bypass
from lottery3d import get_number_form
from lottery3d import drop_directly_numbers
from lottery3d import number_form
from lottery3d import drop_bypass_numbers
from lottery3d import lottery_data_xlxs2txt

#data_row=[]
#data_tem=[]
lottery_date=[]
lottery_issue=[]
lottery_number=[]
lottery_sum=[]

def get_lottery_data():
	'''get data from txt'''
	excel_name = '2015'
	print('打开txt文件 ... ...')
	with open(excel_name+'.txt','r') as txt_file:
		print('读出数据 ... ...')
		for data_one in txt_file:	
			data_one = data_one.split()
		#	print(data_one)
			lottery_issue.append(data_one[0])
			lottery_date.append(data_one[1])
			lottery_number.append(data_one[2])
			lottery_sum.append(data_one[3])
	print('数据读取完成 ... ...')	
	lottery_issue.reverse()
	lottery_date.reverse()
	lottery_number.reverse()
	lottery_sum.reverse()

def print_lottery_data():
	'''print data'''
	for i in range(len(lottery_date)):
		print(i+1,end='\t')
		print(lottery_date[i],end='\t')
		print(lottery_issue[i],end='\t')
		print(lottery_number[i],end='\t')
		print(lottery_sum[i],end='\n')


#lottery_data_xlxs2txt()
get_lottery_data()
#print_lottery_data()
#input('wait...............................')
drop_directly_numbers(lottery_number[:])
#number_form(lottery_number[:])
#l = len(lottery_number)
#print(l)
#drop_bypass_numbers(lottery_number[:])


























input('wait...............................')
