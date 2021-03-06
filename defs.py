def isAgro(coord1, coord2, agroRadius):
    distance = ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5
    return distance <= agroRadius


def calculationOfSpeed(coord1, coord2, speed):
    absciss = coord2[0] - coord1[0]
    ordinat = coord2[1] - coord1[1]
    hypotenuse = (absciss ** 2 + ordinat ** 2) ** 0.5
    print(absciss, ordinat, hypotenuse)
    koef = speed / hypotenuse
    speed_x = koef * absciss
    speed_y = koef * ordinat
    return speed_x, speed_y


def camera(hero, SIZE):
    coord = [0, 0]
    coord[0] = - hero.rect.x + 380
    coord[1] = - hero.rect.y + 300
    if - coord[0] < 0:
        coord[0] = 0
    if - coord[0] > SIZE[0] - 760:
        coord[0] = - SIZE[0] + 760
    if - coord[1] < 0:
        coord[1] = 0
    if - coord[1] >= SIZE[1] - 600:
        coord[1] = - SIZE[1] + 600
    return coord[0], coord[1]
