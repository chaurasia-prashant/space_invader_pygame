import  cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(

        name='Space Warrior',
        options={"build_exe":  {"packages":["pygame"],"include_files":["ship.png","bullet.png","enbullet.png","enemy.png","explosion.png","play.mp3","player.png","ship.png","sky.jpg"]}},
        executables=executables

)
