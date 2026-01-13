
#RecipeBook - Пакет для управления кулинарными рецептами.

version = "1.0.0"
author = "Наторова Евгения Михайловна"
email = "nzena605@gmail.com"

from .ingredient import Ingredient
from .recipe import Recipe
from .cookbook import Cookbook


__all__ = ['Ingredient', 'Recipe', 'Cookbook']
