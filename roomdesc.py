import random


class RoomDescription:
    def __init__(self):
        self.enter_room = [
            'You open up a door',
            'You open an old rusty iron door',
            'You squeeze through a small crevice in the wall',
            'You open an old rotting wooden door',
            'You walk into the room',
            'You walk through the entrance',
            'You go into the next area',
            'You push open a huge gate',
            'You walk through a gateway',
            'You kick open a locked door',
            'You slowly open up a squeaky gate',
            'You walk through a big hole in the wall']
        self.description = [
            'the walls and floor are covered in blood',
            'A light flickers from a chandelier',
            'the only light in the room is from a torch '
            'lying on the ground',
            'the room is overgrown with vegetation',
            'Skeletal remains are scattered all over the floor',
            'decaying bodies lay scattered around the room',
            "there's a fountain in here",
            'moonlight from a crack in the roof lights up '
            'the dark loathsome room',
            'it appears to be a prison cell full of shackles '
            'and skeletons',
            "there's a deep hole in the middle of the room",
            'spider webs cover most of the darkly lit room',
            "in the corner there's a slumped over knight "
            "with blood running down his face",
            "there's a sacrificial altar covered in blood "
            "stains in the middle of the room",
            "in the far end of the room there's a throne "
            "with worn down banners on each side",
            'the room is filled with old stone statues',
            "there's a deep disturbing well in the middle of "
            "the room",
            "the room is pitch-black",
            'a fight between knights and orcs appear to have '
            'taken place in here',
            'The moss-covered stone floor dampens your feet',
            'racks full of whiskey and wine fill up this room',
            "it's an armory filled with old rusty weapons",
            "a thick haunting mist impairs your vision",
            "it appears to be a torture chamber with severed "
            "limbs scattered around the room",
            "it's a library filled with old dusty books",
            "a small bonfire lights up the dark brick walls"]
        self.senses = [
            'the silence is deafening',
            'its exceedingly dark and gloomy',
            "it's very cold and damp in here",
            'you can hear a faint cry for help in the distance',
            'a foul smell of death and despair hits your nostrils',
            'the smell of decay is overwhelming',
            'an unnerving feeling rushes over you',
            'a cold shiver runs down your spine',
            'the only sounds you hear is from crackling of fire '
            'and dripping water',
            'the scent of blood and alcohol washes over you',
            "it's freezing cold", "it's very warm",
            'its hard to breathe the stuffy air',
            'a slight cold breeze grazes you',
            "you can hear a muffled scream echoing between the walls"]

    def get_description(self):
        return f'{random.choice(self.enter_room)}\n'\
               f'{random.choice(self.description)}\nand ' \
               f'{random.choice(self.senses)}'
