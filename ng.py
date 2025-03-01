import sys
import time
import pygame  # Thêm thư viện pygame

# Khởi tạo pygame mixer
pygame.mixer.init()

# Phát nhạc nền
pygame.mixer.music.load("music.mp3")  # Thay bằng file nhạc của bạn
pygame.mixer.music.play(-1)  # Lặp vô hạn

lyrics = """
Cuộc gọi nhỡ cho em hàng đêm
                         đến tận 200 lần  
Dòng ký ức trong em về anh
                         bây giờ đang phai dần  
Quay gót rời đi
                 không để lại gì  
Bay vút qua tầm tay  
                          Sao còn vương vấn để làm gì?  

Bọn mình kết thúc thật rồi
        hết sức thật rồi  
         Phải không em ơi?  
Chuyện tình có khúc phải lòng
         có lúc phải rời  
         Vậy đến lúc rồi  
Và có lẽ giờ này
        em đã ngủ say  
        Còn anh thì vẫn mang  
Nỗi nhớ em trong đêm thật dài  
                        Thêm lý do cho anh tồn tại  
Để lại chạm vào bờ môi ấy dịu dàng  
                        Lời thì thầm ngọt ngào bên tai  
Ta mất nhau thật rồi em ơi  
        Tan vỡ hai cực đành chia đôi  
Anh sẽ luôn ghi nhớ em 
        trong từng tế bào  
Vậy mà dừng lại như thế sao  
                          Trong anh hay là trong em 
đã đổi thay bao nhiêu suy nghĩ  
                          Yêu thương nay còn đâu  
        Anh còn yêu, nghe hơi vô lý  
Ta mất kết nối thật rồi  
        Đã mất kết nối thật rồi em ơi  
Trong anh hay là trong em 
        đã đổi thay bao nhiêu suy nghĩ  
Yêu thương nay còn đâu  
        Anh còn yêu, nghe hơi vô lý  
Ta mất kết nối thật rồi  
        Đã mất kết nối thật rồi em ơi  
        Ta mất nhau thật rồi em ơi  
        Tan vỡ hai cực đành chia đôi  
        Anh sẽ luôn ghi nhớ em trong từng tế bào  
        Vậy mà dừng lại như thế sao  
"""

# Chạy hiệu ứng chạy chữ
for char in lyrics:
    print(char, end='', flush=True)
    time.sleep(0.05)  # Điều chỉnh tốc độ chạy chữ

# Giữ chương trình chạy để nhạc không bị dừng
while pygame.mixer.music.get_busy():
    time.sleep(5)