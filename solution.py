import pandas as pd
import numpy as np


chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    lamp_sum = np.sum(x)
    x = lamp_sum / (n * 40)
    return x.mean() # Ваш ответ
