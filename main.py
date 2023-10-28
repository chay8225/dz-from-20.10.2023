class Zoo:
    group = 'Animals'
    alive = 'All animals is alive'


    def __init__(self, legs, wings, fly, speed, swim, name='Leon-Fedor'):
        self.name = name
        self.legs = 0
        self.wings = 0
        self.fly = True
        self.speed = 0
        self.swim = True

    def count_wings(self):
        if i == ''


    def to_run(self):
        if i == 'Run':
            Leon_Fedor.speed += 74
            Duck_Jack.speed += 50
            Zebra_Chloa.speed += 65
            Crocodile_Gena.speed += 48
            print(f'Leon is running {Leon_Fedor.speed} km/h \n  Oou..duck is running on you with speed {Duck_Jack.speed}km/h!')
            print(f'Look! This zebra running {Zebra_Chloa.speed} km/h')
            print(f'Eeee.. Hear is crocodile running to catch the bird with {Crocodile_Gena.speed} km/h  ')
    def to_fly(self):
        if i == 'Fly':
            print(f'It`s weird choose because only duck can fly hear. Look, on this board information even write about it: ')
            print(f'Leon-{Leon_Fedor.fly}, Zebra-{Zebra_Chloa.fly}, Crocodile-{Crocodile_Gena.fly}, Duck-{Duck_Jack.fly}')
    def to_swim(self):
        if i == 'Swim':
            print(f'Very simple, they all can swim: Leon-{Leon_Fedor.swim}, Duck-{Duck_Jack.swim}, Zebra-{Zebra_Chloa.swim}, Crocodile-{Crocodile_Gena.swim}')



Leon_Fedor = Zoo( 4, 0, False, 0, True )
Duck_Jack = Zoo(2, 2 , True, 0, True, name='Duck-Jack')
Zebra_Chloa = Zoo(4, 0, False, 0,True, name='Zebra-Chloa')
Crocodile_Gena = Zoo(4, 0, False, 0, True, name='Crocodile-Gena')
inf = Leon_Fedor.name, Duck_Jack.name, Zebra_Chloa.name, Crocodile_Gena.name

print(f'Animals name: {inf}')

i = str(input(f'Choose one: Run, Fly, Swim, [animal`s name].wings, [animal`s name].legs'))

print(Zoo.alive)

Leon_Fedor.to_swim()
Leon_Fedor.to_run()
Leon_Fedor.to_fly()




