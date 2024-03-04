import os
import requests
import time
from dotenv import load_dotenv

def save_text_to_file(text: str, file_number: int) -> None:
    with open(f"diary_{file_number}.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

def main() -> None:
    load_dotenv(verbose=True)
    file_number = 1
    for page_number in range(3):
        response = requests.get(os.environ.get("DIARY_URL").format(page_number=page_number))
        text = response.content.decode('shift_jis')

        save_text_to_file(text, file_number)

        if (page_number + 1) % 25 == 0:
            file_number += 1

        print(f"Page {page_number} processed and saved to diary_{file_number}.txt")

        time.sleep(10)  # 10秒待機

if __name__ == "__main__":
    main()
