import lab10

def main():
    Z1 = lab10.Zombies(10,10)       #Test Zombie spawn, Player Spawn, and ZombiePlayer death
    print(Z1)
    P = lab10.Player(5,5)
    P.movement(10,10)
    print(P.death(Z1))

    Z2 = lab10.Zombies(11,11)   #Test Zombie Death due to bullet
    print(Z2)
    B = lab10.Bullet(17,17)
    B.movement(11,11)
    print(Z2.death(B))
    print(B.hit(B,Z2))

main()
