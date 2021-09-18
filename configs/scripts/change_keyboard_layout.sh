#!/bin/sh
if setxkbmap -query | grep -q lang1,lang2 ; then 
    setxkbmap -model acer_laptop -layout lang3,lang4 -variant , ;
else 
    setxkbmap -model acer_laptop -layout lang1,lang2 -variant , ;
fi
