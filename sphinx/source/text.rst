.. _text:

====
Text
====

Ren'Py contains several ways of displaying text. The :ref:`say <say-statement>`
and :ref:`menu <menu-statement>` are primarily concerned with the
display of text to the user. The user interface often contains text,
displayed using the :ref:`text <sl-text>`, :ref:`textbutton <sl-textbutton>`, 
and :ref:`label <sl-label>` screen language statements. These
functions, along with others, create :func:`Text` displayables, and
show them on the screen.

The Text displayable is responsible for managing the process of
showing the text to the user. The text displayable performs actions in
the following order:


1. Translating text.
2. Interpolating data into the text.
3. Styling the text using styles and text tags.
4. Laying out the styled text.
5. Drawing the text to the screen.

This chapter discusses the process of text display in Ren'Py.


Escape Characters
=================

There are three special characters that can control the way Ren'Py
displays text. A creator needs to be aware of these characters to
ensure that their writing is not accidentally misinterpreted by the engine. 

\ (backslash)
    The backslash character is used to introduce when writing a Ren'Py
    or Python string. Some common escape codes are:

    \\" (backslash-doublequote)
        Includes a doublequote in a double-quoted string.

    \\' (backslash-quote)
        Includes a single quote in a single-quoted string.
    
    \\\  (backslash-space)
        Includes an additional space in a Ren'Py string. By default,
        Ren'Py script text collapses adjacent whitespace into a single
        space character.

    \\n (backslash-n)
        Includes a newline character in the text.

    \\\\ (backslash-backslash)
        Includes a backslash character in the text.

[ (left bracket)
    The left bracket is used to introduce interpolation of a value
    into the text. To include a single left bracket in your text,
    double it - write ``[[``.

{ (left brace)
    The left brace is used to introduce a text tag. To include a left
    brace in your text, double it - write ``{{``.

    
Interpolating Data
==================

Ren'Py supports interpolating data into the text string before it is
displayed. For example, if the player's name is stored in the
``playername`` variable, one could write a line of dialogue like::

    g "Welcome to the Nekomimi Institute, [playername]!"

Ren'Py will interpolate variables found in the global store. When
using a text widget in a screen, Ren'Py will also interpolate screen
local variables. (This can be overridden by supplying an explicit
scope argument to the Text displayable.)

Ren'Py isn't limited to interpolating simple variables. It can also
interpolate fields and components of tuples. So it's possible to have
code like::

    g "My first name is [player.names[0]]."

It's possible to apply formatting codes when displaying numbers. This
code will display a floating point number to two decimal places::

    $ percent = 100.0 * points / max_points
    g "I like you [percent:.2] percent!"

Ren'Py's string interpolation is taken from the :pep:`3101` string
formatting syntax. Ren'Py uses [ to introduce string formatting
because { was taken by text tags.

Along with the !s and !r conversion flags supported by Python, Ren'Py
supports a !q conversion flag. The !q conversion flag ensures that
text tags are properly quoted, so that displaying a string will not
introduce unwanted formatting constructs. For example::

    g "Don't pull a fast one on me, [playername!q]."


Styling and Text Tags
=====================

In Ren'Py, text gains style information in two ways. The first is from
the style that is applied to the entire block of text. Please see the
section about the :ref:`style system <styles>` for more details,
especially the section on :ref:`text style properties <text-style-properties>`.  

The second way is through text tags. Text tags are suitable for
styling a portion of text block, or a small fraction of the text
blocks in the program. If you find yourself applying the same text
tags to every line of text, consider using a style instead.

There are two text tags. Some text tags are self-closing, while others
require a closing tag. When multiple closing tags are used, they
should be closed last open, first closed order - Ren'Py will reject
incorrect nesting. For example::

    # This line is correct.
    "Plain {b}Bold {i}Bold-Italic{/i} Bold{/b} Plain"

    # This line is incorrect, and will cause an error or incorrect
    # behavior.
    "Plain {b}Bold {i}Bold-Italic{/b} Italic{/i} Plain"

Some text tags take an argument. In that case, the tag name is
followed by an equals sign (=), and the argument. The argument may
not contain the right-brace (}) character. The meaning of the
argument varies based on the text tag.

General Text Tags
-----------------

Tags that apply to all text are:

.. text-tag:: a

    The anchor tag creates a hyperlink between itself and its closing
    tag. While the behavior of the hyperlink is controlled by the
    :propref:`hyperlink_functions` style property, the default handler
    has the following behavior.

    * Hyperlinks are rendered using the ``style.hyperlink_text`` style. 

    * If the argument begins with the text ``"http://"``, clicking on
      it opens the url in a web browser. Otherwise, the argument is
      interpreted as a label, which is called in a new context. This
      allows hyperlinks to be used to define terms.

    * Apart from the change in style, there is no specific behavior
      when a hyperlink is hovered.

    ::

        label test:
    
            e "Why don't you visit {a=http://renpy.org}Ren'Py's home page{/a}?"

            e "The {a=define_trebuchet}trebuchet{/a} is at the gates."

            return
            
        label define_trebuchet:

            e "A trebuchet is a kind of siege engine."
            e "It uses a lever to fling things at targets."
            e "Like us!"
            
            return


.. text-tag:: b

    The bold tag renders the text between itself and its closing tag
    in a bold font. ::

        "An example of {b}bold test{/b}."

.. text-tag:: color

    The color text tag renders the text between itself and its closing
    tag in the specified color. The color should be in #rgb, #rgba,
    #rrggbb, or #rrggbbaa format. ::

        "{color=#f00}Red{/color}, {color=#00ff00}Green{color}, {color=#0000ffff}Blue{/color}"

.. text-tag:: cps

    The characters per second tag sets the speed of text display, for
    text between the tag and its closing tag. If the argument begins
    with an asterisk, it's taken as a multiplier to the current text
    speed. Otherwise, the argument gives the speed to show the text
    at, in characters per second. ::

        "{cps=20}Fixed Speed{/cps} {cps=*2}Double Speed{/cps}
        
.. text-tag:: font

    The font tag renders the text between itself and its closing tag
    in the specified font. The argument is the filename of the font to
    use. ::

        "Try out the {font=mikachan.ttf}mikachan font{/font}."

.. text-tag:: i

   The italics tag renders the text between itself and its closing tag
   in italics. ::

       "Visit the {i}leaning tower of Pisa{/i}."

.. text-tag:: k

   The kerning tag is a tag that adjust the kerning of characters
   between itself and its closing tag. It takes as an argument a
   floating point number giving the number of pixels of kerning to add
   to each kerning pair. (The number may be negative to decrease
   kerning.) ::

       "{k=-.5}Negative{/k} Normal {k=.5}Positive{/k}"
       
.. text-tag:: image

   The image tag is a self-closing tag that inserts an image into the
   text. The image should be the height of a single line of text. The
   argument should be either the image filename, or the name of an
   image defined with the image statement. ::

       g "Good to see you! {image=heart.png}"

.. text-tag:: s

   The strikethrough tag draws a line through text between itself and
   its closing tag. ::

       g "It's good {s}to see you{/s}."

.. text-tag:: rb

   The ruby bottom tag marks text between itself and its closing tag
   as ruby bottom text. See the section on :ref:`Ruby Text <ruby-text>` 
   for more information.

.. text-tag:: rt

   The ruby top tag marks text between itself and its closing tag as
   ruby top text. See the section on :ref:`Ruby Text <ruby-text>` for
   more information.
   
.. text-tag:: size

   The size tag changes the size of text between itself and its
   closing tag. The argument should be an integer, optionally preceded
   by + or -. If the argument is just an integer, the size is set to
   that many pixels high. Otherwise, the size is increased or
   decreased by that amount. ::

       "{size=+10}Bigger{/size} {size=-10}Smaller{/size} {size=24}24 px{/size}."

.. text-tag:: space

   The space tag is a self-closing tag that inserts horizontal space
   into a line of text. As an argument, it takes an integer giving the
   number of pixels of space to add. ::

       "Before the space.{space=30}After the space."
       
.. text-tag:: u

   The underline tag underlines the text between itself and its
   closing tag. ::

      g "It's good to {u}see{/u} you."

.. text-tag:: vspace

   The vspace tag is a self-closing tag that inserts vertical space
   between lines of text. As an argument, it takes an integer giving
   the number of pixels of space to add. ::

      "Line 1{vspace=30}Line 2"
       
        
Dialogue Text Tags
------------------

Text tags that only apply to dialogue are:

.. text-tag:: fast

    If the fast tag is displayed in a line of text, then all text
    before it is displayed instantly, even in slow text mode. The
    fast tag is a self-closing tag. ::

        g "Looks like they're{nw}"
        show trebuchet
        g "Looks like they're{fast} playing with their trebuchet again."

.. text-tag:: nw

    The no-wait tag is a self-closing tag that causes the current line
    of dialogue to automatically dismiss itself once the end of line
    has been displayed. ::

        g "Looks like they're{nw}"
        show trebuchet
        g "Looks like they're{fast} playing with their trebuchet again."

.. text-tag:: p

    The paragraph pause tag is a self-closing tag that terminates the
    current paragraph, and waits for the user to click to continue. If
    it is given an argument, the argument is interpreted as a number,
    and the wait automatically ends after that many seconds have
    passed. ::
        
        "Line 1{p}Line 2{p=1.0}Line 3"

.. text-tag:: w

    The wait tag is a self-closing tag that waits for the user to
    click to continue. If it is given an argument, the argument is
    interpreted as a number, and the wait automatically ends after
    that many seconds have passed. ::

        "Line 1{w} Line 1{w=1.0} Line 1"


User-Defined Text Tags
----------------------

Ren'Py also supports user-defined text tags. A user-defined text tag
is a text tag where the tag name is empty. In this case, the argument
is taken to be the name of a style. The text between this tag and the
closing tag has the following properties set to those defined in the
style:

* antialias
* font
* size
* bold
* italic
* underline
* strikethrough
* color
* black_color
* kerning


Non-English Languages
=====================

The default font for Ren'Py contains characters for English and many
other languages. For size reasons, it doesn't contain the characters
required to render other languages, including Chinese, Japanese, and
Korean. In order to support these language, a project must first
change the default font, using code like::

    init python:
        style.default.font = "mikachan.ttf"

Ren'Py should then support most world languages without further
configuration. However, Korean can be written with or without spacing
between words. Ren'Py has a special mode to support Korean with
spaces, which can be enabled with the code::

    init python:
         style.default.language = "korean-with-spaces"

Finally, ideographic languages provide a large number of opportunities
for line breaking. To enable a faster line-breaking algorithm, use the
code::

    init python:
         style.default.layout = "greedy"

The faster line-breaking algorithm is not be necessary unless the
game is displaying huge amounts of text, such as in NVL-mode.


.. _ruby-text:

Ruby Text
=========

Ruby text (also known as furigana or interlinear annotations) is a way
of placing small text above a character or word. There are several
steps required for your game to support Ruby text.

First, you must set up styles for the ruby text. The following style
changes are required:

1. The :propref:`line_leading` property must be used to leave enough
   vertical space for the ruby text.
2. A new named style must be created. The properties of this style,
   such as :propref:`size` should be set in a fashion appropriate
   for ruby text.
3. The yoffset of the new style should be set, in order to move the
   ruby text above the baseline.   
4. The :propref:`ruby_style` field of the text's style should be set
   to the newly-created style.

For example::

    init python:
        style.default.line_leading = 12

        style.ruby_style = Style(style.default)
        style.ruby_style.size = 12
        style.ruby_style.yoffset = -20
                        
        style.default.ruby_style = style.ruby_style

Once Ren'Py has been configured, ruby text can be included using the
rt and rb text tags. The rt tag is used to mark one or more characters
to be displayed as ruby text. If the ruby text is preceded by text
enclosed in the rb tag, the ruby text is centered over that
text. Otherwise, it is centered over the preceding character.

For example::

    e "Ruby can be used for furigana (東{rt}とう{/rt} 京{rt}きょう{/rt})."

    e "It's also used for translations ({rb}東京{/rb}{rt}Tokyo{/rt})."

It's the creator's responsibility to ensure that ruby text does not
leave the boundaries of the text. It may be necessary to add leading
or spaces to the left and right of the text to prevent these errors
from occurring.

Fonts
=====

Ren'Py supports Truetype and Image-Based fonts.

A Truetype font is specified by giving the name of the font file. The
file must be present in the game directory, or one of the archive
files.

Ren'Py also supports Truetype collections that define more than one
font. When accessing a collection, use the 0-based font index,
followed by an at-sign and the file name. For example, "0@font.ttc" is
the first font in a collection, "1@font.ttc" the second, and so on.


Font Replacement
----------------

The :var:`config.font_replacement_map` variable is used to map
fonts. The combination of font filename, boldness, and italics is
mapped to a similar combination. This allows a font with proper
italics to be used instead of the automatically-generated italics.

Once such mapping would be to replace the italic version of the Deja
Vu Sans font with the official oblique version. (You'll need to
download the oblique font from the web.) ::

    init python:
        config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False) 

This mapping can improve the look of italic text.

Image-Based Fonts
-----------------

Image based fonts can be registered by calling one of the following
registration functions. Registering an image-based font requires the
specification of a name, size, boldness, italicness, and
underline. When all of these properties match the registered font,
the registered font is used.

.. include:: inc/image_fonts

As BMFont is the most complete of the three image font formats Ren'Py
supports, it's the one recommended for new projects. An example of
BMFont use is::

    init python:
        renpy.register_bmfont("bmfont", 22, filename="bmfont.fnt")

    define ebf = Character('Eileen', what_font="bmfont", what_size=22)

    label demo_bmfont:
                           
        ebf "Finally, Ren'Py supports BMFonts."


Font Groups
-----------

When creating a multilingual game, it may not be possible to find a single
font that covers every writing system the game use while projecting the
the mood the creator intends. To support this, Ren'Py supports font groups
that can take characters from two or more fonts and combine them into a 
single font. 

To create a font group, create a FontGroup object and call the .add method 
on it once or more. a FontGroup can be used wherever a font name can be 
used. The add method takes the start and end of a range of unicode character
points, and the first range to cover a point is used.

For example::

    init python:
         style.default.font = FontGroup().add("english.ttf", 0x0020, 0x007f).add("japanese.ttf", 0x0000, 0xffff)
        
.. include:: inc/font_group


Text Displayable
================

Text can also be used as a :ref:`displayable <displayables>`, which
allows you to apply transforms to text, displaying it as if it was an
image and moving it around the screen.

.. include:: inc/text

Slow Text Concerns
==================

Ren'Py allows the creator or user to indicate that text should be
displayed slowly. In this case, Ren'Py will render the text to a
texture, and then draw rectangles from the texture to the screen.

Unfortunately, this means that it's possible to get rendering
artifacts when characters overlap. To minimize these rendering
artifacts, ensure that the :propref:`line_leading` and
:propref:`line_spacing` properties are large enough that lines do not
overlap. If the bottoms of characters on the first line are clipped,
espeically if line_spacing is negative, consider increasing
:propref:`line_overlap_split`.

Horizontal artifacts are also possible when characters are kerned
together, but these artifacts are less severe, as they exist for only
a single frame.

Artifacts aren't a problem for static text, like the text in menus and
other parts of the user interface.

Translations
============

Ren'Py supports the automatic translation of text. The translation
occurs whenever text is displayed, and before text interpolation
occurs.

Ren'Py reads translations out of .rpt files. A .rpt file is a text
file containing lines beginning with the following characters:

#
    Lines beginning with the hash mark are comment lines, that are
    ignored.

<
    Lines beginning with a less-than followed by a space are
    translation source lines, giving strings to be translated.

>
    Lines beginning with a greater-than followed by a space are
    translation lines, giving the translation of the previous
    translation source.

Inside a translation line, newlines are escaped with \\n, and
backslashes are escaped with \\\\.

By default, Ren'Py reads translations out of a file called
translations.rpt, if it exists. The :func:`Language` action can be
used to change the translation file.

Creating Translation Files
==========================

Ren'Py has support for automatically creating translation
files. Taking advantage of this is a three-step process.

1. Create an empty translation file, such as translations.rpt, in the
   game directory.

2. Set the RENPY_UPDATE_TRANSLATIONS environment variable to a
   non-empty string.

3. Play through the game until all text is seen.

Ren'Py will add an entry to the translations file for each unit of
text shown. This text can then be translated.


Text Overflow Logging
---------------------

Ren'Py can log cases where text expands outside of the area allocated
for it. To enable text overflow logging, the following steps are
necessary.

1. Set the :var:`config.debug_text_overflow` variable to true.
2. Set the :propref:`xmaximum` and :propref:`ymaximum` style properties on either the Text
   displayable, or a container enclosing it.
3. Run the game.

Whenever text is displayed that overflows the available area, Ren'Py
will log an error to the ``text_overflow.txt`` file.
