import json
import datetime
import os

from logging import getLogger, config


# ファイルのパスを取得
file_path = os.path.dirname(__file__)

# configファイルを読み込む
with open(f'{file_path}/log_config.json', 'r') as f:
    log_conf = json.load(f)

# ファイル名をタイムスタンスで作成
log_conf['handlers']['routerHandler']['filename'] = \
    '{}/logs/log_test_2_{}.log'.format(file_path,
                                       datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d%H%M%S"))

# ロギング設定反映
config.dictConfig(log_conf)

logger = getLogger(__name__)

for cnt in range(20):
    logger.debug(f'test_2_a {cnt}')
    logger.info(f'test_2_b {cnt}')
    logger.warning(f'test_2_c {cnt}')
