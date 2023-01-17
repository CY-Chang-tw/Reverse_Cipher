#Owen @ Pycharm_2022/10/18
#HW02-Q5_7111056228

def reverse(plaintext):
    reversed_text = ''
    i = len(plaintext) - 1
    while i >= 0:
        reversed_text = reversed_text + plaintext[i]
        i -= 1
    print(f'The reversed text: {reversed_text}')



if __name__ == '__main__':
    text = input('Enter the text: ')
    reverse(text)


