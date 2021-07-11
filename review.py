import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1
        bar.update(count)
print('檔案讀取完了, 總共有', len(data), '筆資料')

print(data[0])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言平均長度為',sum_len/len(data))


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
        # good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言提到good')
print(good[0])

#文字計數
start_time = time.time()
wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))

while True:
    word = input('請你想查甚麼字： ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為： ', wc[word])
    else:
        print('這個字沒有出現過喔！')
print('感謝使用本查詢功能')
