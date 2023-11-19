# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define b = Character('Отец', color="#fc0303")
define m = Character('Мать', color="#95ff00")
define t = Character('Тихон', color="#95ff00")
define fr = Character('Ферреро Роше', color="#95ff00")
define u = Character('Незнакомец', color="#95ff00")
define unk = Character('', color="#95ff00")


#DETEYY
image house = "bg/house.png"
image road = "bg/road.png"
image forest = "bg/forest.png"
image car = "bg/car.png"




# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Спрайты Бати
image BatyaAngry = "batya/BatyaAngry.png"
image BatyaY = "batya/BatyaAngry.png"

#CПрайты Мати
image Mat =  "mat/Mat.png"
image MatSad = "mat/MatSad.png"


#Спрайты Тихона
image Tihon = "tihon/TihonNormal.png"
image TihonSad = "tihon/TihonSad.png"

#Спрайты Ferrero
image Ferrero = "ferrero/FerreroLike.png"
image FerreroFlip = im.Flip("ferrero/FerreroLike.png", horizontal="True")

# Игра начинается здесь:
label start:
    scene house
    show BatyaAngry at left
    with dissolve
    b "ТЫ НИЧЕГО НЕ ДОБЬЕШСЯ В ЭТОМ МЕГАПОЛИСЕ! ТАКОМУ ДУРАКУ НЕ НАЙТИ ТАМ МЕСТА!"
    b "ТВОЙ УДЕЛ - РАБОТАТЬ НА ФЕРМЕ,ЗНАЙ СВОЕ МЕСТО,СОПЛЯК!"

    show Mat
    with dissolve

    m "Сева прекрати! Не дави так на него,ты же знаешь какой он мягкий и ранимый!"

    hide Mat
    show MatSad at right
    with dissolve

    b "ЗНАЙ СВОЕ МЕСТО ЖЕНЩИНА!"
    b "Почему все в этой чертовой семье считают что я пустое место."
    b "ЭТО МОЙ ДОМ И Я В НЕМ ГЛАВНЫЙ!"

    hide BatyaAngry
    hide MatSad
    with dissolve

    scene forest
    with dissolve

    show Tihon at left
    with dissolve

    unk ""

    scene road
    with dissolve

    show Tihon

    u "В Екатеринбург направляюсь"

    scene car
    with dissolve

    show Tihon at left
    show Ferrero at right

    u "Что с тобой случилось, парень? Ты будто марафон пробежал."
    t  "д.. да не важно..."
    u "может тебе нужна помощь?"
    t "Спасибо, вобще-то я только что сбежал из дома..."
    u "Ооо, ну ты даешь. Что, мамка за компом сидеть запрещает?"
    fr "Я кстати Ферреро Роше, программистом подрабатываю, подсобить могу первое вермя"
    t "Я тоже мечтал стать программистом, но мои родители решили всё за меня"
    fr "Чтож, теперь ты волен сам вершить свою судьбу"

    #e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
