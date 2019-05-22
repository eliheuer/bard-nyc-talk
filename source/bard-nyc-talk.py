# Render this document with DrawBot3: http://www.drawbot.com/

# Import modules:
from drawBot import *
import math

# Basic variables  (width, height, margin, etc...):
W, H, M = 1920, 1080, 128
headlineXPos = M+10
headlineYPos = -M-46
headlineLineHeight = 80
headlineFontSize = 72
print("Headline X position:", headlineXPos)

def grid(W, H, M):  # (width, height, margin)
    fill(None)
    gridWidth = W-(M*2)
    gridHeight = (H-(M*2))-40
    print("grid width =", gridWidth, "px")
    print("grid Height =", gridHeight, "px")
    # Draw grid Y
    stpY = 0
    stroke(0.4)
    gridUnitY = 40
    for y in range(20):
        polygon((M, (M+20)+stpY), (W-M, (M+20)+stpY))
        stpY += gridUnitY
    # Draw grid X
    stpXY = 0
    stroke(0.4)  # Set grid line color RED
    for xx in range(4):
        stpX = 0  # Step in sequence on x axis
        for x in range(8):
            rect(M+stpX, (M+20)+stpXY, 40*4, 40*4)
            stpX += 211  # Set position for next gridline
        stpXY += 200
    # Draw margin
    stroke(1,0,0)
    fill(None)
    rect(M, M+20, gridWidth, gridHeight)


# Title Page ###################################################################
newPage(W, H)
fill(1)
stroke(None)
font("source/fonts/Epistle-Regular.ttf")  # Set the font
# Image (metafont screenshot)
# Text Headline
headlineTxt = FormattedString()
headlineTxt.append("Eli Heuer's Slides",\
    font="source/fonts/Epistle-Regular.ttf",\
    fontSize=headlineFontSize ,\
    fill=(0),\
    lineHeight=headlineLineHeight)
# Text Subhead
headlineSub = FormattedString()
headlineSub.append("Bard, 2019 ",\
#    font="source/fonts/as.ttf",\
    fontSize=headlineFontSize/2 ,\
    fill=(0),\
    lineHeight=headlineLineHeight/2)
# Draw headline text
textBox(headlineTxt, (headlineXPos, headlineYPos,\
    W/2, H), align="left")
# Draw subhead text
textBox(headlineSub, (headlineXPos, headlineYPos-710,\
    W/2, H), align="left")
# Uncomment next line to turn on the grid for this page:
image("source/images/intro.jpg", (-50, -250), alpha=1)
#grid(W, H, 140)


###############################################################################
newPage(W, H)
image("source/images/desk.jpg", (-50, 0), alpha=1)

###############################################################################
newPage(W, H)
image("source/images/ideas.jpg", (-50, -300), alpha=1)

###############################################################################
#newPage(W, H)
#image("source/images/map.jpg", (-50, -200), alpha=1)

###############################################################################
newPage(W, H)
image("source/images/rob.jpg", (-50, -300), alpha=1)


###############################################################################
newPage(W, H)
image("source/images/clock.jpg", (-50, -400), alpha=1)

# baha ####################################################
newPage(W, H)
image("source/images/multitask-bag.jpg", (0, -800), alpha=1)


# turtle ###########################################################
#newPage(W, H)
#fill(0)
#rect(0, 0, W, H)
#image("source/images/tf-01.png", (200, 100), alpha=1)
#grid(W, H, 140)

# jacobin 1 ###################################################################
newPage(W, H)
image("source/images/jacobin-mag.jpg", (0, -300), alpha=1)
#grid(W, H, 140)

# jacobin 1 ###################################################################
newPage(W, H)
image("source/images/plantin.jpg", (0, -250), alpha=1)
#grid(W, H, 140)


# jacobin 1 ###################################################################
newPage(W, H)
image("source/images/unix.jpg", (0, -200), alpha=1)


# jacobin 1 ###################################################################
newPage(W, H)
image("source/images/gnu.jpg", (0, -200), alpha=1)


# baha ####################################################
#newPage(W, H)
#fill(0)
#rect(0, 0, W, H)
#image("source/images/emacs-02.png", (270, 150), alpha=1)

# baha ####################################################
newPage(W, H)
fill(0)
rect(0, 0, W, H)
image("source/images/TruFont.png", (270, 150), alpha=1)



################################################################################
saveImage("~/Drawbot/bard-nyc-talk/elis-slides.pdf")
