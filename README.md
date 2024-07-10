# Factory Project

## Goal
The goal of this assignment will be to create a text-based RPG "program" (I
won't call it a game, because I don't expect you to full code out a functioning
game within the week, but some kind of text interactions).  
Requisites:
- The "program" will print out via stdout, and receive text input via stdin.
You can choose any way to implement input that you like, there are several 
packages that will handle this for you, I recommend: `prompt_toolkit`, but 
`readline` works fine.
- You will utilize the Factory Pattern to create new objects,

The Program:
- A basic Dungeon-crawler, where the player enters a dungeon in search of 
treasure.
- The dungeon can be as simple as you like, with as many rooms as you like.
But one room must contain some treasure.
- There must be an assortment of weapons to choose from in the starting room.
- There must be at least 1 enemy to defeat.


### Getting Started

I have provided a basic scaffold within this repository, feel free to clone it 
into your own repository.

`git clone git@github.com:JoshUptons/basics.git`  
`cd basics`  
`git remote remove origin`
`git remote add origin <your repo here>`
`git push origin main --set-upstream`
`cd assignments/design-patterns/factory`

Within the `src` directory I have added the basic building blocks for a `Player`
and `Dungeon`.
