from __future__ import annotations

from typing import Tuple, TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()

def render_bar(
    console: Console, current_hp: int,  maximum_hp: int, current_mp: int,  maximum_mp: int, current_exp: int, maximum_exp: int, total_width: int
) -> None:
    hp_bar_width = int(float(current_hp) /  maximum_hp * total_width)
    exp_bar_width = int(float(current_exp) /  maximum_exp * total_width)
    mp_bar_width = int(float(current_mp) /  maximum_mp * total_width)

    console.draw_rect(x=0, y=45, width=total_width, height=3, ch=1, bg=color.bar_empty)

    if hp_bar_width > 0:
        console.draw_rect(
            x=0, y=45, width=hp_bar_width, height=1, ch=1, bg=color.hp_bar_filled
        )
            
    if mp_bar_width > 0:
        console.draw_rect(
            x=0, y=46, width=mp_bar_width, height=1, ch=1, bg=color.mp_bar_filled
        )
    if exp_bar_width > 0:
        console.draw_rect(
            x=0, y=47, width=exp_bar_width, height=1, ch=1, bg=color.exp_bar_filled
        )
    console.print(x=1, y=45, string=f"HP: {current_hp}/{maximum_hp}", fg=color.bar_text)
    console.print(x=1, y=46, string=f"MP: {current_mp}/{maximum_mp}", fg=color.bar_text)
    console.print(x=1, y=47, string=f"EXP: {current_exp}/{maximum_exp}", fg=color.bar_text)

def render_dungeon_level(
    console: Console, dungeon_level: int, location: Tuple[int, int]
) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    console.print(x=x, y=49, string=f"Dungeon level: {dungeon_level}")

def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location)