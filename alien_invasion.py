import sys

import pygame

class AlienInvasion:
  # ゲームのアセットと動作を管理する全体的なクラス

  def __init__(self):
    # ゲームを初期化してゲームのリソースを作成する
    pygame.init()

    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("エイリアン侵略")

    # 背景色を設定する
    self.bg_color = (230, 230, 230)

  def run_game(self):
    # ゲームのメインループを開始する
    while True:
      # キーボードとマウスのイベントを監視する
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # ループを通過するたびに画面を再描画する
      self.screen.fill(self.bg_color)

      # 最新の状態の画面を表示する
      pygame.display.flip()

if __name__ == '__main__':
  # ゲームのインスタンスを作成し、ゲームを実行する
  ai = AlienInvasion()
  ai.run_game()
