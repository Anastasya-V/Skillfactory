#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")



def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)



def game_core_v3(number):
    count = 1
    start = 1
    end = 100
    predict = (start + end) // 2
    while number != predict:
        if number > predict:
            start = predict + 1
            predict = (start + end) // 2
            count += 1
        elif number < predict:
            end = predict - 1
            predict = (start + end) // 2
            count += 1 
    return(count)

score_game(game_core_v3)


# In[ ]:





# In[ ]:




