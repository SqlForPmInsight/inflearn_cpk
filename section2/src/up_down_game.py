import tkinter as tk
import random
import sys

answer = random.randint(1, 100)
tries = 0

def check():
    global tries
    guess = int(entry.get())
    tries += 1
    if guess < answer:
        result['text'] = 'Up'
    elif guess > answer:
        result['text'] = 'Down'
    else:
        result['text'] = f'정답! 시도 횟수: {tries}'
        if sys.platform == 'darwin':
            root.bell()
        else:
            print('\a')
        entry.config(state='disabled')
        btn.config(state='disabled')

root = tk.Tk()
root.title('업앤다운 게임')

label = tk.Label(root, text='1~100 사이 숫자 입력:')
label.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text='확인', command=check)
btn.pack()

result = tk.Label(root, text='')
result.pack()

root.mainloop()
