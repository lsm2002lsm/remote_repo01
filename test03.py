"""
生成SECRET_KEY
"""
import os
import base64

tmp = os.urandom(44)
secret_key = base64.b64encode(tmp)
print(secret_key)
