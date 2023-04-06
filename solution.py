import pandas as pd
import numpy as np


chat_id = 417796486 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    y = exp(x - 315)
    y = sum(y) / len(x)
    return y # Ваш ответ
