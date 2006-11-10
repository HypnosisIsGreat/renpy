﻿# This script and the artwork associated with it, is in the
# public domain. Feel free to use it as the basis for your own
# game.

# If you're trying to understand this script, I recommend skipping
# down to the line beginning with 'label start:', at least on your
# first read-through.

# This init block runs first, and sets up all sorts of things that
# are used by the rest of the game. Variables that are set in init
# blocks are _not_ saved, unless they are changed later on in the
# program.

init:
    
    # Set up the size of the screen, and the window title.
    $ config.screen_width = 800
    $ config.screen_height = 600
    $ config.window_title = "The Ren'Py Demo Game"

    # Set up the theme for this game. This must be after the
    # library.script_version and config.screen_width lines.
    $ theme.roundrect()

    # Set this to true to enable some developer-specific
    # functionality. It should be false in a finished game.
    # Read the "Developer Tools" section of the reference
    # to see what this enables.
    $ config.developer = True

    # Declare the images that are used in the program.

    # Backgrounds.
    image bg carillon = "carillon.jpg"
    image bg whitehouse = "whitehouse.jpg"
    image bg washington = "washington.jpg"
    image bg onememorial = "1memorial.jpg"
    image black = Solid((0, 0, 0, 255))

    # Character pictures.
    image eileen happy = "9a_happy.png"
    image eileen vhappy = "9a_vhappy.png"
    image eileen concerned = "9a_concerned.png"

    # Character objects. These lets us have the character say
    # dialogue without us having to repeatedly type her name. It also
    # lets us change the color of her name.
    $ e = Character(u'Eileen', color=(200, 255, 200, 255))
    $ ee = e.copy("Yellow Eileen", color="#ff0", what_size=42)
    

# The start label marks the place where the main menu jumps to to
# begin the actual game.

label start:

    ee "This is a test."

    ee "This is also a test."
    
    # The save_name variable sets the name of the save game. Like all
    # variables declared outside of init blocks, this variable is
    # saved and restored with a save file.
    $ save_name = "Introduction"

    # This variable is only used by our game. If it's true, it means
    # that we won the date.
    $ date = False

    # Clear the game runtime timer, so it doesn't reflect time spent
    # sitting at the main menu.
    $ renpy.clear_game_runtime()        

    # Start some music playing in the background.
    $ renpy.music.play('sun-flower-slow-drag.mid')

    # Now, set up the first scene. We first fade in our washington
    # background, and then we dissolve in the image of Eileen on top
    # of it.
    scene bg washington with fade
    show eileen vhappy with dissolve
    
    # Store the current version of Ren'Py into a variable, so we can
    # interpolate it into the next line.
    $ version = renpy.version()

    # Display a line of dialogue. In this case, we manually specify
    # who's saying the line of dialogue. We also interpolate in the
    # version of Ren'Py we're using.
    "Girl" "Hi, and welcome to the %(version)s demo program."

    # This instantly replaces the very happy picture of Eileen with
    # one showing her merely happy. It demonstrates how the show
    # statement lets characters change emotions.
    show eileen happy
  
    # Another line of dialogue.
    "Girl" "My name is Eileen, and while I hope to one day star in a
            real game, for now I'm here to tell you about Ren'Py."

    # This line uses the e character object, which displays Eileen's
    # name in green. The use of a short name for a character object
    # lets us save typing when writing the bulk of the dialogue.
    e "Ren'Py is a language and engine for writing and playing visual
       novel games."

    e "Our goal is to allow people to be able to write the script for
       a game, and with very little effort, turn that script into
       a working game."

    e "I can tell you about the features of Ren'Py games, or how to write
       your own game. What do you want to know about?"

    # This variable is used to save the choices that have been made in
    # the main menu.
    $ seen_set = [ ]

label choices:

    # We change the save name here.
    $ save_name = "Question Menu"

    # This is the main menu, that lets the user decide what he wants
    # to hear about.
    menu:

        # The set menu clause ensures that each menu choice can only
        # be chosen once.
        set seen_set

        # This is a menu choice. When chosen, the statements in its
        # block are executed.
        "What are some features of Ren'Py games?":

            # We call the features label. The from clause needs to be
            # here to ensure that save games work, even after we
            # change the script. It was added automatically.
            call features from _call_features_1

            # When we're done talking about features, jump back up
            # to choices.
            jump choices

        # Another choice. 
        "How do I write my own games with it?":
            call writing from _call_writing_1
            jump choices

        "Can you demonstrate more features to me?":
            call demonstrate from _call_demonstrate_1
            jump choices

        # This choice has a condition associated with it. It is only
        # displayed if the condition is true (in this case, if we have
        # selected at least one other choice has been chosen.) 
        "Where can I find out more?" if seen_set:
            call find_out_more from _call_find_out_more_1
            jump choices

        "Why are we in Washington, DC?":
            call washington from _call_washington_1
            jump choices

        "I think I've heard enough." if seen_set:
            jump ending


# This is the section on writing games.
label writing:

    # Change the title of the save games.
    $ save_name = "Writing Games"

    # We start off with a bunch of dialogue.
    e "If you want to write a game, we recommend that you read the
       Ren'Py reference, which you can get from our web page,
       http://www.bishoujo.us/renpy/."

    e "But here, we'll go over some of the basics of writing Ren'Py
       scripts. It might make sense if you open the source for this
       game."

    e "The source for this game can be found in the file
       game/script.rpy."

    e "The goal of Ren'Py is to make writing the game similar to
       typing up the script on the computer."

    e "For example, a line of dialogue is expressed by putting the
       character's name next to the dialogue string."

    # A string by itself like this displays without a name associated
    # with it. So it's useful for dialogue and narration.
    "I somehow remember that strings by themselves are displayed as
     thoughts or narration."
    
    e "The menu statement makes it easy to create menus."

    e "A number of statements let you control what is shown on the
       screen."

    # This scene statement has a with clause associated with it. In
    # this case (based on what is defined in the init clause at the
    # top of this script), it causes a fade to black, and then back
    # to the new scene.
    scene bg whitehouse with fade

    e "The scene statement clears the scene list, which is the list of
       things that are shown on the screen."

    # This shows an image, and dissolves it in.
    show eileen happy with dissolve

    e "The show statement shows another image on the screen."

    # The at clause here, displays the character on the left side of
    # the screen. The with clause causes us to slide from the old
    # position to the new position.
    show eileen happy at left with move

    e "Images can take at clauses that specify where on the screen
       they are shown."

    show eileen vhappy at left

    e "Showing a new image with the same first part of the name
       replaces the image in the scene list."

    hide eileen with dissolve

    e "Finally, the hide statement hides an image, which is useful
       when a character leaves the scene."

    show eileen happy with dissolve

    e "Don't worry, I'm not going anywhere."

    e "The with statement is used to cause transitions to
       happen. Transitions like fade..."

    # This statement hides the transient stuff from being included
    # in the next fade.
    with None

    # This with statement causes things to fade without changing the
    # scene.
    with fade

    e "... or dissolve ..."

    # In this block, the scene statement clears the scene list. So we
    # have to reshow the eileen happy image, so that it appears that
    # just the background is dissolving. Sneaky.
    with None
    scene bg washington
    show eileen happy
    with dissolve

    e "... are easily invoked."

    e "We now provide a series of user-interface functions, that allow
       the programmer to create fairly complex interfaces."

    e "Ren'Py also includes a number of control statements, and even
       lets you include python code."

    e "Rather than go into this here, you can read all about it in the
       reference."

    e "You can see a number of features in action by asking me to
       demonstrate them at the next menu."

    e "If you want to make changes, you can edit the script for this
       game by editing game/script.rpy"

    e "When you've made a change, just re-run the game to see your
       change in action."

    e "Would you like to know about something else?"

    # We return back up to the menu that lets the user pick a topic.
    return

# This ends the well-commented portion of this script.

label features:

    $ save_name = "Features"

    e "Ren'Py provides a number of gameplay features, giving the user
       a good experience while freeing up the game author to write his
       game."

    e "What are some of these features? Well, first of all, we take
       care of displaying the screen, as well as dialogue and menus."

    e "You can navigate through the game using the keyboard or the
       mouse. If you've gotten this far, you've probably figured that
       out already."

    e "Right-clicking or pressing escape will bring you to the game
       menu."

    e "The game menu lets you save or load the game. Ren'Py doesn't
       limit the number of save slots available. You can create as
       many slots as you can stand."

    e "A preferences screen on the game menu lets you change the
       fullscreen mode, control skipping, text speed, and
       transitions, and turn sound and music on and off."

    e "The game menu also lets you restart or quit the game. But you
       wouldn't want to do that, would you?"

    e "Finally, the game menu lets you set up the game
       preferences. These preferences are saved between games."

    show eileen vhappy

    e "The next feature is really neat."

    show eileen happy

    menu rollback_menu:
        "Would you like to hear about rollback?"
        
        "Yes.":
            pass

        "No.":
            jump after_rollback


    e "Rollback is a feature that only Ren'Py has. It lets you go back
       in time in a game."

    e "For example, you can go back to a menu and save or make a
       different choice."

    e "You can access it by pressing page up or scrolling up on your
       mouse wheel."

    e "Why don't you try it by going back to the last menu and
       choosing 'No.' instead of 'Yes.'"

    e "Press page up or scroll up the mouse wheel."

    show eileen concerned

    e "Well, are you going to try it?"

    e "Your loss."

    e "Moving on."

label after_rollback:

    show eileen happy
    
    e "Ren'Py gives you a few ways of skipping dialogue. Pressing
       control quickly skips dialogue you've seen at least once."

    e "Pressing Tab toggles the skipping of dialogue you've seen at
       least once."

    e "Pressing page down or scrolling the mouse wheel down will let
       you skip dialogue you've seen this session. This is useful
       after a rollback."

    e "If you want to try these, you might want to rollback a bit
       first, so you can skip over something you've seen already."

    e "Finally, Ren'Py has predictive image loading, so you rarely
       have to wait for a new image to load."

    e "Remember, all these features are built into the engine or
       standard library. So every game written with Ren'Py has them."

    e "Is there anything else you'd like to know about?"
    
    return


label find_out_more:

    $ save_name = "Find Out More"

    e "There are a few places you can go to find out more about
       Ren'Py."

    e "The Ren'Py homepage, http://www.bishoujo.us/renpy/, is probably
       the best place to start."

    e "There, you can download new versions of Ren'Py, and read the
       tutorial online."

    e "If you have questions, the best place to ask them is the Ren'Py
       forum of the Lemmasoft forums."

    e "Just go to http://lemmasoft.renai.us/forums/, and click on
       Ren'Py."

    e "We thank Blue Lemma for hosting our forum."

    e "Finally, feel free to email or IM us if you need help. You can
       get the addresses to use from http://www.bishoujo.us/renpy/."

    e "We really want people to make their own games with Ren'Py, and
       if there's anything we can do to help, just tell us."

    e "Is there anything I can help you with now?"

    return

label washington:

    $ save_name = "Washington, DC"

    e "We're in Washington, DC because over Summer 2004 American
       Bishoujo's home base was just outside of DC."

    scene bg whitehouse
    show eileen happy at left
    with fade

    e "Even though we've moved back to New York, we took a bunch of
       pictures, and decided to use them."

    show eileen concerned at left

    e "It was easier than drawing new pictures for this demo."

    show eileen happy at left
    
    e "Do you have a favorite landmark in or around DC?"

    menu:

        "The White House.":

            e "I was supposed to go on a tour of the West Wing, once."

            show eileen concerned

            e "They wouldn't let us in."

            e "The secret service guy who was supposed to show us
               around was out of town that day."

            e "Too bad."

        "The National Mall.":

            e "It's always fun to go down to the national mall."

            e "You can visit the monuments, or see one of the
               museums."

            e "I guess you could run out of things to do after a while
               but I didn't over the course of a summer."
            
        "The Netherlands Carillon.":
            jump netherlands
            
    jump post_netherlands

label netherlands:

    show eileen vhappy at left

    e "You've been to the Netherlands Carillon?"

    scene bg carillon
    show eileen vhappy at left
    with dissolve

    e "It may not be much to look at but the sound of the bells is
       really neat."

    e "I love going there. Saturdays during the summer, they have
       these recitals in the park where a guy comes and plays the 
       bells live."

    e "You can climb to the top and talk to him, if you're not afraid
       of heights."

    e "Once, I saw a little girl there, maybe three or four years old.
       The guy played the bumblebee song for here, and he even let her play the last
       note. It was so cute!"

    e "I haven't been there for so long."

    menu:
        "Would you like to go there sometime?":

            e "You mean, together?"

            e "Sure, why not. How does next Saturday sound?"
            
            e "It's a date."

            $ date = True

        "That sounds nice.":

            show eileen happy at left

            e "Well, it is."
        
label post_netherlands:

    scene bg washington
    show eileen happy
    with fade

    e "Anyway, is there anything else you want to know about Ren'Py?"

    return

label ending:

    $ save_name = "Ending"

    e "Well, that's okay."

    e "I hope you'll consider using Ren'Py for your next game
       project."

    show eileen vhappy

    e "Thanks for viewing this demo!"

    if date:
        e "And I'll see you on Saturday."
    
    scene black with dissolve

    "Ren'Py and the Ren'Py demo were written by PyTom."

    "The character art was done by Piroshki (from the Lemmasoft forums)."

    'The background music is "Sun Flower Slow Drag" by S. Joplin
     (1868-1917). Thanks to the Mutopia project for making it
       available.'

    'The author would like to thank everyone who makes original
     English-language bishoujo games, and the people on the Lemmasoft forums
     who encouraged him.'

    "We can't wait to see what you do with this. Good luck!"

    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    "It took you %(minutes)d minutes and %(seconds)d seconds to
     finish this demo."
       
    $ renpy.full_restart()


label speedtest:

    with None
    scene bg whitehouse
    show eileen happy
    with dissolve

    e "Okay, I'm going to run the speedtest on your system."

    e "I'll only be testing the performance of the dissolve
       transition. It taxes your system the most, as it needs to
       redraw the entire screen each frame."

    $ frames = config.frames

    with None
    scene bg washington
    show eileen happy
    with Dissolve(5.0)

    $ frames = config.frames - frames
    $ fps = frames / 5.0

    e "Well, your system displayed %(frames)d frames in five
       seconds. That's %(fps).1f fps."

    e "Remember, this is the worst-case speed, as usually we can just
       draw the parts of the screen that have changed."

    e "Thanks for viewing the secret speed test."

    return

label developer:

    scene black

    # It's bad form to change a config variable outside of an init
    # block. We're only doing this to help test the game. Don't do
    # it in your own game.
    $ config.developer = True

    "Developer mode enabled. You can now use '>' to warp to the next
     menu."

    $ config.log = "log.txt"

    "Logging enabled. You can now find a log of this game in log.txt."

    return
    
# Setup the secret keys for the speedtest and developer mode.
init:
    python:
        config.keymap['speedtest'] = [ 'S' ]
        config.keymap['developer'] = [ 'D' ]
        config.underlay.append(renpy.Keymap(
            speedtest=renpy.curried_call_in_new_context('speedtest'),
            developer=renpy.curried_call_in_new_context('developer')))

init:

    # This is just some example code to show the ui functions in
    # action. You probably want to delete this (and the call to
    # day_planner above) from your game. This code isn't really all
    # that useful except as an example.
    
    python:
        def day_planner():

            periods = [ 'Morning', 'Afternoon', 'Evening' ]
            choices = [ 'Study', 'Exercise',
                        'Eat', 'Drink', 'Be Merry' ]

            plan = { 'Morning' : 'Eat',
                     'Afternoon' : 'Drink',
                     'Evening' : 'Be Merry' }

            day = 'March 25th'

            stats = [
                ('Strength', 100, 10),
                ('Intelligence', 100, 25),
                ('Moxie', 100, 100),
                ('Chutzpah', 100, 75),
                ]

            editing = None

            def button(text, selected, returns, **properties):
                style='selected_button'
                style_text='selected_button_text'
                    
                if selected:
                    role='selected_'
                else:
                    role=''

                ui.button(clicked=ui.returns(returns),
                          style='button', role=role, **properties)
                ui.text(text, style='button_text')


            while True:

                # Stats Window
                ui.frame(xpos=0,
                         ypos=0,
                         xanchor='left',
                         yanchor='top',
                         xfill=True,
                         )

                ui.vbox()

                ui.text('Statistics')
                ui.null(height=20)

                for name, range, value in stats:

                    ui.hbox()
                    ui.text(name, minwidth=150)
                    ui.bar(range, value, ypos=0.5, yanchor='center')
                    ui.close()

                ui.close()
                
                

            
                # Period Selection Window.
                ui.frame(xpos=0,
                         ypos=200,
                         xanchor='left',
                         yanchor='top',
                         xfill=False,
                         xminimum=300
                         )
                
                ui.vbox(xpos=0.5, xanchor='center')
                ui.text(day, xpos=0.5, xanchor='center', textalign=0.5)
                ui.null(height=20)
                
                for i in periods:
                    face = i + ": " + plan[i]
                    button(face, editing == i, ("edit", i), xminimum=250)

                ui.null(height=20)
                ui.textbutton("Continue", clicked=ui.returns(("done", True)), xminimum=250)
                ui.null(height=20)
                ui.close()


                # Choice window.
                if editing:
                    ui.frame(xpos=300,
                              ypos=200,
                              xanchor='left',
                              yanchor='top',
                              xfill=False,
                              xminimum=500
                              )
                
                    ui.vbox()
                    ui.text("What will you do in the %s?" % editing.lower())
                    ui.null(height=20)

                    for i in choices:
                        button(i, plan[editing] == i, ("set", i),
                               xpos=0, xanchor='left')

                    ui.close()

                # Window at the bottom.
                ui.window()
                ui.vbox()
                ui.text("To get to the next screen, click the 'Continue' button.")
                ui.close()

                type, value = ui.interact()

                if type == "done":
                    break

                if type == "edit":
                    editing = value

                if type == "set":
                    plan[editing] = value
                    editing = None

            return plan

init:
    image movie = Movie()

    python:
        povname = ""
        pov = DynamicCharacter("povname", color=(192, 64, 64, 255))

    $ ectc = Character('Eileen', color=(200, 255, 200, 255),
                       ctc = anim.Blink("arrow.png"))

    $ ectcf = Character('Eileen', color=(200, 255, 200, 255),
                        ctc = anim.Filmstrip("sakura.png", (20, 20), (2, 1), .30, xpos=760, ypos=560, xanchor=0, yanchor=0),
                        ctc_position="fixed")

    $ equote = Character('Eileen',  color=(200, 255, 200, 255),
                         who_suffix = ':', what_prefix='"', what_suffix='"')

    $ eweird = Character('Eileen', color=(200, 255, 200, 255),
                         what_underline=True, window_left_margin=200,
                         window_yminimum=300)

    $ etwo = Character('Eileen', color=(200, 255, 200, 255),
                       show_two_window=True)

    $ eside = Character('Eileen', color=(200, 255, 200, 255),
                        window_left_margin=270,
                        show_side_image=Image("9a_happy.png", xalign=0.0, ypos=380))

    image eileen animated = Animation(
        "9a_vhappy.png", 1.0,
        "9a_happy.png", 1.0)

    image smanim = anim.SMAnimation(
        "r",
        anim.State("r", Solid((255, 0, 0, 255))),
        anim.State("g", Solid((0, 255, 0, 255))),
        anim.State("b", Solid((0, 0, 255, 255))),

        anim.Edge("r", .5, "g", dissolve),
        anim.Edge("r", .5, "b", dissolve),

        anim.Edge("g", .5, "r", dissolve),
        anim.Edge("g", .5, "b", dissolve),

        anim.Edge("b", .5, "r", dissolve),
        anim.Edge("b", .5, "g", dissolve),         
        )

    # There's no reason to use DynamicDisplayable here, except to test it.
    image cyan base = DynamicDisplayable("Image('cyan.png')")

    image cyan crop = im.Crop("cyan.png", 100, 0, 100, 200)

    image cyan scale = im.Scale("cyan.png", 100, 100) 
    
    image cyan composite = im.Composite((200, 300),
                                        (0, 0), "cyan.png",
                                        (0, 50), "cyan.png",
                                        (0, 100), "cyan.png")

    image cyan livecomposite = LiveComposite((200, 300),
                                             (0, 0), anim.Blink(Image("cyan.png")),
                                             (0, 50), "cyan.png",
                                             (0, 100), "cyan.png")

    image cyan green = im.Map("cyan.png", bmap=im.ramp(0, 0))

    image cyan green2 = im.Recolor("cyan.png", 255, 255, 0, 255)

    image cyan alpha = im.Alpha("cyan.png", 0.5)

    image cyan blackwhite = "blackwhite.png"

    image cyan twocolor = im.Twocolor("blackwhite.png",
                                      (0, 255, 255, 255),
                                      (255, 255, 0, 255))

    image eileen alpha = im.Alpha("9a_happy.png", 0.5)

    image eileen flip = im.Flip("9a_happy.png", vertical=True)

    $ cyanpos = Position(xpos=700, xanchor='right', ypos=100, yanchor='top')

    $ slowcirciris = ImageDissolve("circiris.png", 5.0, 8)
    $ circirisout = ImageDissolve("circiris.png", 1.0, 8)
    $ circirisoutramp = ImageDissolve("circiris.png", 3.0, ramp=[ 16 * i for i in range(0, 15) + range(15, 0, -1) + range(0, 15) + range(15, 0, -1) + range(0, 15)  + range(15, 0, -1) + range(0, 15) ] )
    $ circirisin = ImageDissolve("circiris.png", 1.0, 8, reverse=True)

    $ demotrans = ImageDissolve("demotrans.png", 3.0, 16)

    image circiris = "circiris.png"

    image snowblossom = SnowBlossom(anim.Filmstrip("sakura.png", (20, 20), (2, 1), .15), fast=True)

    $ renpy.register_sfont("skyfont", 22, filename="skyfont.png", default_kern=-1)

    $ esf = Character('Eileen', color=(200, 255, 200, 255),
                      what_font="skyfont", what_size=22,
                      what_drop_shadow=(1, 1))

    $ style.frame.background = Frame("frame.png", 12, 12)

    $ definition = Character(None, window_yfill=True, window_xmargin=20, window_ymargin=20, window_background=Solid((0, 0, 0, 192)))

    $ config.layers.insert(1, 'demo')
    $ config.layer_clipping['demo'] = (50, 50, 700, 500)

    
label demonstrate:

    scene bg washington
    show eileen happy

    e "I can give you a demonstration of some of the features in
       Ren'Py, but you'll have to tell me what it is you'd like to
       have demonstrated."

    menu demo_menu:

        "Simple transitions, updated in 4.8.5":

            e "Okay, I can tell you about simple transitions. We call
               them simple because they aren't that flexible."

            e "But don't let that get you down, since they're the
               transitions you'll probably use the most."

            with None
            scene bg whitehouse
            show eileen happy
            with dissolve

            e "The dissolve transition is probably the most useful,
               blending one scene into another."

            with None
            with fade

            e "The fade transition fades to black, and then fades back
               in to the new scene."

            e "If you're going to stay at a black screen, you'll
               probably want to use dissolve rather than fade."

            with None
            scene bg washington
            show eileen happy
            with pixellate

            e "The pixellate transition pixellates out the old scene,
               switches to the new scene, and then unpixellates that."

            e "It's probably not appropriate for most games, but we
               think it's kind of neat."

            e "Finally, we can point out that motions can be used as
               transitions."

            "..."

            "......"

            $ renpy.play('punch.wav')
            with vpunch

            e "Hey! Pay attention."

            e "I was about to demonstrate vpunch... well, I guess I just
               did."

            $ renpy.play('punch.wav')
            with hpunch

            e "We can also shake the screen horizontally, with hpunch."

        "ImageDissolve transitions, updated in 5.3.1.":

            e "ImageDissolve allows us to have dissolve transitions that are
               controlled by images."

            e "This lets us specify very complex transitions, fairly
               simply."

            e "Let's try some, and then I'll show how they work."

            e "There are two ImageDissolve transitions present by
               default in the standard library."
            
            scene black with blinds
            scene bg washington
            show eileen happy
            with blinds

            e "The blinds transition opens and closes what looks like
               vertical blinds."

            scene black with squares
            scene bg washington
            show eileen happy
            with squares

            e "The squares transition uses these squares to show
               things."

            e "I'm not sure why anyone would want to use it, but it
               was used in some translated games, so we added it."

            e "There are also a few transitions that aren't in the
               standard library."

            e "These ones require images the size of the screen, and
               so we couldn't include them as the size of the screen
               can change from game to game."

            e "You can find them defined in the source of the demo
               script."

            scene black with circirisin

            e "We can hide things with a circirisin..."

            with None
            scene bg washington
            with circirisout

            e "... and show them again with a circirisout."

            e "The ramp parameter lets things dissolve in and out
               along the way."

            scene bg whitehouse with circirisoutramp

            e "It's even possible to have weird custom transitions."

            scene circiris with demotrans

            e "What we're showing here is the picture that's used in
               the circiris transitions."

            e "If you take a look, the center of it is white, while
               the edges are darker."

            e "When we use an ImageDissolve, the white will dissolve
               in first, followed by progressively darker colors."

            e "Let's try it."

            with None
            scene bg washington
            show eileen happy
            with slowcirciris

            
            e "It's also possible to reverse the transition, so that
               the black pixels are dissolved in first."

        "CropMove transitions, added in 4.5.":

            e "The CropMove transition class lets us provide a wide
               range of transition effects."

            hide eileen with dissolve

            e "I'll stand offscreen, so you can see some of its modes. I'll read
               out the mode name after each transition."

            scene bg whitehouse with wiperight

            e "We first have wiperight..."

            scene bg washington with wipeleft

            e "...followed by wipeleft... "    

            scene bg whitehouse with wipeup

            e "...wipeup..."

            scene bg washington with wipedown

            e "...and wipedown."

            e "Next, the slides."

            scene bg whitehouse with slideright

            e "Slideright..."

            scene bg washington with slideleft

            e "...slideleft..."

            scene bg whitehouse with slideup

            e "...slideup..."

            scene bg washington with slidedown

            e "and slidedown."

            e "While the slide transitions slide in the new scene, the
               slideaways slide out the old scene."

            scene bg whitehouse with slideawayright

            e "Slideawayright..."

            scene bg washington with slideawayleft

            e "...slideawayleft..."

            scene bg whitehouse with slideawayup

            e "...slideawayup..."

            scene bg washington with slideawaydown

            e "and slideawaydown."

            e "We also have a couple of transitions that use a
               rectangular iris."

            scene bg whitehouse with irisout

            e "There's irisout..."

            with None
            scene bg washington
            show eileen happy
            with irisin

            e "... and irisin."

            e "It's enough to make you feel a bit dizzy."
            
        "Positions and movement, updated in 5.6.0.":

            e "I'm not stuck standing in the middle of the screen,
               even though I like being the center of attention."

            e "Positions, given with an at clause, specify where I'm
               standing."

            e "The move transition moves around images that have
               changed position."

            e "For example..."

            show eileen happy at offscreenleft with move

            e "I can move over to the offscreenleft position, just off
               the left side of the screen."

            show eileen happy at left with move

            e "The left position has my left side border the left
               margin of the screen."

            show eileen happy at center with move

            e "I can also move to the center..."

            show eileen happy at right with move

            e "... the right ..."

            show eileen happy at offscreenright with move

            e "... or even to offscreenright, off the right-hand side
               of the screen."

            show eileen happy at right with move

            e "We don't limit you to these five positions either. You
               can always create your own Position objects."

            # This is necessary to restart the time at which we are
            # shown. 
            hide eileen happy

            show eileen happy at Move((1.0, 1.0, 'right', 'bottom'),
                                      (0.0, 1.0, 'left', 'bottom'),
                                      4.0, repeat=True, bounce=True)

            e "It's also possible to have a movement happen while
               showing dialogue on the screen, using the Move function."

            e "Move can repeat a movement, and even have it bounce
               back and forth, like I'm doing now."
            
            scene bg onememorial at Pan((0, 800), (0, 0), 10.0) with dissolve

            e "We can pan around an image larger than the
               screen, using the Pan function in an at
               clause."

            e "That's what we're doing now, panning up a picture of
               the memorial to the Big Red One."

            scene bg whitehouse with dissolve
            scene bg whitehouse at Zoom((800, 600), (0, 0, 800, 600), (225, 150, 400, 300), 1.0)

            e "We can zoom into images..."

            scene bg whitehouse at Zoom((800, 600), (225, 150, 400, 300), (0, 0, 800, 600), 1.0)

            e "... and zoom back out of them again."

            scene bg whitehouse
            show eileen happy at FactorZoom(1.0, 0.5, 1.0, opaque=False), center

            e "We can also zoom images by a factor..."

            show eileen happy at FactorZoom(0.5, 1.0, 1.0, opaque=False), center

            e "... and zoom {i}them{/i} out again."
            
        
            with None
            scene bg washington
            show eileen happy
            with dissolve

            show snowblossom

            e "Finally, there's now a particle motion system in
               Ren'Py."

            e "It can be used to animate things like falling cherry
               blossoms, falling snow, and rising bubbles."

            e "While there's convenient support for things rising and
               falling in straight lines, it's also possible to define
               your own motions."

            e "The sky's the limit."

            e "Or the ground, in the case of these cherry blossoms."

            hide snowblossom with dissolve

        "Animation, updated in 4.8.5":

            e "Ren'Py supports a number of ways of creating
               animations."

            e "These animations let you vary images, independent of
               the user's clicks."

            show eileen animated

            e "For example, I'm switching my expression back and
               forth, once a second."

            e "Even though you clicked, I'm still doing it."

            e "This is an example of the Animation function at work."

            show eileen happy

            e "The Animation function is limited to simple lists of
               images, with fixed delays between them."

            e "The sequence can repeat, or can stop after one
               go-through."

            e "If you want more control, you can use the
               anim.SMAnimation function."

            e "It can randomly change images, and even apply
               transitions to changes."

            with None
            scene smanim
            show eileen happy
            with dissolve

            e "Here, we randomly dissolve the background between red,
               green, and blue images."

            e "Psychadelic."

            with None
            scene bg washington
            show eileen happy
            with dissolve

            e "It's probably best if we stop here, before somebody's
               brain explodes."

        "Fonts and Text Tags, updated in 5.5.1.":

            e "Text tags let us control the appearance of text that is
               shown to the user."

            e "Text tags can make text {b}bold{/b}, {i}italic{/i}, or
               {u}underlined{/u}."

            e "They can make the font size {size=+12}bigger{/size} or
               {size=-8}smaller{/size}."

            e "They let you pause{w} the display of the text,
               optionally with{p}line breaks."

            e "They let you include {image=slider_idle.png} images
               inside text."

            e "They can even change the
               {color=#f00}color{/color}
               {color=#ff0}of{/color}
               {color=#0f0}the{/color}
               {color=#0ff}text{/color}."

            e "There are also bold, italic, and underline style properties, which can
               be styled onto any text."

            e "{a=define_hyperlink}Hyperlinks{/a} let buttons be
               defined as using text tags."

            e "If you find yourself using text tags on every line, you
               should probably look at style properties instead."

            e "Used with care, text tags can enhance {b}your{/b} game."

            e "{u}Used{/u} with {i}abandon,{/i} they {b}can{/b} make {b}your{/b}
               game {color=#333}hard{/color} {color=#888}to{/color} {color=#ccc}read{/color}."

            e "With great power comes great responsibility, after all."

            e "And we want to give you all the power you need."

            esf "For even more control, Ren'Py supports SFonts."

            esf "An SFont is an image file containing font
                 information."

            esf "SFonts let you use fonts you otherwise couldn't, and
                 apply special effects to fonts... like I'm doing
                 now."

            e "We recommend keeping your usual font simple and readable."

            esf "Not like this one."

        "Music, sound and movies, updated in 4.5.":
            
            e "Ren'Py supports a number of multimedia functions."

            e "You're probably hearing music playing in the
               background."


            $ renpy.music_stop(fadeout=0.5)
            e "We can stop it..."


            $ renpy.music_start('sun-flower-slow-drag.mid')
            e "... and start it playing again."
            
            # This plays a sound effect.
            $ renpy.play("18005551212.ogg")

            e "We can also play up to eight channels of sound effects
               on top of the music."

            e "We ship, in the extras/ directory, code to support
               characters having voice."

            e "Finally, we support playing mpeg movies."
    
            if renpy.exists('Eisenhow1952.mpg'):

                e "Since you downloaded the Eisenhower commercial, I can show
                   it to you as a cutscene."

                e "You can click to continue if it gets on your nerves too
                   much."

                $ renpy.movie_cutscene('Eisenhow1952.mpg', 63.0)

                hide eileen
                show movie at Position(xpos=420, ypos=25, xanchor='left', yanchor='top')
                show eileen happy

                $ renpy.movie_start_displayable('Eisenhow1952.mpg', (352, 240))

                e "Ren'Py can even overlay rendered images on top of a movie,
                   although that's more taxing for your CPU."

                e "It's like I'm some sort of newscaster or something."

                $ renpy.movie_stop()
                hide movie

                $ renpy.music_start('sun-flower-slow-drag.mid')

            else:

                e "You haven't downloaded the Eisenhower commercial, so we
                   can't demonstrate it."

            e "That's it for multimedia."

        "Image Operations, updated in 5.6.0":

            e "Image operations allow one to manipulate images as they
               are loaded in."

            e "These are efficient, as they are only evaluated when an
               image is first loaded."

            e "This way, there's no extra work that needs to be done
               when each frame is drawn to the screen."

            show eileen happy at left with move
            show cyan base at cyanpos with dissolve

            e "Let me show you a test image, a simple cyan circle."

            e "We'll be applying some image operations to it, to see
               how they can be used."

            show cyan crop at cyanpos with dissolve
            
            e "The im.Crop operation can take the image, and chop it
               up into a smaller image."

            show cyan composite at cyanpos with dissolve

            e "The im.Composite operation lets us take multiple images,
               and draw them into a single image."

            e "While you can do this by showing multiple images, this
               is more efficent, if more complex."

            show cyan livecomposite at cyanpos with dissolve

            e "There's also LiveComposite, which is less efficent, but
               allows for animation."

            e "It isn't really an image operation, but we don't know
               where else to put it."

            show cyan scale at cyanpos with dissolve

            e "The im.Scale operation lets us change the size of images."

            show cyan green at cyanpos with dissolve

            e "The im.Map operation lets us mess with the red, green,
               blue, and alpha channels of an image."

            e "In this case, we removed all the blue from the image,
               leaving only the green component of cyan."

            show cyan base at cyanpos with dissolve
            show cyan green2 at cyanpos with dissolve 

            e "The im.Recolor operation can do the same thing, but is more
               efficient when we're linearly mapping colors."

            show cyan blackwhite at cyanpos with dissolve

            e "The im.Twocolor operation lets you take a black and white image, like this one..."

            show cyan twocolor at cyanpos with dissolve

            e "... and assign colors to replace black and white."

            show cyan base at cyanpos with dissolve
            show cyan alpha at cyanpos with dissolve

            e "The im.Alpha operation can adjust the alpha channel on
               an image, making things partially transparent."

            show eileen alpha at left with dissolve

            e "It's useful if a character just happens to be ghost."

            with None
            hide cyan
            show eileen happy at left
            with dissolve

            e "But that's not the case with me."

            show eileen happy with move

            show eileen flip with dissolve

            e "Finally, there's im.Flip, which can flip an image horizontally or vertically."

            e "I think the less I say about this, the better."

            show eileen happy with dissolve

            
        "User interaction, updated in 5.5.0":

            e "Ren'Py gives a number of ways of interacting with the
               user."

            e "You've already seen say statements and menus."

            menu:
                
                e "But were you aware that you can have dialogue and
                   menus onscreen at the same time?"

                "Yes.":

                    show eileen vhappy

                    e "Good!"

                    show eileen happy

                "No.":

                    e "Well, now you know."

            e "We can also prompt the user to enter some text."

            $ povname = renpy.input("What is your name?")

            pov "My name is %(povname)s."

            
            e "Imagemaps let the user click on an image to make a
               choice."

            # This is an imagemap. It consists of two images, and a list of
            # hotspots. For each hotspot we give the coordinates of the left,
            # top, right, and bottom sides, and the value to return if it is
            # picked.

            $ result = renpy.imagemap("ground.png", "selected.png", [
                (100, 100, 300, 400, "eileen"),
                (500, 100, 700, 400, "lucy")
                ])

            # We've assigned the chosen result from the imagemap to the
            # result variable. We can use an if statement to vary what
            # happens based on the user's choice.

            if result == "eileen":
                show eileen vhappy
                e "You picked me!"

            elif result == "lucy":
                show eileen concerned
                e "It looks like you picked Lucy."

                # Eileen is being a bit possesive here. :-P
                if date:
                    e "You can forget about Saturday."
                    $ date = False

            show eileen happy

            e "While these constructs are probably enough for most
               visual novels, dating simulations may be more
               complicated."

            e "The ui functions allow you to create quite complicated
               interfaces."
            
            e "For example, try the following scheduling and stats screen,
               which could be used by a stat-based dating simulation."

            $ day_planner()

            e "The ui functions can be used to rewrite many parts of
               the interface."

            e "Hopefully, this gives you enough power to write any
               visual novel you want."

        "Character Objects, updated in 5.6.0.":

            e "The Character object is used to declare characters, and
               it can also be used to customize things about how a
               character speaks."

            e "By supplying it with the appropriate arguments, we can
               really change around the feel of the game."

            e "In this section, we'll demonstrate some of what can be
               accomplished by customizing character objects."

            equote "By supplying what_prefix and what_suffix arguments
                    to a Character object, we can automatically add
                    things before each line of text."

            equote "This is a lot easier than having to put those
                    quotes in by hand."

            equote "We can also use who_prefix and who_suffix to
                    add text to the name of the speaker."

            e "We can also supply arguments to the Character
               object that customize the look of the character
               name, the text that is being said, and the window
               itself."

            eweird "These can really change the look of the game."

            eside "A more practical use of that is in conjunction with
                   show_side_image, which lets us position an image next
                   to the text."

            etwo "There's also show_two_window, which puts the character's
                  name in its own window."
            
            ectc "Finally, we demonstrate a click to continue
                  indicator. In this example, it's nestled in with the
                  text."

            ectc "This also demonstrates the use of the anim.Blink
                  function."

            ectcf "A click to continue image can also be placed at a
                   fixed location on the screen."

            e "That's it for now."

        "Layers and Advanced Show, added in 5.6.0.":

            e "Ren'Py lets you define layers, and show images on
               specific layers."

            hide eileen
            with dissolve

            show bg whitehouse onlayer demo
            with dissolve

            show eileen happy onlayer demo 
            with dissolve

            e "The \"onlayer\" clause of the scene, show, and hide
               statements lets us pick which layers the commands
               affect."

            e "As you can see, layers do not have to take up the
               entire screen. When a layer doesn't, images are
               clipped to the layer."

            scene onlayer demo
            show eileen happy
            with dissolve

            e "The \"as\" clause lets you change the tag of an image."

            show eileen happy as eileen2
            with None

            show eileen happy at left
            show eileen happy at right as eileen2
            with move

            e "This is useful when you want to show two copies of the
               same image."

            e "Or if a character has a twin."

            show eileen happy at center
            show eileen happy at offscreenright as eileen2
            with move

            hide eileen2

            show expression Text("This is text.", size=50, yalign=0.5, xalign=0.5, drop_shadow=(2, 2)) as text
            with dissolve

            e "You can use \"show expression\" to show things that
               aren't just images, like text."

            hide text
            with dissolve

            show eileen happy zorder 2
            show cyan base at Position(xalign=0.6, yalign=0.0) zorder 1
            with dissolve

            e "Finally, the \"zorder\" clause lets you place an image behind
               another."

            hide cyan base
            show eileen happy
            with dissolve

            e "And that's it for layers and advanced show."

            

        "" # Empty, so we have a blank line.

        "That's enough for me.":

            e "Is there anything else you'd like to ask?"

            return

    e "Is there anything else you want demonstrated?"

    jump demo_menu


label define_hyperlink:

    definition "A hyperlink is a button that is defined inside text, using
                text tags. They're ideal for including definitions of words
                used in the script, but they shouldn't be used in place of
                menus."

    return

# Here, are a number of customizations that make the game look
# better. We place them down here at the bottom, to make the first few
# lines of the script look better.
#
# These can be deleted without issue, if you do not want them.

init:
    
    # Change the look of the main menu.
    $ style.mm_root.background = Image("mainmenu.jpg")
    $ style.mm_menu_window.yanchor = 0
    $ style.mm_menu_window.ypos = .05

    # Change the look of the text window.    
    $ style.window.background = Frame("window.png", 16, 16)
    $ style.window.xmargin = 0
    $ style.window.ymargin = 0
    $ style.window.xpadding = 12
    $ style.window.top_padding = 6
    $ style.window.bottom_padding = 12

    # Interface sounds, just for the heck of it.
    $ style.button.activate_sound = 'click.wav'
    $ style.imagemap.activate_sound = 'click.wav'
    $ library.enter_sound = 'click.wav'
    $ library.exit_sound = 'click.wav'
    $ library.sample_sound = "18005551212.ogg"

    # Select the transitions that are used when entering and exiting
    # the game menu.
    $ library.enter_transition = pixellate
    $ library.exit_transition = pixellate
    

# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.

# We'll comment it out for now.
#
# label splashscreen:
#     scene black
#     show text "American Bishoujo Presents..." with dissolve
#     $ renpy.pause(1.0)
#     hide text with dissolve
#
#     return

init:
    python:
        def fadeup(mul):

            def inner(st, at):
                i = int(st * mul)
                if i > 255:
                    i = 255
                    
                return Solid((i, i, i, 255)), .1

            return DynamicDisplayable(inner)
    
label splashscreen:


    
    show expression DynamicDisplayable("'#f00'") as bg

    "Foo."

    scene black
    
    show expression fadeup(80) as bg

    "Bar."
    
    