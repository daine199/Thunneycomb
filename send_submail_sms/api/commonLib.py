#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Daine.H

import random


def generate_verification_code(length=6):
    """
    用于生成验证码
    :param length: 生成期望长度验证码
    :return: 返回对应位数验证码
    """
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123):  # 对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    my_slice = random.sample(code_list, length)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(my_slice)  # list to string
    return verification_code

