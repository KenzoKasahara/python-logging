import os

from logging import getLogger, StreamHandler, FileHandler, Formatter


# ファイルのパスを取得
file_path = os.path.dirname(__file__)

# ロギング設定（親設定）
logger = getLogger(__name__)
logger.setLevel(10)    # [DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50]のいずれかを指定
format = "[%(levelname)-9s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s"

# 出力先の設定（子設定）
handler_str = StreamHandler()
handler_str.setLevel(20)    # [DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50]のいずれかを指定
handler_str.setFormatter(Formatter(format))

output_log_path = file_path + '/logs/log_test_1.log'
handler_file = FileHandler(filename=output_log_path, encoding="utf-8")
handler_file.setLevel(20)    # [DEBUG: 10, INFO: 20, WARNING: 30, ERROR: 40, CRITICAL: 50]のいずれかを指定
handler_file.setFormatter(Formatter(format))

# ロギング設定の適用
logger.addHandler(handler_str)
logger.addHandler(handler_file)
logger.propagate = False    # 親設定を引き継がない

logger.info('test1')
logger.debug('test2')
logger.warning('test3')
