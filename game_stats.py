class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра запускается в неактивном положении
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, которая изменяется во время игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
