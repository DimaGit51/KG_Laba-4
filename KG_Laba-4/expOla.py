def f():
    with open('text.txt', encoding='utf-8') as f:
        let = '!,."!@#$%^&*()-_='
        data=f.readline().lower()
        for i in range(len(let)):
            data=data.replace(let[i], '')
        data = data.split(' ')
        return data

def f1():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        processed_words = [word.lower().strip('.,:;!?') for word in words]
        return processed_words

print(f1())