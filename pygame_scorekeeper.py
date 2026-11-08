import pygame
import json
import os

class ScoreManager:
    """Handles current score, high score loading, and persistent saving for 2D games."""
    def __init__(self, save_filename="highscore.json"):
        self.save_filename = save_filename
        self.score = 0
        self.high_score = self.load_high_score()

    def add_score(self, points):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score

    def reset_score(self):
        self.score = 0

    def load_high_score(self):
        if os.path.exists(self.save_filename):
            try:
                with open(self.save_filename, "r") as file:
                    data = json.load(file)
                    return data.get("high_score", 0)
            except (json.JSONDecodeError, IOError):
                return 0
        return 0

    def save_high_score(self):
        try:
            with open(self.save_filename, "w") as file:
                json.dump({"high_score": self.high_score}, file)
        except IOError as e:
            print(f"Error saving high score: {e}")

# Quick Pygame text render snippet for integration
def render_score_ui(surface, font, score_manager, color=(255, 255, 255), position=(20, 20)):
    score_str = f"Score: {score_manager.score}  |  Best: {score_manager.high_score}"
    text_surface = font.render(score_str, True, color)
    surface.blit(text_surface, position)
