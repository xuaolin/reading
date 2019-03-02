data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('档案读取完毕，总共有', len(data), '个档案')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('the average words for each review is', sum_len/len(data))

