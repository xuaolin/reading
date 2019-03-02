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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔短留言')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are total', len(good), 'good reviews!')

good = [d for d in data if 'good' in d]
print(len(good)) #advanced way to make good list, function the same as the line 22-26

bad = []
bad = [d for d in data if 'bad' in d]
print(len(bad)) #filter all the bad review and output the counting number