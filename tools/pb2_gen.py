import os

os.chdir('proto\\')
for fname in os.listdir('.'):
    print fname
    if '.proto' == fname[-6:]:
        os.system('protoc %s --python_out output\\'%fname)
    