# QAutoScrollLabel

This is a Widget that I made on my own to start practicing my knowledge of pythhon and PyQt, it will show in the code itself and in the documentation and notes that I am newbie 
on this.

## Widget preview
This is a preview of the Widget with its default Text, The text in this widget moves automatically if the text is larger than the Widget itself.

![QAutoScrollLabel Preview](https://i.imgur.com/wAIoFRb.gif)

## Package requirements
This packege requieres a compatible verison of PyQt 6.1.1

`pip install PyQt6~=6.1.1` 

and a compatible version of multipledispatch 0.6.0

`pip install multipledispatch~=0.6.0`

## Download
You can get the package whit the command `pip install QAutoScrollLabel`

## How to use

### Widget initialization

To initialize the Widget you will need to instantiate the QAutoScrollLabel class, which has two optional arguments which are parent of type QWidget and debug of type Boolean; 
after this the `show()` function must be called.

### Debug

The function debug must be used to set or change the debug status, it acepts an optional boolean parameter.

- **If True:** The widget will start printing the following data every tick: `debug(True)`

  - **Orientation:** The ocurrent orientacion of the scrolling.
  - **Pos:** ScrollBar current position in Pixels.
  - **Max:** The maximum scroll value in Pixels.
  - **Vel:** The amount of pixels to scroll every tick.
  - **Time between ticks:** The time in seconds between one tick and the next one.
  - **Ticks Per Second:** The number of ticks each second.
  
- **If False** `debug(False)` The widget will stop printing debug info. 
- **If None or no parametr given** `debug(None)` **or** `debug()` The debug status will be inverted (False -> True **or** True -> False)

### Set Debug
The function `setDebug()` will let you set a custom calleable object to use as widget debug, this function requieres a calleable object in the parameter debug_fun, please use 
this function before the function `show()`

### Debug Status
The `debugStatus` property returns a boolean value depending on the current state of debbuging.

### Set Velocity
The `setTimeBetweenTicks()` function will allow you to configure the pixels that the scroll bar will scroll each Tick, this function **requires a parameter of type Int**

### Set Time Beteen Ticks
The `setVelocity()` function will allow you to configure the time between each Tick, this function **requires a parameter of type Float or Int**

### Velocity
The `velocity` property returns  the pixels that the scroll bar will scroll each Tick.

### Orientation
The `orientation` property returns  the Current orientation of the text.

### Time Beteen Ticks
The `timeBetweenTicks` property returns  the time between each Tick.

### Set Text **- Inherited from ScrollLable(QScrollArea)**
The funtion `setText()` set a new text in the Widget, this function **requires a parameter of type Str**.

### Text **- Inherited from ScrollLable(QScrollArea)**
The function `text()` retuns the current text in the Widget
