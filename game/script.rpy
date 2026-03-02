# The script of the game goes in this file.
init python:
    def blur_filter(img, blur_strength=10):
        return im.MatrixColor(img, im.matrix.saturation(0.5))  # Чуть уменьшает насыщенность

    ## 🎭 Глобальные переменные (для отслеживания предметов)
    has_toy = False          
    has_key = False          
    has_photo_album = False  
    has_diary = False
    cafe_false_id = False
    cafe_mother_hint = False
    chapel_shadow_whisper = False
    chapel_victims_knowledge = False
    east_market_occult = False
    flag_memory_photo = False
    found_article = False
    found_false_id = False
    morgue_body_double = False
    morgue_father_experiments = False
    west_asylum_paranoia = False
    west_found_blueprint = False
    west_memory_door = False
    west_saw_patient_shadow  = False        

## 🌍 Язык
define config.language = "russian"  # Язык по умолчанию

## 🎬 Эффекты
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")  
define horror_flash = Fade(0.1, 0.0, 0.7, color="#ff0000")  
define quick_flash = Dissolve(0.2)  
define slow_dissolve = Dissolve(2.0)  
define shake = Move((0, 0), (10, 0), 0.05, repeat=5)  

## 🎭 Определяем персонажей
define alex = Character("[player_name]")  
define owner = Character("Владелец гостиницы")  
define shadow = Character("Тень")  
define unknown = Character("???")
define barista = Character("Бариста")
define photographer = Character("Фотограф")
define old_man = Character("Старик")
define librarian = Character("Библиотекарь")
define market_woman = Character("Продавщица")
define priest = Character("Священник")
define coroner = Character("Патологоанатом")
define shadow_figure = Character("Тень отца")

## 🎨 Фоны (с пробелами, как в твоей папке)
image bg road_night = "images/bg road_night.png"
image bg old_house_inside = "images/bg old_house_inside.png"
image bg old_house_night = "images/bg old_house_night.png"
image bg attic = "images/bg attic.png"
image bg secret_room = "images/bg secret_room.png"
image bg asylum_files = "images/bg asylum_files.png"
image bg asylum_hallway = "images/bg asylum_hallway.png"
image bg asylum_inside = "images/bg asylum_inside.png"
image bg asylum_outside = "images/bg asylum_outside.png"
image bg asylum_room = "images/bg asylum_room.png"
image bg black = "images/bg black.png"
image bg dream = "images/bg dream.png"
image bg dream_dark = "images/bg dream_dark.png"
image bg hotel = "images/bg hotel.png"
image bg hotel_basement = "images/bg hotel_basement.png"
image bg hotel_hallway = "images/bg hotel_hallway.png"
image bg hotel_lobby = "images/bg hotel_lobby.png"
image bg hotel_room = "images/bg hotel_room.png"
image bg night_sky = "images/bg night_sky.png"
image bg nightmare = "images/bg nightmare.png"
image bg nightmare_sewer = "images/bg nightmare_sewer.png"
image bg old_picture = "images/bg old_picture.png"
image bg old_picture_1 = "images/bg old_picture_1.png"
image bg room = "images/bg room.png"
image bg secret_tunnel = "images/bg secret_tunnel.png"
image bg underground_passage = "images/bg underground_passage.png"
image bg void = "images/bg void.png"
image bg sunset = "images/bg sunset.png"
image bg old_cabinet = "images/bg old_cabinet.png"
image bg hidden_door = "images/bg hidden_door.png"
image bg old_painting = "images/bg old_painting.png"
image bg old_painting_close = "images/bg old_painting_close.png"
image bg old_photo_faded = "images/bg old_photo_faded.png"
image bg memory_hospital = "images/bg memory_hospital.png"
image bg old_letters = "images/bg old_letters.png"
image bg street_night = "images/bg street_night.png"
image bg north_district = "images/bg north_district.png"
image bg park_night = "images/bg park_night.png"
image bg south_district = "images/bg south_district.png"
image bg cafe_inside = "images/bg cafe_inside.png"
image bg photo_studio = "images/bg photo_studio.png"
image bg west_district = "images/bg west_district.png"
image bg old_house_outside = "images/bg old_house_outside.png"
image bg library_inside = "images/bg library_inside.png"
image bg library_archive = "images/bg library_archive.png"
image bg school_ruins = "images/bg school_ruins.png"
image bg classroom_dark = "images/bg classroom_dark.png"
image bg east_district = "images/bg east_district.png"
image bg market_empty = "images/bg market_empty.png"
image bg chapel_inside = "images/bg chapel_inside.png"
image bg morgue_inside = "images/bg morgue_inside.png"
image bg secret_tunnel = "images/bg secret_tunnel.png"
image bg underground_passage = "images/bg underground_passage.png"
image bg memory_hospital = "images/bg memory_hospital.png"


## 📜 Объекты (ВСЕ, что есть в папке)
image owner = "images/owner.png"
image shadow = "images/shadow.png"
image shadow_patient = "images/shadow_patient.png"
image alex normal = "images/alex_normal.png"
image alex happy = "images/alex_happy.png"
image alex sad = "images/alex_sad.png"
image alex worried = "images/alex_worried.png"
image alex shocked = "images/alex_shocked.png"
image alex confused = "images/alex_confused.png"
image cafe_barista = "images/cafe_barista.png"
image camera_operator = "images/camera_operator.png"
image old_man = "images/old_man.png"
image librarian = "images/librarian.png"
image market_woman = "images/market_woman.png"
image priest_shadow = "images/priest_shadow.png"
image coroner = "images/coroner.png"
image shadow_figure = "images/shadow_figure.png"
image letter = "images/letter.png"
image old_photo = "images/old_photo.png"
image old_photo_faded = "images/old_photo_faded.png"
image old_toy = "images/old_toy.png"
image toy_bear = "images/toy_bear.png"
image old_key = "images/old_key.png"
image secret_papers = "images/secret_papers.png"
image file_cabinet = "images/file_cabinet.png"
image broken_ladder = "images/broken_ladder.png"
image letter = "images/letter.png"
image old_photo = "images/old_photo.png"
image old_photo_faded = "images/old_photo_faded.png"
image old_toy = "images/old_toy.png"
image old_key = "images/old_key.png"
image old_diary = "images/old_diary.png"
image old_photo_album = "images/old_photo_album.png"
image old_photo_close = "images/old_photo_close.png"
image documents_reveal = "images/documents_reveal.png"
image mirror_reflection = "images/mirror_reflection.png"
image shadow_figure = "images/shadow_figure.png"
image cold_hand = "images/cold_hand.png"

image flickering_light:
    "images/flickering_light.png"
    pause 0.2
    alpha 0.5  # Ослабляем яркость
    pause 0.2
    alpha 1.0  # Восстанавливаем яркость
    repeat

## 🔊 Музыка и атмосфера
define audio.ambient = "audio/ambient.mp3"
define audio.asylum_ambience = "audio/asylum_ambience.mp3"
define audio.basement_ambience = "audio/basement_ambience.mp3"
define audio.dream_theme = "audio/dream_theme.mp3"
define audio.ending_theme = "audio/ending_theme.mp3"
define audio.hotel_theme = "audio/hotel_theme.mp3"
define audio.main_menu_theme = "audio/main_menu_theme.mp3"

## 🎭 Эффекты и звуки окружения
define audio.whispers = "audio/whispers.ogg"
define audio.death_scream = "audio/death_scream.ogg"
define audio.door_bang = "audio/door_bang.ogg"
define audio.fall_crack = "audio/fall_crack.ogg"
define audio.falling_wind = "audio/falling_wind.ogg"
define audio.footsteps = "audio/footsteps.ogg"
define audio.heartbeat_fast = "audio/heartbeat_fast.ogg"
define audio.heartbeat_slow = "audio/heartbeat_slow.ogg"
define audio.page_turn = "audio/page_turn.ogg"
define audio.door_creak = "audio/door_creak.ogg"


## 🎥 Анимации и эффекты
transform shake:
    xoffset -10
    linear 0.1 xoffset 10
    linear 0.1 xoffset -10
    repeat

transform flash:
    alpha 1.0
    linear 0.1 alpha 0.0



# The game starts here.

label start:
    # Показываем фон (можно заменить на свой)
    stop music fadeout 1.0  # Музыка плавно затухает

    scene bg room
    # Игрок выбирает язык
    menu:
        "Выбери язык / Choose a language:"
        "Русский":
            $ config.language = "russian"
        "English":
            $ config.language = "english"
    
    # Переход в основную часть игры
    jump main_game
    
## 🏚 СЦЕНА 1: Пролог
label main_game:

    # Остановка музыки меню и запуск фоновой музыки
    stop music fadeout 1.0
    scene bg road_night with fade
    play music "audio/ambient.mp3"

    # Игрок вводит имя
    $ player_name = renpy.input("Как зовут нашего героя?", default="Алекс").strip().capitalize()
    if player_name == "":
        $ player_name = "Алекс"

    show alex normal at left with moveinleft
    alex "Спустя 15 лет я снова здесь…"

    window hide  # Прячем стандартное окно диалога
    "{color=#AAAAAA}Ветер проносится по пустынной дороге, поднимая пыль и мертвые листья.{/color}"  

    show alex normal at center with move
    alex "Я думал, что никогда больше не вернусь в этот город."

    "{color=#AAAAAA}Но несколько недель назад кто-то начал присылать мне письма…{/color}"

    show letter at center with dissolve
    "{color=#AAAAAA}Ты достаёшь последнее письмо из кармана. Пожелтевшая бумага, аккуратный почерк.{/color}"
    "{color=#AAAAAA}Кажется, что ты слышишь голос в голове.{/color}"
    
    unknown "{color=#AA0000}Ты знаешь, что должно было случиться.{/color}"
    unknown "{color=#AA0000}Правда ближе, чем ты думаешь.{/color}"

    hide letter with fade

    show alex sad
    alex "Кто это и зачем он хочет, чтобы я вернулся?"

    "{color=#AAAAAA}Ты ощущаешь холодок, пробежавший по спине. Город перед тобой кажется пустым, мёртвым.{/color}"

    show old_photo at center with dissolve
    "{color=#AAAAAA}Вместе с письмом пришла старая фотография. На ней — твой отец. А рядом… кто-то, кого ты не помнишь.{/color}"

    hide old_photo with fade
    show alex worried
    alex "Почему я ничего не помню?"

    "{color=#AAAAAA}Ты сжимаешь пальцы в кулак и делаешь шаг вперёд.{/color}"

    ## 📌 ВЫБОР 1: Куда пойти?
    menu:
        "Пойти в старый дом":
            jump scene_old_house_outside
        "Пойти в гостиницу":
            jump scene_2b
        "Отправиться в центр города":
            jump scene_city
        "Уехать из города":
            jump ending_escape


## 🏚 СЦЕНА 2А: СТАРЫЙ ДОМ
label scene_old_house_outside:
    scene bg old_house_night
    show alex normal at right with moveinright  
    alex "Все осталось таким же, как и в моих воспоминаниях."

    show alex normal at center with move
    scene bg old_house_inside
    "Ты заходишь внутрь. В воздухе пахнет пылью. На полу лежит ящик с письмами отца."

    hide alex with moveoutleft  
    
    ## 📌 ВЫБОР:
    menu:
        "Открыть письма и прочитать":
            jump scene_old_house_letters
        "Оставить письма нетронутыми и исследовать дом":
            jump scene_old_house_search

label scene_old_house_letters:
    scene bg old_house_inside
    show alex normal at left with moveinleft  

    "Ты открываешь письма. В них говорится, что твой отец работал в психиатрической лечебнице..."

    show alex sad at center with move  
    alex "Эксперименты? Над людьми?"

    hide alex with moveoutright  
    
    ## 📌 ВЫБОР:
    menu:
        "Отправиться в лечебницу":
            jump scene_4_asylum
        "Оставить дом и покинуть город":
            jump scene_old_house_exit

label scene_old_house_search:
    scene bg old_house_inside with fade
    show alex normal at left with moveinleft  
    "Ты продолжаешь осматривать дом."

    menu:
        "Прочитать письма":
            jump scene_old_house_read_letters
        "Открыть шкаф":
            jump scene_old_house_cabinet
        "Подняться на чердак":
            jump scene_old_house_attic
        "Подойти к старому портрету":
            jump scene_old_house_painting
        "Осмотреть странную дверь":
            jump scene_old_house_hidden_door
        "Оставить дом":
            jump scene_old_house_exit

label scene_old_house_cabinet:
    scene bg old_cabinet with fade
    "Ты открываешь скрипучий шкаф. Внутри – только пыль и паутина."

    show old_key at center with dissolve
    "Но вдруг, на нижней полке, ты замечаешь старый ключ."

    menu:
        "Взять ключ":
            $ has_key = True
            "Ты кладёшь ключ в карман."
        "Оставить его":
            "Ты решаешь не брать ключ."

    jump scene_old_house_search

label scene_old_house_hidden_door:
    scene bg hidden_door with fade
    "Ты находишь странную дверь, наполовину скрытую за старым ковром."

    menu:
        "Попробовать открыть дверь":
            if has_key:
                jump scene_old_house_secret_room
            else:
                "Дверь заперта. Нужен ключ."
                jump scene_old_house_search
        "Не трогать дверь":
            jump scene_old_house_search

label scene_old_house_secret_room:
    scene bg secret_room with fade
    "Ты осторожно открываешь дверь. Внутри – комната, о которой ты никогда не знал."

    show old_diary at center with dissolve
    "На столе лежит дневник отца. Его записи выглядят странными..."

    menu:
        "Прочитать дневник":
            jump scene_old_house_diary
        "Оставить комнату":
            jump scene_old_house_search

label scene_old_house_diary:
    scene bg secret_room with fade
    "Ты перелистываешь страницы дневника."

    "Записи полны странных слов и символов. Отец явно скрывал что-то."

    "На последней странице написано: 'Только те, кто осмелится узнать правду, найдут её.'"

    menu:
        "Отправиться в лечебницу":
            jump scene_4_asylum
        "Покинуть дом":
            jump scene_old_house_exit
        "Продолжить поиски в доме":
            jump scene_old_house_search  # Теперь можно продолжить искать улики!

label scene_old_house_painting:
    scene bg old_painting with fade
    "Ты подходишь к старинному портрету. Он выглядит очень знакомым."

    "Сердце сжимается от странного чувства дежавю."

    menu:
        "Осмотреть картину ближе":
            jump scene_old_house_painting_close
        "Отойти":
            jump scene_old_house_search

label scene_old_house_painting_close:
    scene bg old_painting_close with fade
    "Ты приглядываешься. Лицо на портрете... Это ты."

    "Но картина выглядит старой. Слишком старой."

    "Как такое возможно?"

    menu:
        "Потрогать портрет":
            "Твоя рука касается холста... и что-то холодное касается тебя в ответ."
            jump ending_madness
        "Оставить всё как есть":
            jump scene_old_house_search

label scene_old_house_attic:
    scene bg attic
    show alex normal at right with moveinright
    "Ты слышишь странный шум наверху."

    "На чердаке ты находишь детские рисунки, подписанные твоим именем."

    scene bg old_picture
    alex "Я этого не помню..."

    hide alex with moveoutleft  

    ## 📌 ВЫБОР:
    menu:
        "Осмотреть коробку в углу":
            jump scene_old_house_box
        "Искать другие улики":
            jump scene_old_house_more_clues
        "Покинуть дом немедленно":
            jump scene_old_house_exit

label scene_old_house_box:
    scene bg attic with fade
    "В углу чердака ты замечаешь старую деревянную коробку."

    show old_photo_album at center with dissolve
    "Ты открываешь её и находишь старый фотоальбом."

    "Фотографии сделаны в этом доме... Но вот что странно: на одной из них ты изображён ребёнком, но фото выглядит слишком старым, как будто ему больше 50 лет."

    menu:
        "Рассмотреть фотоальбом внимательнее":
            jump scene_old_house_photo_album
        "Оставить его и продолжить поиски":
            jump scene_old_house_more_clues

label scene_old_house_photo_album:
    call scene_old_house_photo_album_check_has_photo_album
    scene bg attic with fade
    "Ты листаешь пожелтевшие страницы."

    show old_photo_close at center with dissolve
    "На одной из фотографий ты стоишь рядом с незнакомым мужчиной. Он выглядит так же, как ты сейчас… но фото сделано несколько десятилетий назад."

    menu:
        "Попытаться вспомнить":
            jump scene_old_house_flashback
        "Закрыть альбом":
            jump scene_old_house_search

label scene_old_house_flashback:
    call scene_old_house_flashback_check_has_toy
    scene bg black with fade
    play sound "audio/whispers.ogg"  # Странные шёпоты в темноте

    "Голова начинает болеть. В памяти всплывают размытые картинки..."

    scene bg old_photo_faded with slow_dissolve
    "Ты видишь старый чёрно-белый снимок. Мужчина в больничном халате держит тебя за руку."

    "Он что-то говорит, но слов не разобрать."
    
    scene bg memory_hospital
    show bg memory_hospital as blurred_scene at Transform(blur=10) with Dissolve(1.0) # Размытая картинка больницы
    "Мелькает образ мрачной палаты. Ты слышишь отдалённые крики."

    scene bg black with fade
    play sound "audio/heartbeat_slow.ogg"
    "Ты резко приходишь в себя, сердце колотится в груди."

    menu:
        "Вернуться к поискам в доме":
            jump scene_old_house_search
        "Покинуть дом":
            jump scene_old_house_exit

            
label scene_old_house_more_clues:
    scene bg attic with fade
    "Ты продолжаешь искать по углам чердака."

    show old_toy at center with dissolve
    "Среди пыли ты находишь старую игрушку – потерянного плюшевого медведя."

    "На лапке вышито имя... Твоё имя."

    menu:
        "Взять игрушку":
            $ has_toy = True
            "Ты берёшь медведя в руки. Ощущение странного дежавю не покидает тебя."
            jump scene_old_house_search
        "Оставить её":
            "Ты решаешь не трогать медведя и продолжаешь поиски."
            jump scene_old_house_search


label scene_old_house_read_letters:
    scene bg old_letters with fade
    show alex normal at center with moveinbottom  
    "Ты медленно разворачиваешь старые, пожелтевшие страницы."

    "Письма полны намёков на нечто жуткое, скрытое в этом городе."

    "Один из писем заканчивается словами: 'Тебе нужно найти правду, пока не стало слишком поздно.'"

    hide alex with moveoutbottom  

    jump scene_old_house_search

label scene_old_house_exit:
    scene bg street_night with fade
    show alex normal at right with moveinright
    "Ты выходишь на улицу. Ночной воздух холодит кожу."

    hide alex with moveoutleft  

    ## ВЫБОР: Куда идти дальше?
    menu:
        "Пойти в гостиницу":
            jump scene_2b
        "Отправиться в центр города":
            jump scene_city
        "Уехать из города":
            jump ending_escape

## 🏨 СЦЕНА: ГОРОД
label scene_city:
    scene bg black with fade  # Временный чёрный фон (пока нет фона города)
##    scene bg city_square with fade
    
    "Ты стоишь в центре пустынного города. Все улицы ведут к твоему прошлому."

    ## 📌 ВЫБОР 1: Куда пойти?
    menu:
        "Пойти в старый дом":
            jump scene_old_house_outside
        "Направиться на север":
            jump scene_north_district
        "Направиться на юг":
            jump scene_south_district
        "Направиться на запад":
            jump scene_west_district
        "Направиться на восток":
            jump scene_east_district
        "Уехать из города":
            jump ending_escape

## СЕВЕР — Лечебница и Заброшенный парк
label scene_north_district:
    scene bg north_district with fade
    "Ветер носит клочья бумаги по улицам. Здесь царит мрак и запустение."

    menu:
        "Подойти к лечебнице":
            jump scene_4_asylum
        "Зайти в заброшенный парк":
            jump scene_north_park
        "Вернуться в центр":
            jump scene_city

##🎢 Заброшенный парк
label scene_north_park:
    scene bg park_night
    "Сломанные качели, туманные силуэты и детский смех, которого быть не может."

    show toy_bear with dissolve
    "Ты находишь старую игрушку в песочнице. На ней вышито твоё имя."
    $ has_toy = True
## уже была игрушка в доме, здесь дубль?
    jump scene_north_district

##🔥 ЮГ — Центр города, гостиница, кафе, фотоателье
label scene_south_district:
    scene bg south_district with fade
    play music "audio/hotel_theme.mp3" fadein 2.0

    "Южный район города выглядит... живым. Слишком живым."
    "Вывески кафе всё ещё мигают, двери гостиницы открыты, будто в городе никогда ничего не случалось."

    menu:
        "Зайти в гостиницу":
            jump scene_2b
        "Зайти в кафе":
            jump scene_south_cafe
        "Посетить фотоателье":
            jump scene_south_studio
        "Вернуться в центр":
            jump scene_city

##☕ Кафе
label scene_south_cafe:
    call scene_south_cafe_check_cafe_false_id
    scene bg cafe_inside with fade
    play music "audio/dream_theme.mp3" fadein 2.0

    "Ты входишь в уютное, но странно пустое кафе. В воздухе запах ванили и старых газет."
    "Бариста, молодой парень с тёмными кругами под глазами, смотрит прямо на тебя."

    show cafe_barista at left with dissolve
    barista "Ты опять пришёл. Долго тебя не было."

    alex "Мы... знакомы?"

    barista "Ты просил оставить для тебя воспоминание. Вот оно."

    show old_photo at center with dissolve
    "Он протягивает тебе старую фотографию. На ней — ты. Но подпись другая: 'Макс Б. 1993 год'."

    $ found_false_id = True

    menu:
        "Спросить, кто такой Макс Б.":
            jump scene_south_cafe_false_identity
        "Спросить, откуда у него это фото":
            jump scene_south_cafe_photo_origin
        "Просто взять фото и уйти":
            jump scene_south_district

##📸 Ложная личность
label scene_south_cafe_false_identity:
    barista "Ты был здесь ребёнком. Говорил, что тебя забрали в 'белый дом с решётками'."
    barista "Ты исчез, и потом всё пошло наперекосяк."

    alex "Я не Макс. Я Алекс."

    barista "Смотри в глаза правде, Алекс или Макс — какая разница?"

    $ cafe_false_id = True
    jump scene_south_district

##🔍 Источник фото
label scene_south_cafe_photo_origin:
    barista "Это фото мне оставила женщина. Сказала: 'Он должен вспомнить'."
    barista "Больше ничего не сказала. Но она плакала."

    alex "Как она выглядела?"

    barista "Как тень, которая умеет плакать..."

    $ cafe_mother_hint = True
    jump scene_south_district

##📷 Старое фотоателье
label scene_south_studio:
    scene bg photo_studio with fade
    play sound "audio/door_creak.ogg"

    "Дверь скрипит, когда ты входишь в затхлое помещение. Плёнка развешена на просушку, в витрине стоят старые камеры."

    show camera_operator at right with dissolve
    photographer "Сюда редко кто заходит... Но ты — особенный случай."

    alex "Почему?"

    photographer "Ты оставил тут фото... или воспоминание."

    menu:
        "Попросить показать":
            jump scene_south_studio_memory_photo
        "Уйти":
            jump scene_south_district

##🖼️ Фотография памяти
label scene_south_studio_memory_photo:
    show old_photo_faded at center with dissolve

    "Он подаёт тебе снимок. На нём — палата с окном, решётки, ребёнок на койке. В углу — силуэт мужчины в халате."
    "Ты не хочешь, но узнаёшь обоих."

    alex "Это… мой отец. А второй — я?"

    photographer "Фотографии не лгут. Люди — да."

    $ has_photo_album = True
    $ flag_memory_photo = True

    jump scene_south_district

##🌑 ЗАПАД — Частный сектор(сосед отца), библиотека, школа
label scene_west_district:
    scene bg west_district with fade
    play music "audio/ambient.mp3" fadein 1.0

    "Запад города — это улицы с закрытыми ставнями и шорохами за углами."

    menu:
        "Поговорить с соседом отца":
            jump scene_west_neighbor
        "Зайти в библиотеку":
            jump scene_west_library
        "Проверить старую школу":
            jump scene_west_school
        "Вернуться в центр":
            jump scene_city

##🧓 Дом соседа отца (Свидетель)
label scene_west_neighbor:
    scene bg old_house_outside with fade
    show old_man at left with dissolve

    "Старик выходит на крыльцо, будто ждал тебя."

    old_man "Ты похож на него. Такой же упрямый взгляд. Это ты, Алекс?"

    alex "Да. Вы знали моего отца?"

    old_man "Мы вместе строили эту улицу... А потом он ушёл в ту клинику. После этого всё изменилось."

    menu:
        "Расспросить о детстве":
            jump scene_west_neighbor_childhood
        "Спросить про клинику":
            jump scene_west_neighbor_asylum
        "Промолчать и уйти":
            jump scene_west_district

##👶 Воспоминания о детстве
label scene_west_neighbor_childhood:
    old_man "Ты был странным ребёнком. Не играл с другими. Всё рисовал двери."
    old_man "Когда твой отец приходил — ты замирал. Я это помню."

    $ west_memory_door = True
    jump scene_west_district

##🏥 Про клинику
label scene_west_neighbor_asylum:
    old_man "Я слышал, что в подвале они держали кого-то... Твоего отца всё это сломало."
    old_man "Он ходил ночью, шептал что-то вроде 'они следят'."

    $ west_asylum_paranoia = True
    jump scene_west_district

##📚 Старая библиотека
label scene_west_library:
    scene bg library_inside with fade
    play music "audio/ambient.mp3"

    "Ты входишь в пыльную библиотеку. Внутри пахнет мокрой бумагой и молчанием."

    show librarian at right with dissolve
    librarian "Закрыты мы. Но для тебя — исключение."

    menu:
        "Спросить про старые газеты":
            jump scene_west_library_newspapers
        "Искать что-то самостоятельно":
            jump scene_west_library_search
        "Уйти":
            jump scene_west_district

##🗞️ Статьи прошлого
label scene_west_library_newspapers:
    scene bg library_archive with fade
    "Ты находишь статью от 1994 года: 'Пациент погиб в клинике. Имя засекречено. Ведётся следствие.'"

    "На полях карандашом приписано: 'Папа?'"

    $ found_article = True
    jump scene_west_district

##🔍 Поиск улик
label scene_west_library_search:
    "Ты находишь книгу с закладкой. В ней — схема подвала клиники, с пометкой 'Не входить'."

    $ west_found_blueprint = True
    jump scene_west_district

##🏫 Полуразрушенная школа
label scene_west_school:
    scene bg school_ruins with fade
    play sound "audio/door_bang.ogg"

    "Ты заходишь внутрь через выбитую дверь. Пыль пляшет в лучах закатного света. Всё мертво, кроме звуков шагов, которые... не твои?"

    show shadow at left with dissolve

    alex "Кто здесь?"

    hide shadow

    "Ответа нет. Только скрип доски в одном из классов."

    menu:
        "Пойти на звук":
            jump scene_west_school_sound
        "Спрятаться и наблюдать":
            jump scene_west_school_hide
        "Сбежать":
            jump scene_west_district

##🔊 Пойти на звук
label scene_west_school_sound:
    scene bg classroom_dark with fade
    "На доске мелом написано: 'Я всё ещё здесь.'"

    show old_diary at center with dissolve
    "Ты находишь обгоревшую тетрадь. Записи — маниакальные, как будто кто-то пытался удержать рассудок."

    $ has_diary = True
    jump scene_west_district

##🕵️ Спрятаться
label scene_west_school_hide:
    "Ты прячешься за шкафом. Кто-то проходит мимо — силуэт с перевязанной головой, будто из больницы."

    "Ты дышишь тише и слышишь слова:"

    unknown "Не забудь, кто ты на самом деле..."

    $ west_saw_patient_shadow = True
    jump scene_west_district

##🦴 ВОСТОК — Рынок, часовня, морг
label scene_east_district:
    scene bg east_district with fade
    "Скрипящие ворота и запах гари. Восток — как граница с чем-то чужим."
    "Восточная часть города тиха и пуста, будто сама смерть забыла её обнять. Тут всё связано с концами: рынок с гниющим запахом прошлого, старая часовня и здание, бывшее моргом."

    menu:
        "Зайти на рынок":
            jump scene_east_market
        "Зайти в часовню":
            jump scene_east_chapel
        "Посетить морг":
            jump scene_east_morgue
        "Вернуться в центр города":
            jump scene_city

##🧺 Рынок
label scene_east_market:
    scene bg market_empty with fade

    "Ты идёшь между шатрами. Всё мертво. Лишь один лоток освещён тусклым светом лампы."

    show market_woman at right with dissolve
    market_woman "Смотри внимательней. Здесь продаются не овощи, а следы памяти."

    alex "Вы меня с кем-то путаете..."

    market_woman "Ты ищешь отца. А нашёл — себя."

    menu:
        "Посмотреть, что у неё на столе":
            jump scene_east_market_table
        "Спросить, откуда она знает про отца":
            jump scene_east_market_origin
        "Уйти":
            jump scene_east_district

##📦 Стол памяти
label scene_east_market_table:
    show old_toy at center with dissolve

    "На столе — твоя старая игрушка. Её не может здесь быть."

    alex "Где вы это взяли?"

    market_woman "Ты сам оставил. В тот день, когда тебя увели из дома."

    $ has_toy = True
    jump scene_east_district

##🧠 Источник знания
label scene_east_market_origin:
    market_woman "Твой отец приносил мне сны. Он платил за них... голосами."

    "Она смеётся. И становится ясно — это не просто продавец."

    $ east_market_occult = True
    jump scene_east_district

##⛪ Часовня
label scene_east_chapel:
    scene bg chapel_inside with fade
    play sound "audio/door_creak.ogg"

    "Ты входишь в маленькую полуразрушенную часовню. Стены обуглены, купол пробит. В центре — лишь одна скамья и фигура в тени."

    show priest_shadow at left with dissolve
    priest "Ты вернулся, как и было предсказано."

    alex "Вы... кто?"

    priest "Священник, что молился за тех, кого твой отец принёс в жертву ради науки."

    menu:
        "Спросить про жертвы":
            jump scene_east_chapel_victims
        "Помолиться молча":
            jump scene_east_chapel_prayer
        "Уйти":
            jump scene_east_district

##🕯️ Жертвы
label scene_east_chapel_victims:
    priest "Шестеро исчезли. Четверо — дети. Двое — персонал. Никто не искал их. Никто, кроме меня."

    alex "Мой отец..."

    priest "Он верил, что лечит. Но ты стал границей между разумом и одержимостью."

    $ chapel_victims_knowledge = True
    jump scene_east_district

##✝️ Молитва
label scene_east_chapel_prayer:
    "Ты опускаешь голову. Молча. В тишине слышишь своё имя, шёпотом. Оно звучит, как приговор."

    unknown "{color=#AA0000}Прими тень. Прими себя.{/color}"

    $ chapel_shadow_whisper = True
    jump scene_east_district

##⚰️ Морг
label scene_east_morgue:
    scene bg morgue_inside with fade
    play music "audio/basement_ambience.mp3"

    "Холод ударяет в лицо. Ты заходишь в здание, где, по слухам, скрывали последствия экспериментов."

    show coroner at right with dissolve
    coroner "Я знал, что ты вернёшься. У нас есть нераспознанное тело... Совпадение по ДНК с тобой."

    menu:
        "Осмотреть тело":
            jump scene_east_morgue_body
        "Спросить, откуда анализ":
            jump scene_east_morgue_dna
        "Уйти":
            jump scene_east_district

##🧬 Осмотр тела
label scene_east_morgue_body:
    "Ты подходишь к столу. Тело — обугленное, но лицо... твоё?"

    alex "Это... я?"

    "На груди выжжено: 'Тот, кто не хочет знать'."

    $ morgue_body_double = True
    jump scene_east_district

##🧪 Анализ
label scene_east_morgue_dna:
    coroner "Проба была у меня давно. Приказ сверху. Тогда я не знал, чьё это..."

    "Он бросает на стол лист — приказ подписан инициалами твоего отца."

    $ morgue_father_experiments = True
    jump scene_east_district


## 🏨 СЦЕНА 2Б: ГОСТИНИЦА
label scene_2b:
    # 🎬 ВИДЕО ОТЕЛЯ СНАРУЖИ
    window hide  # Убираем текстовое окно на время видео
    play movie "videos/hotel_exterior.webm" loop  # Показываем видео отеля
    pause 4  # Держим видео 4 секунд
    stop movie  # Останавливаем видео
    scene bg hotel
    window show  # Показываем текстовое окно

    "Перед тобой возвышается гостиница 'Затмение'."
    "Она выглядит... слишком уютной для этого города."
    show alex normal at left with moveinleft    
    "Почему-то внутри что-то ёкает, как будто я уже был здесь."

    # 🏨 ПОКАЗЫВАЕМ ИНТЕРЬЕР ОТЕЛЯ
    scene bg hotel_lobby with fade
    play music "audio/hotel_theme.mp3" fadein 2.0  # Фоновая музыка гостиницы

    # 👤 УПРАВЛЯЮЩИЙ ГОСТИНИЦЫ 
    show owner at left with dissolve # Показываем управляющего
    owner "Как приятно видеть вас снова, [player_name]."
    hide owner

    show alex normal at right with dissolve
    alex "Но... я здесь впервые."
    hide alex
    
    show owner at left with dissolve # Показываем управляющего
    "Он улыбается так, словно я сказал что-то глупое."

    # 🔑 ДИАЛОГ О СНИМАНИИ КОМНАТЫ
    owner "Вы сняли номер заранее. Всё готово."
    hide owner
    show alex sad at right with dissolve
    "Это странно... Я ведь не бронировал комнату."

    menu:
        "Спросить, почему номер уже готов":
            jump scene_2b_question
        "Не спорить и взять ключ":
            jump scene_2b_room

label scene_2b_question:
    alex "Но я не бронировал номер..."
    hide alex
    show owner at left with dissolve # Показываем управляющего
    owner "Всё в порядке. Иногда судьба делает выбор за нас."
    hide owner
    show alex normal at right with dissolve
    "Ответ заставляет меня напрячься, но я беру ключ."
    hide alex
    
    jump scene_2b_room

label scene_2b_room:
    # 🚪 ПОКАЗЫВАЕМ КОРИДОР
    scene bg hotel_hallway with fade

    "Коридор тянется вдаль. Лампочки моргают, отбрасывая длинные тени."

    "Я чувствую, как что-то шевелится в темноте..."

    menu:
        "Следовать за тенями в коридоре":
            jump scene_3v  # Ветка с тайным проходом
        "Закрыться в номере":
            jump scene_3g  # Ветка со странными снами
        "Покинуть отель немедленно":
            jump ending_2


## 🚪 СЦЕНА 3В: ТАЙНЫЙ ПРОХОД
label scene_3v:
    scene bg hotel_basement with fade  # Фон подвала гостиницы

    play music "audio/basement_ambience.mp3"  # Жуткая фоновая музыка

    "Ты открываешь скрипучую дверь и спускаешься вниз."
    "В воздухе пахнет сыростью и плесенью."
    "Где-то капает вода..."

    show shadow at left with dissolve  # Тень мелькает сбоку

    "Ты видишь тень, исчезающую в темноте..."
    "Кажется, она зовёт тебя дальше."
    hide shadow
    menu:
        "Пойти за тенью":
            jump scene_3v_follow_shadow
        "Осмотреться в подвале":
            jump scene_3v_search_basement

label scene_3v_follow_shadow:

    "Ты делаешь шаг вперёд, но вдруг пол трескается под тобой!"

    # Включаем звук обрушения
    play sound "audio/fall_crack.ogg"

    # Дёргаем экран, создавая эффект провала
    scene bg hotel_basement
    with vpunch  # Вибрация экрана

    "Пол уходит из-под ног! Ты падаешь вниз!"

    # Эффект темноты и смены фона на туннель
    scene black with fade
    pause 0.2

    play sound "audio/falling_wind.ogg"  # Добавляем звук падения

    # Имитация падения с быстрым движением экрана вниз
    scene bg secret_tunnel
    "Ты падаешь в узкий туннель."
    "Теперь назад дороги нет..."

    jump scene_3v_secret_room

label scene_3v_secret_room:
    call scene_3v_secret_room_check_west_found_blueprint
    scene bg secret_tunnel with fade  # Узкий тоннель после падения

    play sound "audio/fall_thud.ogg"  # Звук приземления

    "Ты с глухим ударом приземляешься на каменный пол."
    "Свет из прорехи наверху быстро исчезает."
    
    "Теперь назад дороги нет."

    menu:
        "Осмотреться вокруг":
            jump scene_3v_explore
        "Кричать на помощь":
            jump scene_3v_shout_for_help

label scene_3v_explore:
    "Ты идёшь вперёд в темноту, ощупывая стены."
    
    show flickering_light at center with dissolve  # Находим мигающий фонарь

    "В углу мигает старый фонарь. Кажется, здесь кто-то был..."
    
    menu:
        "Взять фонарь и идти дальше":
            jump scene_3v_find_exit
        "Искать что-то полезное вокруг":
            jump scene_3v_find_documents

label scene_3v_find_exit:
    scene bg underground_passage with fade  # Переход в новый тоннель

    "Ты находишь узкий проход. Возможно, он ведёт наружу."
    
    menu:
        "Идти вперёд":
            jump scene_4_asylum  # Алекс выходит в подвал лечебницы
        "Остаться и изучить место":
            jump scene_3v_find_documents

label scene_3v_find_documents:
    scene bg secret_room with quick_flash  # Таинственная комната
    show file_cabinet at left with dissolve
    "Ты находишь старый шкаф с папками."
    hide file_cabinet
    "На одной из папок написано твоё имя..."
    show secret_papers at center with dissolve

    menu:
        "Открыть папку":
            jump scene_3v_secret_files
        "Оставить документы и искать выход":
            jump scene_3v_find_exit

label scene_3v_secret_files:
    "Ты раскрываешь папку..."
    "Фотографии, медицинские отчёты... Ты был здесь раньше."

    menu:
        "Продолжить изучать документы":
            jump scene_4_truth
        "Бежать, пока не поздно":
            jump scene_escape

label scene_3v_shout_for_help:
    "Ты кричишь, но вместо ответа слышишь лишь эхо."
    
    "А затем... что-то отвечает из темноты."

    menu:
        "Замереть на месте":
            jump scene_3v_meeting_shadow
        "Бежать в противоположную сторону":
            jump scene_escape

label scene_3v_meeting_shadow:
    scene bg nightmare_sewer with horror_flash  # Полный мрак

    "Тень появляется перед тобой."
    show shadow at center
    "Ты теряешь сознание..."
    hide shadow
    jump scene_4_madness  # Финал безумия


label scene_3v_search_basement:
    "Ты включаешь фонарик и осматриваешь подвал."
    "На полу лежат старые медицинские записи..."

    show secret_papers with dissolve  # Появляются документы

    "Это архивы с отчётами о странных экспериментах."
    "Кажется, это связано с твоим прошлым..."

    menu:
        "Взять документы с собой":
            jump scene_3v_take_documents
        "Оставить их и уйти":
            jump scene_3v_leave_basement

label scene_3v_take_documents:
    "Ты берёшь папку с документами и выходишь наверх."
    "Теперь тебе нужно разобраться, что это значит..."

    jump scene_4_investigation  # Следующая сцена

label scene_3v_leave_basement:
    "Ты чувствуешь, что тебе здесь не место."
    "Лучше уйти, пока не поздно..."

    jump scene_4_escape  # Альтернативная сцена

## 💤 СЦЕНА 3Г: СТРАННЫЕ СНЫ
label scene_3g:
    call scene_3g_check_chapel_shadow_whisper
    scene bg dream with fade  # Фон сна

    play music "audio/dream_theme.mp3"  # Играет жуткая музыка сна (замени файл на свой)

    "Ты оказываешься в странном месте..."
    "Всё вокруг размыто, как будто это сон."

    show shadow with dissolve  # Появляется тёмная фигура

    "Ты видишь тень, которая стоит вдалеке."
    "Она зовёт тебя по имени..."

    menu:
        "Подойти к тени":
            jump scene_3g_approach
        "Остаться на месте":
            jump scene_3g_stay

label scene_3g_approach:
    "Ты делаешь шаг вперёд..."
    "Но вдруг всё вокруг рушится!"

    scene bg void with flash  # Мир исчезает, остаётся пустота

    "Ты просыпаешься с криком."
    jump wake_up

label scene_3g_stay:
    "Ты остаёшься на месте."
    "Тень приближается сама..."

    scene bg nightmare with fade  # Экран темнеет

    "Ты просыпаешься в холодном поту."
    jump wake_up

label wake_up:
    scene bg hotel_room with fade
    "Ты открываешь глаза. Это был просто сон..."
    return

## 🏚 СЦЕНА 4: ЛЕЧЕБНИЦА
label scene_4_asylum: 
    call scene_4_asylum_check_has_diary
    window hide  # Убираем текстовое окно на время видео
    play movie "videos/asylum_exterior.webm" loop  # Показываем видео отеля
    pause 4  # Держим видео 4 секунд
    stop movie  # Останавливаем видео
    scene bg asylum_outside with fade  # Фон лечебницы снаружи
    window show  # Показываем текстовое окно
    
    play music "audio/asylum_ambience.mp3"  # Жуткий фоновый звук
    show alex normal at right with moveinright
    show alex normal at center with move
    "Ты стоишь перед мрачным зданием старой лечебницы."
    "Ветер проносит по земле сухие листья, окна тёмные и пустые."

    menu:
        "Зайти внутрь":
            jump scene_4_enter_asylum
        "Развернуться и уйти":
            jump scene_4_escape

label scene_4_enter_asylum:
    scene bg asylum_hallway with fade  # Фон внутри лечебницы

    "Дверь тяжело скрипит, когда ты входишь внутрь."
    "В коридорах пахнет сыростью и старостью."
    
    show flickering_light with dissolve  # Мигающий свет в коридоре

    "Лампочка над тобой вспыхивает и гаснет."
    play sound "audio/whispers.ogg"
    "Ты слышишь шёпот… или это просто ветер?"

    menu:
        "Исследовать архивы":
            jump scene_4_examine_files
        "Пойти в палату":
            jump scene_4_enter_room

label scene_4_examine_files:
    scene bg asylum_files with fade  # Фон с архивами

    show secret_papers with dissolve  # Медицинские документы

    "Ты находишь пыльный шкаф с медицинскими записями."
    "В одной из папок написано твоё имя..."

    jump scene_4_truth  # Истина раскрыта

label scene_4_enter_room:
    scene bg asylum_room with fade  # Фон палаты

    "Ты заходишь в старую палату."
    "На кровати кто-то сидит спиной к тебе..."

    show shadow_patient with dissolve  # Фигура в палате

    "Фигура медленно поворачивается..."
    jump scene_4_madness  # Финал безумия

label scene_4_escape:
    "Ты чувствуешь, что тебе не стоит здесь находиться."
    "Развернувшись, ты уходишь в ночь."

    jump scene_4_final_escape  # Финал бегства

label scene_4_truth:
    call scene_4_truth_check_morgue_body_double
    scene bg secret_room with fade

    "Ты листаешь старые медицинские отчёты. Они датированы годами, когда ты был ребёнком."

    "Среди документов ты находишь своё имя. Записи говорят, что ты был объектом экспериментов."

    show shadow at right with dissolve
    "В углу комнаты шевелится тень."

    menu:
        "Продолжить читать документы":
            jump scene_4_investigation
        "Бросить бумаги и бежать":
            jump scene_escape

label scene_escape:
    scene bg underground_passage with flash

    play sound "audio/footsteps.ogg"

    "Сердце бешено колотится, ты мчишься по узкому туннелю, не разбирая дороги."

    scene bg hotel with fade
    "Спустя несколько минут ты выбегаешь из подвала. Перед тобой снова гостиница."

    menu:
        "Вернуться внутрь":
            jump scene_2b_room
        "Уйти из города":
            jump ending_2
            return

label scene_4_madness:
    scene bg nightmare_sewer with horror_flash

    play sound "audio/whispers.ogg"
    "Шёпоты заполняют твой разум. Они становятся громче, заставляя тебя зажмуриться."

    show shadow at center with slow_dissolve
    "Перед тобой вырисовывается фигура. Ты не можешь двигаться."

    menu:
        "Протянуть руку":
            "Ты медленно поднимаешь руку, пытаясь коснуться тени."
            "Она приближается... Холод пробирает до костей."
            "Ты чувствуешь ледяное прикосновение..."
            show bg black with flash  # Вспышка и затемнение
            jump ending_4
            return
        "Закричать":
            "Ты открываешь рот, но не издаёшь ни звука."
            "Тень простирает к тебе руки..."
            "Ты теряешь сознание..."
            show bg black with fade
            play sound "audio/death_scream.ogg"
            jump ending_4
            return

label scene_4_investigation:
    scene bg secret_room with fade

    "Ты медленно изучаешь документы. В них говорится, что твой отец работал здесь врачом."

    "Эксперименты проводились на детях... Среди них был ты."

    show secret_papers at center with dissolve
    "На одной из фотографий ты видишь себя. Но тебе становится плохо."

    menu:
        "Покинуть помещение":
            jump scene_escape
        "Продолжить изучение":
            "Ты находишь координаты заброшенной клиники."
            jump scene_4_asylum

label scene_4_final_escape:
    scene bg underground_passage with shake  # Тоннель дрожит, будто рушится

    play sound "audio/heartbeat_fast.ogg"
    "Ты бежишь по мрачному подземному коридору, сердце бешено колотится."

    show shadow at left with slow_dissolve
    "В углу мелькает неясная тень. Ты слышишь шаги позади."

    menu:
        "Бежать дальше без оглядки":
            jump scene_escape_success

        "Остановиться и посмотреть назад":
            jump scene_escape_fail

label scene_escape_success:
    scene bg hotel with fade
    play sound "audio/door_bang.ogg"
    
    "С трудом ты выбегаешь наружу, задыхаясь от страха."

    menu:
        "Остаться и попытаться разобраться":
            jump scene_4_investigation
            
        "Сбежать из города":
            jump ending_2
            return  # Конец игры, персонаж уезжает

label scene_escape_fail:
    scene bg black with flash
    play sound "audio/death_scream.ogg"

    "Ты поворачиваешься назад..."
    "Последнее, что ты видишь — это пустые глаза тени."

    call screen game_over_screen  # Переход на экран смерти


## 🎭 ФИНАЛЫ
label ending_truth:
    scene bg asylum_inside with fade

    show alex shocked at center with dissolve
    "Ты находишь документы. В них сказано, что ты был частью эксперимента."

    alex "Я... Я был пациентом?.."

    "Воспоминания вспыхивают, накрывая тебя волной ужаса."
    "Ты вспоминаешь лицо отца. Его голос, его руки... Всё это было правдой."

    show documents_reveal at center with fade
    "На одной из фотографий ты видишь себя в белой больничной рубашке."
    
    "Ты больше не можешь отрицать очевидное. Правда раскрыта."

    jump ending_credits
    return

label ending_escape:
    scene bg road_night with slow_dissolve

    show alex sad at center with dissolve
    "Ты садишься в машину и заводишь двигатель. Город остаётся позади."

    alex "Я не хочу знать, что случилось."

    "Ты едешь всё дальше, но ощущение тревоги не исчезает."

    show mirror_reflection with fade
    "На мгновение тебе кажется, что в зеркале заднего вида мелькнуло лицо... Твоё лицо, но каким-то образом искажённое."

    "Ты пытаешься выбросить мысли из головы, но ощущение потери не покидает тебя."

    jump ending_credits
    return

label ending_madness:
    scene bg dream_dark with fade

    show alex confused at center with dissolve
    "Ты идёшь вперёд, но пространство вокруг меняется."

    "Стены растворяются, превращаясь в бесконечную тьму."
    "Ты слышишь шаги, но не можешь понять, твои ли они."

    unknown "Добро пожаловать домой."

    show shadow_figure at right with slow_dissolve
    "Перед тобой стоит силуэт. Он похож на тебя."

    "Ты больше не понимаешь, кто ты. Ты теряешь контроль."

    jump ending_credits
    return

label ending_death:
    scene bg black with fade
    play sound "audio/heartbeat_slow.ogg"

    "Сердце начинает биться всё медленнее..."

    show cold_hand at center with slow_dissolve
    "Последнее, что ты чувствуешь — это ледяное прикосновение к твоей коже."

    "Ты больше ничего не видишь."

    call screen game_over_screen  # Показываем экран смерти
    return
screen game_over_screen():
    modal True
    add "black"

    text "Ты больше не проснёшься...":
        xalign 0.5
        yalign 0.4
        color "#ffffff"
        size 40

    textbutton "Выйти в меню":
        xalign 0.5
        yalign 0.6
        action MainMenu()
   
label ending_credits:
    scene bg sunset with fade  # Показываем закат
    play music "audio/ending_theme.mp3"

    alex "Наконец-то всё стало ясно..."

    scene bg night_sky with fade  # Переключаем сцену на ночное небо

    "Алекс ушёл в темноту, оставив прошлое позади."

    scene bg black with fade
    show text "{size=60}{color=#ffffff}До встречи!" with dissolve

    $ renpy.pause(3)
    jump titles
    return

transform fade_in:
    alpha 0.0
    linear 3.0 alpha 1.0  # Плавное появление текста за 3 секунды

label titles:
    scene bg black with fade

    show text """ 
    {size=40}{color=#ffffff}{b}Сценарий:{/b} StViga

    {b}Художники:{/b} StViga, AI

    {b}Программист:{/b} StViga

    Спасибо за игру!
    """ with dissolve
    $ renpy.pause(15)  # Длительность титров
    return


label ending_1:
    scene bg asylum_inside

    "Ты находишь документы. В них сказано, что ты был частью эксперимента."

    alex "Я... Я был пациентом?"

    "Воспоминания возвращаются. Ты узнаёшь правду."
    jump ending_credits
    return

label ending_2:
    scene bg road_night

    "Ты уезжаешь, так и не узнав правды."

    alex "Я не хочу знать, что случилось."
    jump ending_credits
    return

label ending_3:
    scene bg dream_dark

    "Ты следуешь за голосом. Мир вокруг темнеет."

    unknown "Добро пожаловать домой."

    "Ты теряешь контроль над разумом."
    jump ending_credits
    return

label ending_4:
    show bg black with fade
    play sound "audio/heartbeat_slow.ogg"
    "Сердце начинает биться всё медленнее..."
    "Последнее, что ты чувствуешь — это ужасающее касание холода."
    call screen game_over_screen  # Показываем экран смерти
    return

label scene_old_house_flashback_check_has_toy:
    if has_toy:
        "Ты держишь медвежонка... и комната вспыхивает ярким воспоминанием."
        scene bg memory_hospital with flash
        "Ты видишь, как отец вручает тебе эту игрушку в больничной палате."
        "Это был его способ сказать прости. Или — прощай."
    return


label scene_4_asylum_check_has_diary:
    if has_diary:
        "Дневник в твоём кармане будто пульсирует, когда ты входишь в здание."
        "На стене ты замечаешь фразу, идентичную той, что была в конце дневника отца..."
        "— 'Не доверяй тем, кто лечит.'"
    return


label scene_old_house_photo_album_check_has_photo_album:
    if has_photo_album:
        "Ты инстинктивно сравниваешь лицо на фото с фигурами, что видишь в снах."
        "Сходство пугающе точное. Фото словно запечатлело сон, который ещё не приснился."
    return


label scene_south_cafe_check_cafe_false_id:
    if cafe_false_id:
        "Ты вдруг вспоминаешь, как подписал школьную анкету — не своим именем. Макс Б."
        "Бариста не лгал. В каком-то слое реальности ты действительно был другим."
    return


label scene_3v_secret_room_check_west_found_blueprint:
    if west_found_blueprint:
        "На полу виден люк, который ты раньше не замечал. Ты сопоставляешь его с чертежами."
        "Он ведёт в туннель, которого нет на планах города."
        jump scene_hidden_tunnel
    return


label scene_4_truth_check_morgue_body_double:
    if morgue_body_double:
        "В одной из фотографий — тело... твоё тело? Но лицо изуродовано."
        "Ты был мёртв? Или кто-то выдавал себя за тебя?"
    return


label scene_3g_check_chapel_shadow_whisper:
    if chapel_shadow_whisper:
        "Ты слышишь в голове отголосок шёпота из часовни:"
        unknown "{color=#990000}Ты обещал мне, что всё вспомнишь...{/color}"
    return

label scene_hidden_tunnel:
    scene bg secret_tunnel with fade
    play music "audio/tunnel_ambience.mp3" fadein 1.5

    "Ты входишь в тёмный туннель. Влага капает со свода, стены покрыты плесенью и старыми знаками."

    if west_found_blueprint and morgue_father_experiments:
        "Символы на стенах совпадают с пометками в документах отца. Ты чувствуешь, что приближаешься к чему-то важному."

        scene bg underground_passage with fade
        "Дальше — каменная арка. За ней слышно... дыхание?"

        "Ты делаешь шаг, и..."
        scene bg memory_hospital with flash

        "Вспышка. Боль. Комната. Ты на столе. Вокруг — белые халаты. Один из них — твой отец."

        show shadow_figure at center with dissolve
        unknown "{color=#990000}Ты должен был стать идеальным. Но ты выбрал помнить...{/color}"

        $ found_truth_tunnel = True
        jump scene_4_real_truth  # сцена финальной истины

    elif west_found_blueprint:
        "Ты доходишь до конца туннеля. Там тупик. Но в воздухе витает память, которую ты ещё не готов открыть."
        "Тебе не хватает частиц правды."

        return

    else:
        "Ты стоишь у входа, но не решаешься идти дальше. Что-то подсказывает: ты ещё не готов."

        return

label scene_4_real_truth:
    scene bg secret_room with fade
    play music "audio/truth_reveal.mp3" fadein 1.0

    "Ты спускаешься по скрипучей лестнице. Пыль поднимается с каждого шага. Запах сырости и формалина усиливается."
    "Туннель ведёт к камере — не тюремной, а скорее лабораторной. Холодной. Беспощадной."

    show shadow at center with dissolve
    "Тень ждет тебя. Но теперь — она не агрессивна. Она... знакома."

    unknown "{color=#666666}Ты пришёл. И ты уже знаешь.{/color}"

    alex "Ты... это ты?"

    unknown "{color=#666666}Я — то, что осталось от него. От твоего отца. От меня.{/color}"

    "Флэш воспоминания вспыхивает в твоем сознании — ты ребёнок, в палате, за стеклом наблюдает мужчина в белом халате. Ты его боишься... но и ждёшь."

    scene bg memory_hospital with flash
    "— \"Ты должен быть сильным, Алекс. Если ты забудешь, боль уйдёт. Но с ней уйду и я.\""

    return to scene bg secret_room with fade

    alex "Почему ты заставил меня забыть?"

    shadow "Потому что я боялся. Твоё сознание трещало. Эксперименты вышли из-под контроля. Ты был подопытным — и единственным, кого я пытался спасти."

    alex "Ты сам всё устроил?"

    shadow "Я хотел вылечить. Но болезнь была глубже. Она была в семье. В крови. Я искал способ стереть... но стёр и тебя."

    menu:
        "Принять правду и простить":
            jump scene_true_acceptance
        "Отвергнуть отца и покинуть это место":
            jump scene_true_rejection

label scene_true_acceptance:
    scene bg memory_hospital with fade
    play music "audio/redemption_theme.mp3" fadein 1.5

    "Ты медленно подходишь к Тени. Его силуэт мерцает, но не исчезает."
    alex "Я не знаю, что ты чувствовал. И не прощу всего. Но если это был способ любить... пусть так."

    shadow "Ты сильнее, чем я думал. Я разрушал — ты собрал заново."

    "Вокруг начинает рассеиваться тьма. Сцена превращается в тот самый день, который был стёрт из памяти: ты, отец и та самая игрушка. Вспоминаешь — не боль, а тепло."

    scene bg sunset with dissolve
    "Свет закатного солнца проникает в подземную комнату. Впервые за всё время — тебе дышится свободно."

    shadow "Спасибо, что отпустил меня, Алекс."

    "Тень исчезает. На её месте — лишь старое фото. На нём — вы вдвоём. Улыбающиеся."

    $ ending_truth = True
    jump ending_credits

label scene_true_rejection:
    scene bg secret_room with fade
    play music "audio/disconnect_theme.mp3" fadein 1.5

    alex "Нет. Это не искупление. Ты не заслужил прощения. Я больше не позволю прошлому определять, кто я."

    shadow "Я... я просто хотел, чтобы ты не страдал. Хоть немного..."

    alex "Ты пытался стереть меня. А теперь просишь быть целым. Прости, но я не тот ребёнок."

    "Ты отворачиваешься. Свет из коридора становится ярче — ты идёшь к выходу. Тень остаётся позади."

    shadow "{color=#666666}Ты прав... Я не заслужил.{/color}"

    "Сзади — тишина. Впереди — город, уже не такой пугающий. Но что-то навсегда останется внутри, неотвеченным."

    $ ending_escape = True
    jump ending_credits
