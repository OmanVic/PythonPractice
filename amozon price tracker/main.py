# television = "https://www.amazon.com/amazon-fire-tv-43-inch-4-series-4k-smart-tv/dp/B0B3HG269B/ref=sr_1_1_sspa?keywords=smart+tv&qid=1684516422&sprefix=s%2Caps%2C1310&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySVA3UDBUTzc2MkxZJmVuY3J5cHRlZElkPUEwMzQ3MjkxMVdVSU1QV1RMV1pPMyZlbmNyeXB0ZWRBZElkPUEwMDYxMjk4NklMWlRCVjZMWDRTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

list_num = [1,2,6,2,3,7,7,5,7,6,2,7]
new = set(list_num)
list_new = sorted(list(new), reverse=True)
order_list = []
new_list = []
for item in list_new:
    count = 0
    for ite in list_num:
        if item == ite:
            count += 1
    order_list.append(count)

while order_list:
    frequency = max(order_list)
    max_index = order_list.index(frequency)
    number = list_new[max_index]
    new_list.append(number)
    order_list.remove(frequency)
    list_new.remove(number)
print(f"{list_num}=>{new_list}")