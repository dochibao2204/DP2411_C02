# utf8 #

# # Bài 1: Lambda function
# #1. Dùng lambda function để làm các bài sau:

# y = lambda x: x*x
# print(y(5))  # Kết quả: 25

# # 2. Lọc ra các số âm trong một mảng cho trước.
# # Lọc các số lẻ từ danh sách
# numbers = [-1, 2, -3, 4, 5, -6, 7, 8, -9, 10]
# odd_numbers = list(filter(lambda x: x < 0, numbers))
# print(odd_numbers)  # Kết quả: [1, 3, 5, 7, 9]

# # 3. Hãy sắp xếp danh sách này tăng dần theo độ dài chuỗi.
# # Chuyển đổi độ dài các phần tử trong danh sách
# lengths = list(map(lambda x: len(x), ['apple', 'banana', 'cherry', 'orange', 'watermelon']))
# sort_lengths = sorted(lengths, key = (lambda x: x))
# print(lengths)  # Kết quả: [5, 6, 6]


# # lengths = list(map(lambda x: len(x), ['apple', 'banana', 'cherry', 'orange', 'watermelon']))
# lengths_fruit = ['apple', 'banana', 'cherry', 'coconut', 'watermelon', 'orange']
# sort_lengths_fruit = sorted(lengths_fruit, key = (lambda x: len(x)))
# print(sort_lengths_fruit)  # Kết quả: [5, 6, 6]

# ## Bài 2: Xử lý tập tin văn bản

# # 1. Đọc tập tin và đếm số dòng trong tập tin đó.
# f = open("demo2.txt", "r")
# count = 0
# while True:
#     line = f.readline()
#     count += 1
#     if line == '':
#         break
# print(count)
# f.close()

# 2. Đọc tập tin và xác định từ xuất hiện nhiều nhất.

f = open("demo2.txt", "r")
word_counts = {}

while True:
    line = f.readline()
    if line == '':  # Kết thúc tệp
        break
    
    # Tách từ và đếm
    words = line.strip().lower().split()  # Loại bỏ khoảng trắng thừa, chuyển thành chữ thường
    print(words)
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        # print(word_counts.get(word, 0))
f.close()

# Tìm từ xuất hiện nhiều nhất
most_common_word = max(word_counts, key=word_counts.get)
print(f"Từ xuất hiện nhiều nhất: '{most_common_word}' với tần suất {word_counts[most_common_word]}")
