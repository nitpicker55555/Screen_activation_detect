from PIL import ImageGrab, ImageChops
import time

def get_screenshot():
    return ImageGrab.grab()

def active_pixels(img1, img2, threshold=5):
    """返回两图像之间差异超过阈值的像素数"""
    diff = ImageChops.difference(img1, img2)
    diff_data = diff.getdata()

    return sum(1 for pixel in diff_data if sum(pixel) > threshold)

def main():
    prev_screenshot = get_screenshot()
    while True:
        # time.sleep(1)  # 每秒检查一次
        current_screenshot = get_screenshot()
        active_count = active_pixels(prev_screenshot, current_screenshot)
        print(f"{active_count} active pixels detected")
        prev_screenshot = current_screenshot

if __name__ == "__main__":
    main()
