import pytest
import os,sys
from common.bases.get_config import read_config
from common.bases.get_log import Log

BASE_DIR = os.path.dirname(__file__)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'common/config/config.ini')
log_dir = read_config(conf_dir,"log","log_path")
img_dir = read_config(conf_dir,"img","img_path")
logger = Log(log_dir)

if __name__ == '__main__':
    pytest.main(['-s','-q','--alluredir=allure_results'])
    cmd = 'allure generate %s -o %s -c' % ('allure_results','test_report')
    os.system(cmd)