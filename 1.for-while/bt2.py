#%% [markdown]
# Mô phỏng búng đồng xu
# 
# Chúng ta sẽ mô phỏng việc búng đồng tiền xu để hiểu hơn về hàm random.random(). Đồng tiền xu có 2 mặt, mặt trước và mặt sau. Chương trình được yêu cầu đếm số lần xuất hiện của mặt trước và mặt sau cho 1000 lần thử.
# 
# Chúng ta sẽ dùng vòng lặp for, mỗi lần lặp, chương trình sẽ tạo ra 1 số ngẫu nhiên n nằm trong khoảng 0 và 1 bằng hàm random.random(). Mặt sau xuất hiện khi n < 0.5, và ngược lại, mặt trước xuất hiện. Sau 1000 lần thử, in số lần xuất hiện mặt trước và mặt sau.
# 
# Thảo luận
# 
# 1) Hàm random.random() sinh ra số ngẫu n có phân bố đều (uniform distribution) trong khoảng `[0,1)` (không bao gồm số 1).
# 
# 2) Mặt sau xuất hiện khi n < 0.5. Điều này đồng nghĩa với việc miền giá trị cho việc mặt sau xuất hiện là một đoạn [0, 0.5). Lập luận tương tự, miền giá trị cho việc mặt trước xuất hiện là [0.5, 1).
# 
# 3) Theo xác suất, khi số lần thử đủ lớn thì số lần xuất hiện mặt trước và mặt sau sẽ xấp xỉ bằng nhau vì miền giá trị của 2 trường hợp bằng nhau.

#%%
import random

def side_coin(n):
  up_side = 0
  down_side = 0
  for i in range(n):
    side = random.random()
    if side < 0.3:
      down_side += 1
    elif side < 0.7:
      down_side += 0
      up_side += 0
    elif side <= 1:
      up_side += 1
  
  return "upside: ", up_side, "downside: ", down_side
  





#%%
side_coin(1000)