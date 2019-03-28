import sys
import os
import time
from pysideuic import compileUi as pyside_compileUi
from pyside2uic import compileUi as pyside2_compileUi

for _path in sys.argv[0:]:
    _dir, _file = os.path.split(_path)
    _name, _ext = os.path.splitext(_file)
    
    if _ext == ".ui":
        
        with open("%s\\%s_pyside.py" % (_dir,_name),"w") as f:
            pyside_compileUi(_path, f, False, 4,False)
            print ("%s\\%s_pyside.py" % (_dir,_name))

        with open("%s\\%s_pyside2.py" % (_dir,_name),"w") as f:
            pyside2_compileUi(_path, f, False, 4,False)
            print ("%s\\%s_pyside2.py" % (_dir,_name))
        
        time.sleep(1)