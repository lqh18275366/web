import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.debug('this is a debug log')
logging.info('this is a info log')
logging.warning('this is a warning log')
logging.error('this is a erro log')
logging.critical('this is a critical log')

current_path = os.path.dirname(__file__)  #os.path.dirname():��һ��Ŀ¼������__file__:��ǰ�ļ���
print('current_path',current_path)