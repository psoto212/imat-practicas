import copy

class WolfGoatCabbageWorld:
    def __init__(self, state):
        # el estado se representa como (left_side, right_side), cada uno un set
        self.state = tuple(set(x) for x in state)  # ejemplo inicial: (['👨🏻','🐺','🐐','🥦'],[])
        self.actions = [
            'MOVE_FARMER_FROM_LEFT_TO_RIGHT',
            'MOVE_FARMER_FROM_RIGHT_TO_LEFT',
            'MOVE_CABBAGE_AND_FARMER_FROM_LEFT_TO_RIGHT',
            'MOVE_CABBAGE_AND_FARMER_FROM_RIGHT_TO_LEFT',
            'MOVE_GOAT_AND_FARMER_FROM_LEFT_TO_RIGHT',
            'MOVE_GOAT_AND_FARMER_FROM_RIGHT_TO_LEFT',
            'MOVE_WOLF_AND_FARMER_FROM_LEFT_TO_RIGHT',
            'MOVE_WOLF_AND_FARMER_FROM_RIGHT_TO_LEFT'
        ]

    # mover un elemento de una orilla a otra
    def move(self, state, what, where_from, where_to):
        state[where_from].remove(what)
        state[where_to].add(what)

    # posibles transiciones de estado según acción
    def get_next_state(self, starting_state, action):
        next_state = copy.deepcopy(starting_state)
        left_side, right_side = next_state[0], next_state[1]

        if action == 'MOVE_FARMER_FROM_LEFT_TO_RIGHT':
            if '👨🏻' in left_side:
                self.move(next_state, '👨🏻', 0, 1)

        if action == 'MOVE_FARMER_FROM_RIGHT_TO_LEFT':
            if '👨🏻' in right_side:
                self.move(next_state, '👨🏻', 1, 0)

        if action == 'MOVE_GOAT_AND_FARMER_FROM_LEFT_TO_RIGHT':
            if {'👨🏻', '🐐'} <= left_side:
                self.move(next_state, '👨🏻', 0, 1)
                self.move(next_state, '🐐', 0, 1)

        if action == 'MOVE_WOLF_AND_FARMER_FROM_LEFT_TO_RIGHT':
            if {'🐺','👨🏻'} <= left_side:
                self.move(next_state, '👨🏻', 0, 1)
                self.move(next_state, '🐺', 0, 1)

        if action == 'MOVE_CABBAGE_AND_FARMER_FROM_LEFT_TO_RIGHT':
            if {'🥦','👨🏻'} <= left_side:
                self.move(next_state, '👨🏻', 0, 1)
                self.move(next_state, '🥦', 0, 1)

        if action == 'MOVE_GOAT_AND_FARMER_FROM_RIGHT_TO_LEFT':
            if {'🐐','👨🏻'} <= right_side:
                self.move(next_state, '👨🏻', 1 ,0)
                self.move(next_state, '🐐', 1, 0)

        if action == 'MOVE_WOLF_AND_FARMER_FROM_RIGHT_TO_LEFT':
            if {'🐺','👨🏻'} <= right_side:
                self.move(next_state, '👨🏻', 1, 0)
                self.move(next_state, '🐺', 1, 0)

        if action == 'MOVE_CABBAGE_AND_FARMER_FROM_RIGHT_TO_LEFT':
            if {'🥦','👨🏻'} <= right_side:
                self.move(next_state, '👨🏻', 1, 0)
                self.move(next_state, '🥦', 1, 0)

        return next_state


# función para verificar si un estado es seguro
def safe(state):
    left_side, right_side = state[0], state[1]

    wolf_goat_alone = (
        {'🐺', '🐐'} <= left_side and '👨🏻' not in left_side
    ) or (
        {'🐺', '🐐'} <= right_side and '👨🏻' not in right_side
    )

    goat_cabbage_alone = (
        {'🥦', '🐐'} <= left_side and '👨🏻' not in left_side
    ) or (
        {'🥦', '🐐'} <= right_side and '👨🏻' not in right_side
    )

    return not (wolf_goat_alone or goat_cabbage_alone)


# ejemplo de uso
world = WolfGoatCabbageWorld((['👨🏻', '🐺', '🐐', '🥦'], []))
print("Estado inicial:", world.state)

new_state = world.get_next_state(world.state, 'MOVE_GOAT_AND_FARMER_FROM_LEFT_TO_RIGHT')
print("Después de mover granjero + cabra:", new_state)
print("¿Es seguro?:", safe(new_state))
