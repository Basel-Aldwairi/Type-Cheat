import pyautogui
import pytesseract


def get_text():
	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

	region = (50,740,1755,130)
	screenshot = pyautogui.screenshot(region=region)

	screenshot.save("screenshot.png")

	text = pytesseract.image_to_string(screenshot)
	# print(text)
	return text
	# print('Extracted text = ',text)