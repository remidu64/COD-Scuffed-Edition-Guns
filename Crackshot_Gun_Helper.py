REE = open("results.yml", "w")
REE.write("\n")

def p(number):
    """
    Return prime factor list for a given number
        number - an integer number
        Example: get_prime_factors(8) --> [2, 2, 2].
    """
    if number == 1:
        return []

    # We have to begin with 2 instead of 1 or 0
    # to avoid the calls infinite or the division by 0
    for i in range(2, number):
        # Get remainder and quotient
        rd, qt = divmod(number, i)
        if not qt: # if equal to zero
            return [i] + p(rd)

    return [number]

def rpm(rpm):
    bullets = 1
    firerate = round((rpm-300)/60)
    plist = p(firerate)
    while firerate > 15:
        bullets *= plist[0]
        firerate //= plist[0]
        plist = plist[1:]

    return [firerate, bullets]

def creategun():
    gun_id = input("Gun ID ?")

    name = "&e" + input("Gun Name ?")

    type = input("Gun item ? (Put default, Default or 417 to use the default item)")
    if type == "default" or type == "Default":
        type = "417"

    lore = "&e" + input("Gun description ?")

    akimbo = input("Is the gun akimbo ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if akimbo == "1" or akimbo == "True":
        akimbo = "true"
    if akimbo == "0" or akimbo == "False":
        akimbo = "false"

    rightclick = input("Do you use right-click to shoot ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if rightclick == "1" or rightclick == "True":
        rightclick = "true"
    if rightclick == "0" or rightclick == "False":
        rightclick = "false"

    delay = input("Delay in ticks between shots ?")

    recoil = input("Recoil ?")

    bullets = input("Bullets per shot ?")

    drop = input("Do bullets drop ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if drop == "1" or drop == "True":
        drop = "true"
    if drop == "0" or drop == "false":
        drop = "false"

    speed = input("Bullet speed ?")

    damage = input("Damage per bullet ? ")

    incendiarytrig = input("Does the bullet burn the enemies ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if incendiarytrig == "True" or incendiarytrig == "1":
        incendiarytrig = "true"
    if incendiarytrig == "False" or incendiarytrig == "0":
        incendiarytrig = "false"
    if incendiarytrig == "true":
        incendiarytime = input("For how long does the enemies burn when shot ?")
    else:
        incendiarytime = "0"

    spread = input("Spread ? (You can use decimal numbers. The lower, the more precise. A spread of 0.01 is average.)")

    soundshoot = input("Sounds ? (It has to be in the form SOUND-VOLUME-PITCH-DELAY, SOUND2-VOLUME2-PITCH2-DELAY2, etc)")

    fullautotrig = input("Is it fully automatic ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if fullautotrig == "True" or fullautotrig == "1":
        fullautotrig = "true"
    if fullautotrig == "False" or fullautotrig == "0":
        fullautotrig = "false"
    if fullautotrig == "true":
        fire = rpm(int(input("How fast does it shoot IN ROUNDS PER MINUTE")))
        fullautotime = str(fire[0])
        bullets = str(int(bullets)*fire[1])
    else:
        fullautotime = "0"

    if fullautotrig == "false":
        burst = input("Does it have burst fire ? (Put True,true or 1 if yes, put False, false or 0 if no)")
        if burst == "True" or burst == "1":
            burst = "true"
        if burst == 'False' or burst == "0":
            burst = "false"
        if burst == 'true':
            burstamount = input("Shots per burst ?")
            bursttime = input("Delay in ticks between each shots IN A BURST ?")
        else:
            burstamount = "0"
            bursttime = "0"
    else:
        burst = "false"
        burstamount = "0"
        bursttime = "0"

    roundspermag = input("Rounds per mag ?")

    timetoreload = input("Time to reload ?")

    onebyone = input("Do you reload each bullet individually ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if onebyone == "True" or onebyone == "1":
        onebyone = "true"
    if onebyone == "False" or onebyone == "0":
        onebyone = "false"

    soundoutofammo = input("What sound plays when you shoot and you're out of ammo ? (It has to be in the form SOUND-VOLUME-PITCH-DELAY, SOUND2-VOLUME2-PITCH2-DELAY2, etc)")

    soundreloading = input("What sound plays when you reload ? (It has to be in the form SOUND-VOLUME-PITCH-DELAY, SOUND2-VOLUME2-PITCH2-DELAY2, etc)")

    if akimbo == "true":
        singlereloadduration = input("Time ro reload a single gun ?")
    else:
        singlereloadduration = "0"

    firearmtype = input("What type of gun is it ? (valid entries are: slide | bolt | lever | pump | break | revolver . Leave empty if you don't care about this.)")

    if not firearmtype == "":
        timetoopen = input("Time to open in ticks?")
        timetoclose = input("Time to close in ticks ?")
        soundopen = input("Sound when openning ? (It has to be in the form SOUND-VOLUME-PITCH-DELAY, SOUND2-VOLUME2-PITCH2-DELAY2, etc)")
        soundclose = input("Sound when closing ? (It has to be in the form SOUND-VOLUME-PITCH-DELAY, SOUND2-VOLUME2-PITCH2-DELAY2, etc)")
    else:
        timetoopen = ""
        timetoclose = ""
        soundopen = ""
        soundclose = ""

    scopetrig = input("Does it have a scope ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if scopetrig == "True" or scopetrig == "1":
        scopetrig = "true"
    if scopetrig == "False" or scopetrig == "0":
        scopetrig = "false"

    if scopetrig == "true":
        scopezoom = input("How much does the scope z o o m ?")
    else:
        scopezoom = "1"

    headshottrig = input("Does the weapon have headshot damage ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if headshottrig == "True" or headshottrig == "1":
        headshottrig = "true"
    if headshottrig == "False" or headshottrig == "0":
        headshottrig = "false"

    if headshottrig == "true":
        headshotbonusdamage = input("How much damage does a headshot add ?")
    else:
        headshotbonusdamage = "0"

    backstabtrig = input("Does the weapon have backstab damage ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if backstabtrig == "True" or backstabtrig == "1":
        backstabtrig = "true"
    if backstabtrig == "False" or backstabtrig == "0":
        backstabtrig = "false"

    if backstabtrig == "true":
        backstabbonusdamage = input("How much damage does a backstab add ?")
    else:
        backstabbonusdamage = "0"

    explosiontrig = input("Does the gun make explosions ? (Put True,true or 1 if yes, put False, false or 0 if no)")
    if explosiontrig == "True" or explosiontrig == "1":
        explosiontrig = "true"
    if explosiontrig == "False" or explosiontrig == "0":
        explosiontrig = "false"

    if explosiontrig == "true":
        explosionkb = input("How much knockback does the explosion give ?")
        explosiondamagemultiplier = input("What's the explosion damage multiplier (100 is 100% damage, 50 is 50% damage, etc)")
        explosionowner = input("Does the guy who did the explosion get damage from it ? (Put True,true or 1 if yes, put False, false or 0 if no)")
        if explosionowner == "True" or explosionowner == "1":
            explosionowner = "true"
        if explosionowner == "False" or explosionowner == "0":
            explosionowner = "false"
        explosionradius = input("What's the explosion radius ? (4 is average)")
        explosiononimpactwithanything = input("Does the projectile explode when it impacts literally anything ? (Put True,true or 1 if yes, put False, false or 0 if no)")
        if explosiononimpactwithanything == "True" or explosiononimpactwithanything == "1":
            explosiononimpactwithanything = "true"
        if explosiononimpactwithanything == "False" or explosiononimpactwithanything == "0":
            explosiononimpactwithanything = "false"
    else:
        explosiondamagemultiplier = "0"
        explosionowner = "true"
        explosionradius = "1"
        explosiononimpactwithanything = "true"
        explosionkb = "1"

    kb = input("How much knockback does the enemies get when shot ? (Put 0 if you don't care)")

    result = f"    {gun_id}:\n" \
             f"        Item_Information:\n" \
             f"            Item_Name: \"{name}\"\n" \
             f"            Item_Lore: \"{lore}\"\n" \
             f"            Item_Type: {type}\n" \
             f"            Sounds_Acquired: BAT_TAKEOFF-1-1-0\n" \
             f"        Shooting:\n" \
             f"            Recoil_Amount: {recoil}\n" \
             f"            Right_Click_To_Shoot: {rightclick}\n" \
             f"            Cancel_Left_Click_Block_Damage: true\n" \
             f"            Cancel_Right_Click_Interactions: true\n" \
             f"            Dual_Wield: {akimbo}\n" \
             f"            Projectile_Amount: {bullets}\n" \
             f"            Projectile_Type: snowball\n" \
             f"            Remove_Bullet_Drop: {drop}\n" \
             f"            Projectile_Speed: {speed}\n" \
             f"            Projectile_Damage: {damage}\n" \
             f"            Projectile_Flames: {incendiarytrig}\n" \
             f"            Projectile_Incendiary:\n" \
             f"                Enable: {incendiarytrig}\n" \
             f"                Duration: {incendiarytime}\n" \
             f"            Bullet_Spread: {spread}\n" \
             f"            Sounds_Shoot: {soundshoot}\n" \
             f"        Fully_Automatic:\n" \
             f"            Enable: {fullautotrig}\n" \
             f"            Fire_Rate: {fullautotime}\n" \
             f"        Burstfire:\n" \
             f"            Enable: {burst}\n" \
             f"            Shots_Per_Burst: {burstamount}\n" \
             f"            Delay_Between_Shots_In_Burst: {bursttime}\n" \
             f"        Reload:\n" \
             f"            Enable: true\n" \
             f"            Reload_Amount: {roundspermag}\n" \
             f"            Reload_Duration: {timetoreload}\n" \
             f"            Reload_Bullets_Individually: {onebyone}\n" \
             f"            Sounds_Out_Of_Ammo: {soundoutofammo}\n" \
             f"            Sounds_Reloading: {soundreloading}\n"
    if akimbo == "true":
        result += f"            Dual_Wield:\n" \
                  f"                Single_Reload_Duration: {singlereloadduration}\n" \
                  f"                Sounds_Single_Reload: {soundreloading}\n" \
                  f"                Sounds_Shoot_With_No_Ammo: {soundoutofammo}\n"

    if not firearmtype == "":
        result += f"        Firearm_Action:\n" \
                  f"            Type: {firearmtype}\n" \
                  f"            Open_Duration: {timetoopen}\n" \
                  f"            Close_Duration: {timetoclose}\n" \
                  f"            Sound_Open: {soundopen}\n" \
                  f"            Sound_Close: {soundclose}\n"

    result+= f"        Scope:\n" \
             f"            Enable: {scopetrig}\n" \
             f"            Zoom_Amount: {scopezoom}\n" \
             f"            Sounds_Toggle_Zoom: NOTE_STICKS-1-2-0\n" \
             f"        Headshot:\n" \
             f"            Enable: {headshottrig}\n" \
             f"            Bonus_Damage: {headshotbonusdamage}\n" \
             f"            Sounds_Shooter: NOTE_PLING-1-2-0\n" \
             f"            Sounds_Victim: VILLAGER_DEATH-1-1-0\n" \
             f"        Fireworks:\n" \
             f"            Enable: true\n" \
             f"            Firework_Headshot: STAR-TRUE-TRUE-250-0-0\n" \
             f"        Backstab:\n" \
             f"            Enable: {backstabtrig}\n" \
             f"            Bonus_Damage: {backstabbonusdamage}\n" \
             f"            Sounds_Shooter: NOTE_PLING-1-2-0\n" \
             f"            Sounds_Victim: VILLAGER_DEATH-1-1-0\n" \
             f"        Explosions:\n" \
             f"            Enable: {explosiontrig}\n" \
             f"            Knockback: {explosionkb}\n" \
             f"            Damage_Multiplier: {explosiondamagemultiplier}\n" \
             f"            Enable_Owner_Immunity: {explosionowner}\n" \
             f"            Explosion_No_Grief: true\n" \
             f"            Explosion_Radius: {explosionradius}\n" \
             f"            On_Impact_With_Anything: {explosiononimpactwithanything}\n" \
             f"        Abilities:\n" \
             f"            Reset_Hit_Cooldown: true\n" \
             f"            Knockback: {kb}"

    REE.write(result)
    REE.close()

creategun()