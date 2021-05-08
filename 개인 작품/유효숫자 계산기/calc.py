print('1. 더하기 2. 곱하기')
mode = int(input())

if mode == 1:
	
	k = 0
	j = 0
	k_1 = -1
	j_1 = -1
	
	print('더하기')
	
	num1 = float(input())
	num2 = float(input())
	
	num_1 = list(str(num1))
	num_2 = list(str(num2))
	
	while True:
		if num_1[k] == '.':
			k_1 = k
			num_12 = num_1
			del num_12[0:k_1 + 1]
		
		if num_2[j] == '.':
			j_1 = j
			num_22 = num_2
			del num_22[0:j_1 + 1]
			
		if k_1 != -1 and j_1 != -1:
			l_1 = len(num_1)
			l_2 = len(num_2)
			break
		
		if k_1 == -1:
			k += 1
		
		if j_1 == -1:
			j += 1
	
	if l_1 > l_2:
		print(round(num1 + num2, l_2))
	if l_1 <= l_2:
		print(round(num1+num2, l_1))
	
elif mode == 2:
        print('곱하기')
		
        num1, num2 = input('실수 두 개를 공백을 두고 입력하시오: ').split()

        num_1 = float(num1)
        num_2 = float(num2)

        num_1_1, num_1_2 = num1.split('.')
        num_2_1, num_2_2 = num2.split('.')

        lena = len(num_1_1) + len(num_1_2)
        lenb = len(num_2_1) + len(num_2_2)

        if lena >= lenb:
            lenValue = lenb
        elif lena < lenb:
            lenValue = lena

        # print(lena, lenb, lenValue)

        value = num_1*num_2
        value1, value2 = str(value).split('.')

        value_1 = int(value1)
        value_2 = int(value2)

        lenva = len(str(value_1))
        lenvb = len(str(value_2))

        # print(value_1, value_2, lenva, lenvb)

        lenV = lenva + lenvb
        
        if lenV >= lenValue:
            vvalue = int(round(value_2/(10**(lenV-lenValue)), 0))
            # print(vvalue)
            print('{}.{}'.format(value_1, vvalue))
