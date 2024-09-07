# python-logging

## log_test_1.py

1. スクリプト内でログ出力設定を定義
2. 「./logs」にログを出力

## log_test_2.py

1. 「log_config.json」でログ出力設定を定義
2. スクリプト内でconfigファイルを読み込み
3. 「./logs」にログを出力
4. ログルーティングを設定（1ファイル 512byte まで）
5. コンソールへ出力は「INFO以上」、ファイル出力は「DEBUG以上」
