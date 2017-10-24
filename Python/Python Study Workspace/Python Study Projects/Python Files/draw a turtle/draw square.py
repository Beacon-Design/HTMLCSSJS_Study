#!/usr/bin/env python3
#coding:utf-8

import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    for i in range(1, 5):
        draw_square(brad)
        brad.right(10)


    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
