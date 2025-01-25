import os

current_dir = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(current_dir, '..', "..", "assets", "images")

class Piece:
    def __init__(self, id, name, color, asset, value=None, texture_rect=None):
        self.id = id
        self.name = name
        self.color = color
        self.value = value
        self.texture_size = 80
        self.asset = os.path.join(ASSETS_DIR, "80px", asset)
        self.texture_rect = texture_rect
    
    def update_asset_size(self, size):
        asset = self.asset.split(os.sep)
        self.asset = os.path.join(current_dir, '..', "..", "assets", "images", f"{size}px", asset)        
        

