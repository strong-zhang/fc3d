#import openpyxl


def drop_directly_numbers(test_num):
	'''numbers drop directly'''
	l = len(test_num)-1
	print('Drop directly data:total = ',l)
	
	total_count = 0
	sums = [0,0,0,0]
	number_count = []
	for i in range(4):
		number_count.append([[0,0,0],[0,0,0],[0,0,0]])
	
	for i in range(len(test_num)-1):
		nums = get_drop_directly(test_num[i],test_num[i+1])
		form_current = get_number_form(test_num[i])
		form_previous = get_number_form(test_num[i+1])
		number_count[nums][form_previous-1][form_current-1] += 1
	for i in range(4):
	 for j in range(3):
	  sums[i] += sum(number_count[i][j])
	print('drop/previous/current\tnumbers\t\tpercent\t\tpercentinall')
	for i in range(4):
		for j in range(3):
			print('')
			for k in range(3):
				n = number_count[i][j][k]
				total_count += n
				print('%d%d%d:\t\t\t%d\t\t%2.3f%%\t\t%2.3f%% '%(i,j+1,k+1,n,n*100/sums[i],n*100/l))
		print('drops %d in all is %d ,percent is %2.3f%%'%(i,sums[i],sums[i]*100/l))
	print(total_count)
	
	
def drop_bypass_numbers(test_num):
	'''numbers drop bypass'''
	l = len(test_num)-1
	print('Drop bypass data:total = ',l)
	
	total_count = 0
	sums =[0,0,0,0]
	number_count = []
	for i in range(4):
		number_count.append([[0,0,0],[0,0,0],[0,0,0]])
	
	for i in range(len(test_num)-1):
		nums = get_drop_bypass(test_num[i],test_num[i+1])
		form_current = get_number_form(test_num[i])
		form_previous = get_number_form(test_num[i+1])
		number_count[nums][form_previous-1][form_current-1] += 1
	for i in range(4):
	 for j in range(3):
	  sums[i] += sum(number_count[i][j])
	print('drop/previous/current\tnumbers\t\tpercent\t\tpercentinall')
	for i in range(4):
		for j in range(3):
			print('')
			for k in range(3):
				n = number_count[i][j][k]
				total_count += n
				print('%d%d%d:\t\t\t%d\t\t%2.3f%%\t\t%2.3f%% '
					%(i,j+1,k+1,n,n*100/sums[i],n*100/l))
		print(
			'drops %d in all is %d ,percent is %2.3f%%'
			%(i,sums[i],sums[i]*100/l))
	print(total_count)
	
def lottery_data_xlxs2txt():
	'''data xlxs2txt'''
	excel_name = '2018'
	#excel_name = '2015'
	sheet_name = '第一页'

	data_row=[]
	data_tem=[]
	
	print('打开xlsx文件 ... ...')
	wb  = openpyxl.load_workbook(excel_name+".xlsx")
	#for i in range(3,len(wb[sheet_name]['a'])):
	#for row in wb[sheet_name].rows:
	print('开始读取数据 ... ...')
	
	with open(excel_name+'.txt','w') as txt_file:
		for row in range(3,wb[sheet_name].max_row+1):
			data_row = [c.value for c in wb[sheet_name][row]]
			data_tem=[]
			for v in data_row:
				if v or v == 0:
					data_tem.append(v)
		#	print(data_tem)	
			if (int(data_tem[2])+int(data_tem[3])+int(data_tem[4]) == data_tem[5]):
				txt_file.write(data_tem[0]+'\t')
				txt_file.write(data_tem[1]+'\t')
				txt_file.write(data_tem[2]+data_tem[3]+data_tem[4]+'\t')
				txt_file.write(str(data_tem[5])+'\t')
				txt_file.write('\n')
			else:
				print('数据可能有错：',end='\t')
				print(data_tem)
		print('数据读取完成 ... ...')	

def get_drop_directly(current_numbers,previous_numbers):
	'''number drop directly'''
	numbers=0
	if not current_numbers.isdigit():
		return -1
	if len(current_numbers) != 3:
		return -2
	if not previous_numbers.isdigit():
		return -3
	if len(previous_numbers) != 3:
		return -4
	for n in current_numbers:
		if n in previous_numbers:
			numbers+=1
	return numbers
	
def get_drop_bypass(current_numbers,previous_numbers):
	'''number drop bypass'''
	numbers=0
	string_judge=''
	
	if not current_numbers.isdigit():
		return -1
	if len(current_numbers) != 3:
		return -2
	if not previous_numbers.isdigit():
		return -3
	if len(previous_numbers) != 3:
		return -4
		
	for n in previous_numbers:
		string_judge += str((int(n)+10-1)%10)
		string_judge += str((int(n)+10+1)%10)
	string_judge = sorted(set(string_judge))	
#	print(string_judge)

	for n in current_numbers:
		if n in string_judge:
			numbers+=1
	return numbers

def get_number_form(judge_number):
	'''number form'''
	if not judge_number.isdigit():
		return -1
	if len(judge_number) != 3:
		return -2
	return len(set(judge_number))

def number_form(test_numbers):
	'''numbers form'''
	l = len(test_numbers)
	print(l)
	print('total:\t',l)
	m1 = 0
	m2 = 0
	m3 = 0
	for i in test_numbers:
		n = get_number_form(i)
		if n == 3:
			m3 += 1
		elif n == 2:
			m2 += 1
		elif n == 1:
			m1 += 1
	print('m3:\t',str(m3),'\t',m3*100/l)
	print('m2:\t',str(m2),'\t',m2*100/l)
	print('m1:\t',str(m1),'\t',m1*100/l)
	

