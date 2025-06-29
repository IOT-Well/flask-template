import hashlib


# 加密函数
def spw(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()  # 返回加密的密码
