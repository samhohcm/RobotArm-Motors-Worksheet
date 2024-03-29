---
layout: page
title: Motors for Robots - How to move your robot!
---

<!--Comment: Above here is the header, we need this to generate the web page-->

<!--Comment: This section is markdown inside a bootstrap container-->

[![logoPicture](images/girlsIntoCodingLogo.jpg)](https://www.girlsintocoding.com/)

A project activity for [Girls Into Coding](https://www.girlsintocoding.com/).


This session is designed to be fun! The idea is that we can follow it together online, but that we can be free to move at our own pace. We're going to be doing some basic python programming in this activity. If you're not too familiar with Python, don't worry, you'll be able to follow along :) ! 


<!--Comment: End of markdown section-->

<!--Comment: This code here is html-->

<!--Comment: This is html paragraph spacing <br>-->
<br>
<br>

<!--Comment: This is html bootstrap-->
<div class="container p-3 my-3 bg-primary">
<h2>Contents</h2>
<ul class="list-group">
  <li class="list-group-item"><a href="#resourcesPanel">Resources</a></li>
  <li class="list-group-item"><a href="#Explanation">How a Motor works</a></li>
  <li class="list-group-item"><a href="#Activity1">Assembling the servomotor</a></li>
  <li class="list-group-item"><a href="#Activity2">Programming on the MicroBit</a></li>
  <li class="list-group-item"><a href="#Activity3">Programming the servomotor</a></li>
  <li class="list-group-item"><a href="#Activity4">Assembling the stepper motor</a></li>
  <li class="list-group-item"><a href="#Activity5">Programming the stepper motor</a></li>
  <li class="list-group-item"><a href="#Activity6">How hard did I blow?</a></li>
</ul>
</div>

<div id="resourcesPanel" class="container p-3 my-3 bg-info">
<h2>Resources</h2> 
  <p>Here's some resources that may help with the activity</p>
<ul class="list-group">
  <a href="https://www.w3schools.com/python/" target="_blank" class="list-group-item list-group-item-action">Python tutorials at W3 Schools</a>
  <a href="https://www.pythoncheatsheet.org/" target="_blank" class="list-group-item list-group-item-action">Python cheatsheet</a>
  <a href="https://robohub.org/30-women-in-robotics-you-need-to-know-about-2020/" target="_blank" class="list-group-item list-group-item-action">30 women in robotics you need to know about – 2020</a>
</ul>
</div>

<!--Comment: This is the end of html bootstrap-->


<!--Comment: Paragrpah spacing-->
<br>
<br>


# How do you move a robot arm?
<div id="Explanation">
</div>
<br>


Say you'd like to build a robot. And of course, robots have to move, otherwise they can't do much! 

What can you use to move your robot?
Do you have any ideas?
Think about things that move, what makes them move?

<br>

<img src="images/Explanation/Things_that_move.png" alt="Things that move" height="300" class="center">

*Cartoons Copyright of [Irasutoya](https://www.irasutoya.com)*

<br>

**Motors** are an easy way to get moving! They can be quite affordable and electrical motors can be powered by batteries, which are a convenient power source. In fact, I've just packed some for you in the box!

Have a look at the box, and pull out the bags labelled "Motors Workshop" and "Stepper Motor". There's a blue coloured servomotor in the Motors Workshop bag, and a stepper motor in the Stepper Motor bag!

They look like this:

<br>
<!--Insert photo-->
<p style="text-align: center;"><img src="images/Explanation/Both_motors.jpg" alt="Both motors"></p>
<br>

These are two different types of motors, and we're going to learn all about them today.
<br>
<br>

## How do you make battery power turn into movement?
<br>

Using magnets!

What do you remember about magnets and how they behave? Let's pause a moment to have a think about it.

<br>

Have an idea? Cool. Let's crack on!

Have you tried making an **electromagnet** using a coil of wire and a battery? Here's a helpful link if you want to try it at home!

[How to make an electromagnet](https://sciencebob.com/make-an-electromagnet/)

If you run an electrical current through a wire (for example, with a battery!), it will generate an **electromagnetic field** around the wire. Making lots of coils magnifies this effect, so we usually make electromagnets using coils. These are magnets that you can turn on and off, or even switch polarities! This is compared to permanent magnets, which you might have seen around.

<br>
<p style="text-align: center;"><img src="images/Explanation/magnet-set_1308-15311.jpg" alt="Magnets" height="300px" class="center"></p>

*Image Copyright [brgfx](https://www.freepik.com/free-vector/magnet-set_2480989.htm)*

<p style="text-align: center;">Permanent magnets look like these!</p>
<br>


Inside every motor there is a permanent magnet and there is an electromagnet. 

What happens when you point the North end of a magnet to the South end of a magnet?

They try to get closer to each other of course! And if you point the North end of a magnet to the North end of another magnet, they will try to get away from each other. Their electromagnetic fields interact with each other, generating a force. This force is what we use to make the motor turn! We can observe this phenomenon in the animation in this link: [DC Motor animation](https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor)

Open it and let the applet load. It should look like this:

<p style="text-align: center;"><img src="images/Explanation/DC_Motor_animation.jpg" alt="DC Motor Explanation screenshot"
	title="DC Motor Demonstration" height="350"></p>

Have a play with the speed and pay attention to the little green arrows. They show the direction in which the electromagnetic force pushes the coil. In this animation, the outer magnet is the permanent magnet, and the coil in the middle connected to the battery is the electromagnet. The part that moves is connected to the **shaft** of the motor, which you can attach things to that need to be moved. All electric motors use this principle.

Now let's take a look at the motors we have right now and learn more about them!

<br>
<br>


# Let's play with some motors!
---

## The Servomotor
<br>

The servomotor you have with you is a very common hobby servomotor, sometimes shortened to 'servo'. It has a permanent magnet and an electromagnet inside arranged like the animation we looked at before, and a gearbox. The gearbox helps to increase the torque (the turning force) of the motor, while slowing down its speed. It also has a sensor that can measure its rotation!

Being able to measure how much it has rotated helps it to decide how much to continue moving, which is nice because it means you don't have to add extra things to control the motor and make it go to the position you want. This can be useful for robotic applications. It is also very light and compact.

Take it out of the bag and let's have a look at the motor.
<br>

<!-- image of servomotor parts-->
<img src="images/AssemblyServo/Servomotor_Parts.png" alt="Servomotor Parts" class="center"/> 

<br>
You can see the shaft of the motor on the outside, and through the plastic body you can see the plastic gears inside. At the bottom of the motor, you can see a controller board and there are three wires coming out of the body of the motor.

The <span style="color:Brown">brown wire</span> is connected to the ground of the power supply, the <span style="color:Red">red wire</span> is connected to the positive end of the power supply, and the <span style="color:DarkOrange">yellow wire</span> will be used to give the control signal to the servomotor. The control signal is what we will give to the motor controller board to tell it what position we want the servomotor to go to.

For servomotors, the control signal is just how long you turn on the current in one second. This is called *Pulse Width Modulation*. The signal would look like this:

<br>
<p style="text-align: center;"><img src="images/Explanation/servo-rotation.gif" alt="PWM-Angularposition" class="center"></p>

*Image copyright [Apoorve](https://circuitdigest.com/article/servo-motor-working-and-basics#:~:text=Servo%20motor%20works%20on%20PWM,(potentiometer)%20and%20some%20gears.)*
<br>

The servomotor we have can go from 0 degrees to 180 degrees. You can get servomotors that can move in bigger angles, or even continuously, like normal motors! For our motor, if the current is turned on for a shorter amount of time, the angular position will be smaller. To get a larger angular position, the current should be turned on for a longer amount of time.

You can easily get motor driver boards to control a servomotor, or control them using a microcontroller board like an Arduino or a microbit. All you need is to be able to provide electrical power to the electromagnetic coil, and a control signal. Today we will be using the microbit and a robotics board!

<br>
<br>

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="Activity1" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #1</h2>
</div>

<br>

<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

### Assembling the servomotor demonstrator

First, we need to assemble our set up. Expand the headings below (click on them) to see each step of the instructions.

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOne">
        Check contents of box
      </a>
    </div>
    <div id="collapseOne" class="collapse show" data-parent="#accordion">
      <div class="card-body">
      Have a look inside your box, you should find lots of stuff in there! The box contains: 
        <br>
        - 1 microbit <br>
        - 1 Kitronik robotics board <br>
        - 2 Stepper motors <br>
        - 1 Bag labelled 'Motors Workshop' <br>
        - 1 Bag labelled 'Assembly parts' <br>
        - 2 3D printed robot arm links (labelled 1 and 2) <br>
        - 1 base board (white in color in 4 pieces) <br>
        - 1 x AA 4 battery holder (connected to the Kitronik Robotics board)<br>
        - 1 whiteboard marker <br>
        - 1 screwdriver (looks like a pen) <br>
        - 2 jumper leads (4 wires each) <br>
        - 1 dial <br>
        - 1 usb cable <br><br>


      <br>  
      <img src="./images/AssemblyServo/Updated_box_contents.png" class="img-fluid" alt="Box Contents" loading="lazy">

      <br>

      <img src="./images/AssemblyServo/img1_compressed.jpg" class="img-fluid" alt="Box" loading="lazy">
      <br>
      <br>
      For this activity, you only need: <br>
        - the 'Motors Workshop' bag <br>
        - the 'Stepper Motor' bag <br>
        - the bag labelled 'Assembly Parts' <br>
        - the part of the base board with the green attachment on it <br>
        - the 4 AA battery holder and Kitronik Robotics Board <br>
        - the microbit <br>
        - the USB cable <br>
        - the screwdriver <br>
        - 1 jumper lead <br>
        - the dial <br>
        - and Robot Arm 2. 

      <br>
  

      <img src="./images/AssemblyServo/Motors_Workshop_parts.png" class="img-fluid" alt="Motors Workshop Parts" loading="lazy">
      <br>
      <p>Carefully keep the other pieces back in the box for the next workshop.</p>


      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwo">
        Assemble the servomotor
      </a>
    </div>
    <div id="collapseTwo" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Slot the servomotor into the robot arm base on the base board as shown in the photo. It is a snap joint, so all you need to do is put one end of the motor attachment tab into one slot on the motor base, and then gently press in the other end of the motor attachment into the other slot on the motor base until it 'snaps' in.</p>

        <img src="images/AssemblyServo/Slot_in_servo.png" class="img-fluid" alt="Slot In Servo" loading="lazy">

        <p>Make sure that the shaft of the servomotor is in the middle of the two ends, and is facing up towards the ceiling.</p>

        <img src="images/AssemblyServo/Centred_servo.jpg" class="img-fluid" alt="Servo Shaft in centre" loading="lazy">
        <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThree">
        Connect the motor
      </a>
    </div>
    <div id="collapseThree" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Let's take a look at the Kitronik Robotics Board. Check if you have a 'All-In-One' board or a 'Compact' board, it is labelled at the back of the board as shown in the photos:
        <br>
        <img src="images/AssemblyServo/Identifying_Board.png" class="img-fluid" alt="Identifying_Board">
        <br>
        <p>
        Depending on your board, the servo pins might look different. If you look at the area circled in the photo below, you will see a set of pins. </p>
        <br>

        <img src="images/AssemblyServo/Board_Servopins.png" class="img-fluid" alt="Board Servopins"/>

        <br>

        <p>
        Take the connector of the servomotor and attach it to the first 3 pins (SV1), so that the brown wire goes to GND, the red wire goes to V (or VDD), and the yellow wire goes to SIG. Just press them on straight downwards until the end. Double check your wiring with the photo!</p>

        <img src="images/AssemblyServo/Connect_ServoPins.png" class="img-fluid" alt="Connector to Servopins">

      </div>
    </div>
  </div>
  
  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFour">
        Install microbit into the Robotics Board
      </a>
    </div>
    <div id="collapseFour" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Take the microbit and install it into the Robotics Board. You will need to push down on it fimly to install it into the connector. Make sure it is the right way around. The 'GND' marked on the microbit should be on the same side as the 'GND' on the robotics board. 
        <br>
        <img src="images/AssemblyServo/img21_compressed.jpg" class="img-fluid" alt="Aligning Microbit and Robotics Board">
        <br>
        <img src="images/AssemblyServo/img22_compressed.jpg" class="img-fluid" alt="Microbit in Robotics Board">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFive">
        Our screwdriver
      </a>
    </div>
    <div id="collapseFive" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Let's take a look at the screwdriver. Take the caps off both ends, you should find different sizes of screwdriver tip. If you give each end a pull you will see that you have four possible sizes of tip. Make sure to select the correct size in this activity. You'll know you've got the right size if it fits snugly into the screw!</p>

        <img src="images/AssemblyServo/img10_compressed.jpg" class="img-fluid" alt="assemblyImage" loading="lazy">
        <br>
        <img src="images/AssemblyServo/img9_compressed.jpg" class="img-fluid" alt="assemblyImage">
        <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSix">
        Change the attachment on the robot arm
      </a>
    </div>
    <div id="collapseSix" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Take the robot arm labelled number '2', and have a look at the attachment on its end. Use your screwdriver to unscrew the screws and take off the attachment. Be careful not to lose the screws!</p>

        <img src="images/AssemblyServo/Unscrew_old_attmt.jpg" class="img-fluid" alt="Unscrew Stepper Motor Attachment">

        <p>Take the bag labelled 'Motors Workshop' and take out the shaft attachment inside. It should look like the picture below. Put the old attachment into the bag.</p>
        
        <img src="images/AssemblyServo/Switch_attachment_1.png" class="img-fluid" alt="Switch attachment">

        <p>Attach the new attachment from the 'Motors Workshop' bag to Robot Arm 2 using the same screws. Remember, righty tighty, lefty loosey!</p>

        <img src="images/AssemblyServo/Switch_attachment_2.png" class="img-fluid" alt="Switch attachment 2">

        <p>Have a closer look at the attachment on the robot arm. Then take a look at the shaft on the motor. Why do you think the attachment has been designed that way? Can you think of other shapes you can use for a shaft that looks like this?</p>
        <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSeven">
        Attach the robot arm
      </a>
    </div>
    <div id="collapseSeven" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Make sure the battery holder is switched off. If it is on, the servomotor will try to stay in place and you might break something if you try to force it! The motor also moves very quickly, and you might hurt yourself if it is moving. So keep the battery holder off if you're going to use your hands.</p>

        <p>Take the robot arm and push it onto the shaft of the servomotor firmly, as shown in the photo. Try and move it, gently. It should be able to move, up to a certain point. Don't force it, or you might break the gears!</p>

        <img src="images/AssemblyServo/Put_on_arm.jpg" class="img-fluid" alt="Switch attachment">

        <p>Push the arm so that it points straight ahead.</p>

        <img src="images/AssemblyServo/Servo_arm_forward.jpg" class="img-fluid" alt="assemblyImage">

        <p>Once you're done with that, we're ready to start programming!</p>

        

      </div>
    </div>
  </div>

</div>


<!--Comment: This section is markdown again-->

<br><br>




<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="Activity2" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #2</h2>
</div>

### Programming on the Microbit

<br>

<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

Now we've got our servomotor set up, let's learn a bit about how to use the microbit!

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">

  
  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOneB">
        Connect the microbit usb cable to your computer
      </a>
    </div>
    <div id="collapseOneB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Connect the micro-usb cable between your computer and the microbit. It plugs into the top of the microbit and into the usb port on your computer. When it's connected a red light should come on the microbit, and a yellow light will start flashing.
        <br><br>
        <img src="images/AssemblyServo/img27_compressed.jpg" class="img-fluid" alt="assemblyImage">
        <br> <br>
        <img src="images/AssemblyServo/img28_compressed.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwoB">
        Check your microbit is working! - write some code
      </a>
    </div> 
    <div id="collapseTwoB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        In your browser open a new tab and navigate to the online python editor for microbit: <a href="https://python.microbit.org/" target="_blank">Link here</a>

        <br><br>

        First of all let's test the microbit is working. Enter the following code into the python <br> 

        <script src="https://gist.github.com/meisben/ac85b4e31963a878a4bfe12f53970e72.js"></script> 

        <br>
        You can transfer this code into your python either by typing it in, or by copying and pasting. Please be careful to make sure you enter it exactly the same! Where you put spaces, tabs, brackets, full stops and other punctuation is really important in python because these characters tell the computer how to understand your code!
        An easy way to check this is by comparing the number of lines in the example above with the number of lines in your online python editor.

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThreeB">
        Download the test code to your microbit
      </a>
    </div>
    <div id="collapseThreeB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Download the code and transfer it to your microbit by clicking on 'Send to micro:bit' at the bottom, and following the instructions given on the screen.
        <br>
        <img src="images/Coding/python_editor.png" class="img-fluid" alt="Python Editor">


        <br><br>
        If you've got any problems with this you can follow this guide to resolve them: <a href="https://python-editor-2-1-2.microbit.org/help.html?snippets=true" target="_blank">Link here</a>
        
        <br><br>

        You should see your microbit display light up and the code run! Observe what happens on the microbit display. <br><br>
        <ul>
        <li>Can you change the text to your name? (Tip: "awesome person"?)</li>
        <li>Can you change the image to another type? (Tip: look at this and see what <b>Images</b> there are! <a href="https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/images.html" target="_blank">link</a>) </li>
        </ul>
        <br><br>

        <p>If you can't figure it out, don't worry, we talk about it more later!</p>
        
        <p>If it doesn't work check your code and connections, something is wrong there. And please remember you can always ask for help!</p>

        <br> <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFourB">
        Reset the microbit
      </a>
    </div>
    <div id="collapseFourB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Now try pressing the reset button on the back of the microbit. This restarts the microbit and the program will restart from the beginning. Remember you can always press this if your microbit stops working or becomes unresponsive!

        <br> <br>

        <img src="images/AssemblyServo/IMG_20210329_164546_compressed_annotated.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFiveB">
        Understanding what the code is doing
      </a>
    </div>
    <div id="collapseFiveB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Now let's go through the code, and see if we can make the microbit do something new!</p>

        <p>Did you notice what was showing on the LED screen? Have a look at the code and see if you can find which lines they appear on.</p>

        <br>

        <pre class="prettyprint" style="max-height:300px;overflow:auto">
          # Our test microbit program 
          # tip: some of this code might already be in your online python editor when you load it!

          # Import this library so we can talk to the microbit
          from microbit import *

          # Loop for ever (infinite loop)
          while True:
              display.scroll('Hello, awesome person!') # What did you see on the screen?
              display.show(Image.HEART)
              sleep(2000)
        </pre>


        <br>
        
        <p>"display.scroll" is a <b>function</b> that lets you display a scrolling line of text, and "display.show" is a function that lets you show a small picture! How do you think you can change what shows on the screen?</p>

        <p>Let's give it a go. Change the text ('Hello, awesome person!') to whatever you want. You can look up the kind of pictures you can display in "display.show" at this <a href="https://microbit-micropython.readthedocs.io/en/v1.0.1/image.html" target="_blank">website</a> under the header '<b>Attributes</b>'.</p>
        

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSixB">
        Thinking about variables
      </a>
    </div>
    <div id="collapseSixB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p><b>Variables</b> are one way to reduce the amount of code we write!</p>

        <p>It's like a box with a label on it, like 'say_this'. You can put a value in this box and it will stay in this box until you give the box a different value. You can then use 'say_this' in the script, and whenever it sees it it will then go look for this box called 'say_this' and take the value inside it.</p>

        <p>You can <i>assign</i> a variable and then use it like this:</p>
        <br>

        <pre class="prettyprint" style="max-height:300px;overflow:auto">
          # The variable is assigned the value 'Hello, awesome person!'
          say_this = 'Hello, awesome person!' 

          display.scroll(say_this)
        </pre>

        <br>
        <p>You must assign a variable before you can use it. There are rules about the names you can give variables; usually it can't start with a number and it mustn't have any spaces.</p>

        <p><b>Give it a go!</b></p>
        <ul>
        <li>Make a new variable with another sentence in it, and display it after the image. Use the code above for reference!</li>
        </ul>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSevenB">
        Let's try a function!
      </a>
    </div>
    <div id="collapseSevenB" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p><b>Functions</b> are another way to reduce the amount of code we write!</p>

        <p>It's like a set of instructions with a label on the top, like 'do_this'. You can then use 'do_this' in the script, and whenever it sees it it will then go look for this set of instructions called 'do_this' and do what it says. You can also give the function variables, so that it can use the variable to do things!</p>

        <p>In the script, you <i>define</i> a function and then use it like this:</p>

        <pre class="prettyprint" style ="height:300px;overflow:auto">
          def do_this():   # defining the function
              #After defining the function, all the lines that are indented (the same alignment on the left) will be counted
              #as part of the function! This is called the body of the function.
              
              display.show(Image.HEART)
              
              #End of body of function

        
          do_this() # calling the function!
        </pre>
        
        <p>Similar to variables, you have to define the functions before you can use them!</p>
        <p>When do you think this would be useful? What other functions would you make?</p>

        <p><b>Give it a go!</b></p>
        <ul>
        <li>Try and make two different functions that will show two different images after telling you what an awesome person you are! Use the code given above as a reference.
        Hint: You can name one function <b>Show_Image_Smile</b> and the other function <b>Show_Image_Fabulous</b>. Then look up what images you need to use from the link given in the previous steps!</li>
        </ul>

          </div>
        </div>
      </div>
      

    </div>

<br><br>

<div id="Activity3" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #3</h2>
</div>

### Programming the Servomotor

<br>

<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

Now we've got the hang of programming on our microbit, we can start figuring out how to move the servomotor!

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOneC">
        Load our motor code
      </a>
    </div>
    <div id="collapseOneC" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Next we will load our code to make our motor move!</p>

        <p>You can download the code we will use from this <a href="./activity_code/servomotor_code_zero.py" download="servomotor_code_zero.py" target="_blank"> link</a>.</p>

        <p>This link will download a python file to your computer. </p>
        
        <p>Next, in your python editor click on 'Open' and then select the python file you just downloaded (it's called: servomotor_code_zero.py). The code will load and you will see it on your screen. There should be 128 lines, if you scroll all the way to the bottom.</p>

        <br> 
        <img src="images/Coding/python_editor_load.png" class="img-fluid" alt="python_editor_load">
        <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwoC">
        Download the motor code to your microbit
      </a>
    </div>
    <div id="collapseTwoC" class="collapse" data-parent="#accordion">
      <div class="card-body">

        <p> Make sure your battery is turned <b>off</b>!!</p>

        <p>Download the code and transfer it to your microbit by clicking on 'Send to micro:bit' at the bottom, and following the instructions given on the screen.</p>
        <br>
        <img src="images/Coding/python_editor.png" class="img-fluid" alt="Python Editor"> 
        <p>If you've got any problems with this you can follow this guide to resolve them: <a href="https://python-editor-2-1-2.microbit.org/help.html?snippets=true" target="_blank">Link here</a></p>

        <p>You should see the microbit start up with a picture of a ghost! That's how you know you've got the right code. </p>

        <br> <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThreeC">
        Zero the arm
      </a>
    </div>
    <div id="collapseThreeC" class="collapse" data-parent="#accordion">
      <div class="card-body">
       
        <p><b>Take off the motor arm from the motor.</b> Turn on the battery pack, and press the microbit logo on the microbit board.</p>

        <p><img src="images/Coding/microbit_logo.png" class="img-fluid" alt="microbit_logo_to_press"></p>

        <p>Were you able to tell whether the motor moved? It might have made a sound, but it is hard to tell how far the motor moved. This is where the motor arm comes in handy. Push the motor arm back on so it points to the right. So now we know that both the motor and the arm is pointing to zero degrees.</p>

        <p><img src="images/AssemblyServo/Servo_arm_zero.jpg" class="img-fluid" alt="assemblyImage"></p>

        <p>Turn off the battery pack. Move the arm a bit, you should be able to move the arm. <b>Keep your hands away</b>, and then turn on the battery pack again. What happens?</p>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFourC">
        Try and move the robot arm (gently)
      </a>
    </div>
    <div id="collapseFourC" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>When the robot arm is stationary and the battery pack is turned on, try and turn the robot arm (gently) with your hand. You should find that if you do that, it will not want to move, and will keep trying to go back to where it should be! You will hear it complaining a bit. This is a feature of servomotors. As we mentioned earlier, they use a sensor to try and go to a position according to the signal that you give it.</p> 
        <p>If you push too hard, things might break so be careful!</p>
        <br> <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFiveC">
        Understanding the code
      </a>
    </div>
    <div id="collapseFiveC" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Let's have a look at the code. Don't worry if it doesn't make sense to you, it's pretty complicated! You might be able to recognise some of the things we just learned about variables and functions.</p>
        <p>All this stuff at the beginning from line 1 to 52 is code for setting up the robotics board. It helps the microbit communicate with it and then use it to send signals to the motors.</p>
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          # ------------------------------------------#
          # Imports                                   #
          # ------------------------------------------#

          from microbit import *
          import math
          import music

          # ------------------------------------------#
          # Create a class for the robotics board     #
          # ------------------------------------------#

          class KitronikRoboticsBoard:
              PRESCALE_REG = 0xFE
              MODE_1_REG = 0x00
              SRV_REG_BASE = 0x08
              MOT_REG_BASE = 0x28
              REG_OFFSET = 4
              #SERVO_MULTIPLIER = 226
              SERVO_MULTIPLIER = 190
              SERVO_ZERO_OFFSET = 0X66
              ANGLE_ZERO_OFFSET = 0

              chipAddress = 0x6C
              initialised = False
              stepInit = False
              stepStage = 0
              stepper1Steps = 200
              stepper2Steps = 200

              def __init(self):
                      
                  buf = bytearray(2)

                  buf[0] = self.PRESCALE_REG
                  buf[1] = 0x85 #50Hz
                  i2c.write(self.chipAddress, buf, False)
                  
                  for blockReg in range(0xFA, 0xFE, 1):
                      buf[0] = blockReg
                      buf[1] = 0x00
                      i2c.write(self.chipAddress, buf, False)

                  buf[0] = self.MODE_1_REG
                  buf[1] = 0x01
                  i2c.write(self.chipAddress, buf, False)
                  self.initialised = True
          </pre>
        <br>
        <p>This bit over here from line 54 to 75 are <b>functions</b> that can be used for common commands to the motors that we've already written for you.</p> 
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          def servoWrite(self, servo, degrees):
            if self.initialised is False:
                self.__init(self)
            buf = bytearray(2)
            calcServo = self.SRV_REG_BASE + ((servo - 1) * self.REG_OFFSET) #find the servo number
            # = 8 + ((servo number - 1) * 4)
            HighByte = False
            degrees+=self.ANGLE_ZERO_OFFSET
            PWMVal = ((degrees * 100 * self.SERVO_MULTIPLIER) / 10000) + self.SERVO_ZERO_OFFSET
            # (degree input * 100 * 266)/( 10000 + 102)

            if (PWMVal > 0xFF): #if PWMval more than 255
                HighByte = True
            buf[0] = calcServo
            buf[1] = int(PWMVal)
            i2c.write(self.chipAddress, buf, False)
            buf[0] = calcServo + 1
            if (HighByte):
                buf[1] = 0x01
            else:
                buf[1] = 0x00
            i2c.write(self.chipAddress, buf, False)
        </pre>
        <br>
        <p>This first bit of code you've been given from line 103 to 116 just sets the motor to zero, which is what we used to zero the arm. Can you recognise what it does? Can you figure out what variables there are? What will happen if you change them?</p>
        <div style ="max-height:300px;overflow:auto">
          <pre class="prettyprint">
            # This will reset it to zero!
            if pin_logo.is_touched():

                music.pitch(200, duration=150, wait=True)

                # Set motor angle variable to zero
                motor_angle = 0

                # show the motor angle
                display.scroll("%d" %
                    (motor_angle), delay=100, wait=True, loop=False)
                sleep(100)

                # Tell the board to move the servomotor to motor_angle
                theBoard.servoWrite(theBoard, motor_pin, motor_angle)
          </pre>
        </div>
        <br>
        <p>Did you see that we used 'if' in the code? These are called <b>conditionals</b>. We use conditionals to ask our code to check if something is true before it does it. So if it detects that the microbit logo has been touched (pin_logo.is_touched()), it will run the code from line 105 to 116.</p>
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSixC">
        Let's write some code!
      </a>
    </div>
    <div id="collapseSixC" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Now that you have a feel for how the code works, let's try writing some of our own! I've given you a headstart on the A button and B button with the conditionals. If you're not sure what to do, don't worry, I'll give you some hints!</p>
        <br>
        <p>First you'll need to remove the '#' symbol in front of line 118, 122, and 129. The '#' symbol at the front of a line makes that line a comment, and that line will be ignored.</p>
        <p><img src="images/Coding/Remove_comments_servo.png" class="img-fluid" alt="Where to remove comments"></p>
        <p>Once you've done that, your code should look like the following:</p>
        <br>
        <pre class="prettyprint" style="max-height:300px;overflow:auto">
          else:
          
              # Do something if button A is pressed. What do you do if you want button A to increase the angle by 10 degrees every time
              # you press a button?
              if button_a.is_pressed():
                  #insert code here
                  
                  
          
              # Do something if button B is pressed. What do you do if you want button B to decrease the angle by 10 degrees every time
              # you press a button?
              if button_b.is_pressed():
                  #insert code here
        </pre>
        <br>
        
        <p>Give it a bit of a think! If you're confident with Python and microbits, try coding it on your own. If you're not sure, click on the Hint below to get some hints on how to do it. You can also see some example answer code.</p>
        <br>

        <p>
          <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#Servo-Hint" aria-expanded="false" aria-controls="Servo-Hint">
            Hint
          </button>
        </p>
        <div class="collapse" id="Servo-Hint">
          <div class="card card-body">
            
            <ul>
            <li>An easy way to start is copy the code from line 104 to 116, and put it at the '#insert code here'. Then you can have a look at the code and see what you can change.</li>
            <li>Do you understand what the code is doing? First it sets a value of 'motor_angle', then it uses the function servoWrite to tell the servomotor to go to 'motor_angle'.</li>
            <li>How can you change the variable 'motor_angle' so that it increases or decreases every time you press the button?</li>
            <li>You can change the value of a variable by calling itself and doing a bit of math.</li>
            <li>Our motor can only go from 0 degrees to 180 degrees! How can you keep the motor angle from exceeding these values? (Hint hint: You can use a conditional ;))</li>
            <li>Example of conditional to check if motor angle is less than 0
              <pre class="prettyprint" style="max-height:300px;overflow:auto">
                if motor_angle < 0:
                    #do something
              </pre>
              </li>
            </ul>
          </div>
        </div>
        <br>

        <p>
          <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#Servo-Ans" aria-expanded="false" aria-controls="Servo-Ans">
            Example Answer
          </button>
        </p>
        <div class="collapse" id="Servo-Ans">
          <div class="card card-body">
            
            <p>This is just one way you can do it!</p>
            <br>
            <pre class="prettyprint" style="max-height:300px;overflow:auto">
              if button_a.is_pressed():

                  music.pitch(200, duration=150, wait=True)

                  # make sure we don't go above the motor limit!
                  if motor_angle < 180:
                      motor_angle = motor_angle + step_angle # Increase the motor_angle by step_angle

                  # show the motor angle
                  display.scroll("%d" %
                      (motor_angle), delay=100, wait=True, loop=False)
                  sleep(100)

                  # Tell the board to move the servomotor to motor_angle
                  theBoard.servoWrite(theBoard, motor_pin, motor_angle)
            </pre>
            <br>
          </div>
        </div>

        <p>If you're really stuck, you can get the complete script here: <a href="./activity_code/servomotor_code.py" download="servomotor_code.py" target="_blank"> link</a></p>
        <p>You can also have a play around with the code! Have a think about some of the questions below and see if you can figure them out.</p>
        <ul>
        <li>How can you get the motor to move further when you push the A or B button?</li>
        <li>How do you get the microbit to display a different picture when it starts up?</li>
        <li>What types of robots do you think this motor would be good for? What sort of movements?</li>
        </ul>
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSevenC">
        Let's move the motor!
      </a>
    </div>
    <div id="collapseSevenC" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p style="text-align:center"><span style="color:Red"><b>!!! Make sure your hands are far away from the motor arm! !!!</b></span> </p>
        <p>Try pressing the buttons.</p>
        <p>If you did it the same way as the zero code, button A will increase the angle, and button B will decrease the angle. You can see the angle scrolling across the LEDs, before the arm moves.</p>
        <br>
        <p>Turn off the battery pack. Move the arm a bit, you should be able to move the arm. <b>Keep your hands away</b>, and then turn on the battery pack again. What happens?</p>
        <p>Try going all the way up to 180 degrees. Is it exactly 180 degrees from where it started? If it isn't, why do you think it happens?</p>
        <br>
      </div>
    </div>
  </div>

  

</div>

<br><br>

<!--Comment: This section is markdown again-->

## The Stepper Motor 
<br>

Now that we've looked at a servomotor, what it looks like, how you connect it and how you make it move, let's do the same for the stepper motor. The stepper motor we've given you in the kit is a miniature unipolar stepper motor. Just like the servomotor, it has a permanent magnet, electromagnets and a gearbox inside. The gearbox for the stepper motor also helps to increase the torque of the motor while reducing how fast it moves. However, the difference is that instead of the electromagnet rotating, the permanent magnet rotates instead! That means the permanent magnet is connected to the shaft.

<br>

Electromagnet coils are placed around the permanent magnet in the middle, as shown in the figure below. By activating each coil in sequence, the the permanent magnet in the middle will rotate.

<br>
<p style="text-align: center;"><img src="images/Explanation/stepper_motor_animation.gif" alt="Stepper Motor Working Principle"></p>

*Image copyright Sam Hoh*

<br>

As you can see from the animation, the permanent magnet moves in **steps**, which is why it's called a stepper motor! These types of motors have very good positional control, and are very good at holding their position. You don't really need a sensor in order to make it turn a certain amount, since you can just count the number of steps. But if you control it by moving a certain amount of steps, it won't actually know where you started! So you need to move it to its starting position before you turn on the motor and control program.

This is in comparison to the servomotor, which knows what position it is at even if you turn off the motor, but is slightly worse at holding that position.

Let's take the stepper motor out of its bag and have a look at it.

<br>
<p style="text-align:center;"><img src="images/Explanation/Stepper_motor_parts.png"></p>

You can see the body of the motor, where the coils and magnet are. The shaft of the motor sticks out from the 3D printed attachment, and the attachment is covering the gearbox. This is so that dirt won't get in, which can mess with how it moves! There are four wires coming out from the body of the motor. These connect to the electromagnet coils.

Now that we know a bit about our stepper motor, let's try and make it move!


<br>
<br>


<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="Activity4" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #4</h2>
</div>

<br>

<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

### Let's assemble the stepper motor demonstrator!

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOneD">
        Taking off the servomotor
      </a>
    </div>
    <div id="collapseOneD" class="collapse" data-parent="#accordion">
      <div class="card-body">
      <p>Turn off the battery before you disassemble the robot.</p>
      <p>Take off the robot arm from the motor. Unplug the servomotor from the robotics board, and gently pry it out of the motor base. You can then put it back into its plastic bag.</p>
      <br>
      <p style="text-align: center;"><img src="images/AssemblyStepper/Disassembly_1.png" class="img-fluid" alt="assemblyImage"></p>
      
      <br>
    


      </div>
    </div>
  </div>

 <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwoD">
        Take out the parts needed
      </a>
    </div>
    <div id="collapseTwoD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Take out the bag labelled "Assembly Parts". Take out the green bearing holder, a bearing, and two screws and two nuts. Here is a photo to help you identify what's in the bag!</p> 
        <br>
        <img src="images/AssemblyStepper/img4_compressed_annotated.jpg" class="img-fluid" alt="assemblyImage">
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThreeD">
        Begin to attach the stepper motor!
      </a>
    </div>
    <div id="collapseThreeD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Take the motor. We're going to attach it to the green bearing holder. Take an M3 nut and place it in one of the hexagonal shaped holes in the bearing holder.</p> 

        <img src="images/AssemblyStepper/img8_compressed_annotated.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFourD">
        Continue to attach the first motor!
      </a>
    </div>
    <div id="collapseFourD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Next take an M3 screw. Line the holes up between the green bearing holder and the motor. Insert the screw into the same hole that your nut is resting in, then use the right sized screwdriver attachment to tighten the screw. You may need to hold the nut in place with your finger. You need to turn it clockwise to tighten it! A good way to remember this is the phrase "righty tighty, lefty loosy".

        <img src="images/AssemblyStepper/img14_compressed.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFiveD">
        Finish attaching the first motor
      </a>
    </div>
    <div id="collapseFiveD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Repeat this for the second hole between the green bearing holder and the motor. Take another nut, insert it into the hexagonal shaped hole, and then use a screw to tighten the two parts together.</p>
        <img src="images/AssemblyStepper/img15_compressed.jpg" class="img-fluid" alt="assemblyImage">
      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSixD">
        Finish the robot arm base
      </a>
    </div>
    <div id="collapseSixD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Clip the motor into the robot arm base. Make sure the wires of the motor are pointing towards you. You will have to gently bend the side of the base so that it snaps in! Well done! You have finished the installation of our base motor! :)

        <img src="images/AssemblyStepper/img17_compressed.jpg" class="img-fluid" alt="assemblyImage">
        <br>
        <img src="images/AssemblyStepper/img19_compressed.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSevenD">
        Attach wires to the robot arm base motor
      </a>
    </div>
    <div id="collapseSevenD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        Take one set of the jumper wires. Take the small screwdriver and gently screw these into the motor connector. Make sure that the wires aren't crossed over! They don't need to be screwed hard, just gently so that if you give them a little tug they can't pull out. Remember righty tighty, lefty loosy!

        <img src="images/AssemblyStepper/img20_compressed.jpg" class="img-fluid" alt="assemblyImage">

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseEightD">
        Connect the wires from the motor to the Robotics Board.
      </a>
    </div>
    <div id="collapseEightD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>The wires connect into the Robotics board in the same order they came from the motor. Attach them gently with the big screwdriver attachment.</p>
        <br>
        <img src="images/AssemblyStepper/img23_compressed.jpg" class="img-fluid" alt="assemblyImage">
        <br>
        <p>The motor connector ports should line up with the Robotics board ports as shown in the figure. Make sure there aren't any crossovers in the wires! That means the same colour wire in port 1 on the motor connector on the left should be the same colour wire on port a on the Robotics board on the right.</p>
        <br>
        <img src="images/AssemblyStepper/img23a.jpg" class="img-fluid" alt="assemblyImage">
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseNineD">
        Change the motor shaft attachment on the arm.
      </a>
    </div>
    <div id="collapseNineD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Unscrew the screws on the attachment on the robot arm. Keep the screws safe! Then put the attachment back in the plastic bag labelled <b>'Motors Workshop'</b>, and take out the old attachment. It should look like this:</p>
        <br>
        <img src="images/AssemblyStepper/Disassembly_parts_go_where.png" class="img-fluid" alt="assemblyImage">
        <br>
        <p>Line up the holes of the motor shaft attachment to the holes on the robot arm so that the flat side of the 'D' hole shape faces the other end of the arm, and use the screws to attach it. Remember, righty tightey, lefty loosey!</p>
        <br>
        <img src="images/AssemblyStepper/Reattach_stepper_motor_attmt.png" class="img-fluid" alt="assemblyImage">
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTenD">
        Put the motor arm on!
      </a>
    </div>
    <div id="collapseTenD" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Take the robot arm and place it so that the small 'D' shape in the green part of the robot arm lines up with the motor shaft. You should be able to push the two together gently. Now give the robot arm a gentle turn to check it rotates.</p> <br>
      <img src="images/AssemblyStepper/img30_compressed.jpg" class="img-fluid" alt="assemblyImage">
      <br> <br>
      <img src="images/AssemblyStepper/Stepper_zero.jpg" class="img-fluid" alt="assemblyImage">
        <br> <br>
        <p>Now you're ready to code!</p>
      </div>
    </div>
  </div>

</div>

<br>
<br>



<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="Activity5" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #5</h2>
</div>


<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

<br>

### Programming our Stepper Motor
<br>


<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOneE">
        Load our motor code
      </a>
    </div>
    <div id="collapseOneE" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Next we will load our code to make our motor move!</p>

        <p>You will need to download new code for the stepper motor. You can download the code we will use from this <a href="./activity_code/stepper_motor_code_zero.py" download="stepper_motor_code_zero.py" target="_blank"> link</a>.</p>
        
        <br><br>

        This link will download a python file to your computer. 

        <br><br>
        
        Next, in your python editor click on 'Open' and then select the python file you just downloaded (it's called: stepper_motor_code_zero.py). The code will load and you will see it on your screen. There should be 199 lines, if you scroll all the way to the bottom.</p>

        <br> 
        <img src="images/Coding/python_editor_load_stepper.png" class="img-fluid" alt="python_editor_load_stepper">
        <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwoE">
        Download the motor code to your microbit
      </a>
    </div>
    <div id="collapseTwoE" class="collapse" data-parent="#accordion">
      <div class="card-body">

        <p> Make sure your battery is turned <b>off</b>!!</p>

        <p>Download the code and transfer it to your microbit by clicking on 'Send to micro:bit' at the bottom, and following the instructions given on the screen.</p>
        <p><img src="images/Coding/python_editor.png" class="img-fluid" alt="Python Editor">  </p>
        <p>If you've got any problems with this you can follow this guide to resolve them: <a href="https://python-editor-2-1-2.microbit.org/help.html?snippets=true" target="_blank">Link here</a></p>

        <p>You should see the microbit start up with a picture of a snake! That's how you know you've got the right code. </p>

        <br> <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThreeE">
        Zero the arm
      </a>
    </div>
    <div id="collapseThreeE" class="collapse" data-parent="#accordion">
      <div class="card-body">
       
        <p>This motor works a little bit differently from the servomotor. First, make sure the battery pack is turned <b>off</b>.</p>

        <p>Push the motor arm gently so it points to the right. So now we know that the arm is pointing to zero degrees.</p>

        <p>Press the microbit symbol on the board, and the LED should show the text 'Reset 0'.</p>

        <p><img src="images/AssemblyStepper/Stepper_zero.jpg" class="img-fluid" alt="assemblyImage"></p>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFourE">
        Try and move the robot arm (gently)
      </a>
    </div>
    <div id="collapseFourE" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Turn on the battery pack.</p>
        <p>When the robot arm is stationary, try and turn the robot arm (gently) with your hand. You should find that if you do that, it will not want to move! Compared to the servomotor, it doesn't make any noise or complain. This is a feature of a stepper motor, it's very good at keeping its position.</p> 
        <p>If you push too hard, you might <b>break the motor shaft attachment so be careful</b>! If the motor shaft attachment is strong enough, the motor might just 'slip'. That means it will skip a step.</p>
        <p>Try turning off the battery pack. Move the arm, and then turn the battery pack on again. What do you observe? How is it different from a servomotor?</p>
        <br>
        <p>You should notice that when you turn the battery pack on, it won't go back to what you set as 'zero degrees' in the previous step. This is because the stepper motor doesn't have a sensor to tell it where zero degrees is! So even though it's very good at being accurate and holding its position, if the power turns off, without a sensor it won't know where it is. The servomotor is better for moving fast, and if you want it to be better at positioning, you will need to pay more.</p>
        <br> <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFiveE">
        Understanding the code
      </a>
    </div>
    <div id="collapseFiveE" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Let's have a look at the code.</p>
        <p>As before, all this stuff at the beginning from line 1 to 50 is code for setting up the robotics board so our microbit can communicate with it and then use it to send signals to the motors.</p>
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          # ------------------------------------------#
          # Imports                                   #
          # ------------------------------------------#

          from microbit import *
          import math
          import music

          # ------------------------------------------#
          # Create a class for the robotics board     #
          # ------------------------------------------#

          class KitronikRoboticsBoard:
              PRESCALE_REG = 0xFE
              MODE_1_REG = 0x00
              SRV_REG_BASE = 0x08
              MOT_REG_BASE = 0x28
              REG_OFFSET = 4
              #SERVO_MULTIPLIER = 226
              SERVO_MULTIPLIER = 190
              SERVO_ZERO_OFFSET = 0X66
              ANGLE_ZERO_OFFSET = 0

              chipAddress = 0x6C
              initialised = False
              stepInit = False
              stepStage = 0
              stepper1Steps = 200
              stepper2Steps = 200

              def __init(self):
                      
                  buf = bytearray(2)

                  buf[0] = self.PRESCALE_REG
                  buf[1] = 0x85 #50Hz
                  i2c.write(self.chipAddress, buf, False)
                  
                  for blockReg in range(0xFA, 0xFE, 1):
                      buf[0] = blockReg
                      buf[1] = 0x00
                      i2c.write(self.chipAddress, buf, False)

                  buf[0] = self.MODE_1_REG
                  buf[1] = 0x01
                  i2c.write(self.chipAddress, buf, False)
                  self.initialised = True
          </pre>
        <br>
        <p>The lines 52 until 154 are <b>functions</b> that can be used for common commands to the motors. This is a good example of how we would use functions!</p> 
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          def motorOn(self, motor, direction, speed):
            if self.initialised is False:
                self.__init(self)
            buf = bytearray(2)
            motorReg = self.MOT_REG_BASE + (2 * (motor - 1) * self.REG_OFFSET)
            HighByte = False
            OutputVal = speed * 40

            if direction == "forward":
                if OutputVal > 0xFF:
                    HighByte = True
                    HighOutputVal = int(OutputVal/256)
                buf[0] = motorReg
                buf[1] = int(OutputVal)
                i2c.write(self.chipAddress, buf, False)
                buf[0] = motorReg + 1
                if HighByte:
                    buf[1] = HighOutputVal
                else:
                    buf[1] = 0x00
                i2c.write(self.chipAddress, buf, False)

                for offset in range(4, 6, 1):
                    buf[0] = motorReg + offset
                    buf[1] = 0x00
                    i2c.write(self.chipAddress, buf, False)

            elif direction == "reverse":
                if OutputVal > 0xFF:
                    HighByte = True
                    HighOutputVal = int(OutputVal/256)
                buf[0] = motorReg + 4
                buf[1] = int(OutputVal)
                i2c.write(self.chipAddress, buf, False)
                buf[0] = motorReg + 5
                if HighByte:
                    buf[1] = HighOutputVal
                else:
                    buf[1] = 0x00
                i2c.write(self.chipAddress, buf, False)

                for offset2 in range(0, 2, 1):
                    buf[0] = motorReg + offset2
                    buf[1] = 0x00
                    i2c.write(self.chipAddress, buf, False)

          def stepperMotorTurnAngle(self, stepper, angle):
              angleToSteps = 0

              if self.initialised is False:
                  self.__init(self)

              if angle < 0:
                  direction = "reverse"
              else:
                  direction = "forward"

              angleToSteps = int(
                  ((abs(angle) - 1) * (self.stepperSteps - 1)) / (360 - 1) + 1)

              self._turnStepperMotor(self, stepper, direction, angleToSteps)

          def stepperMotorTurnSteps(self, stepper, direction, stepperSteps):
              if self.initialised is False:
                  self.__init(self)

              self._turnStepperMotor(self, stepper, direction, stepperSteps)

          def _turnStepperMotor(self, stepper, direction, steps):
              stepCounter = 0

              while stepCounter < steps:
                  if self.stepStage == 1 or self.stepStage == 3:
                      if stepper == 0:
                          currentMotor = 1
                      else:
                          currentMotor = 3
                  else:
                      if stepper == 0:
                          currentMotor = 2
                      else:
                          currentMotor = 4

                  if self.stepStage == 1 or self.stepStage == 4:
                      currentDirection = "forward"
                  else:
                      currentDirection = "reverse"

                  self.motorOn(self, currentMotor, currentDirection, 100)
                  sleep(50)

                  if direction == "forward":
                      if self.stepStage == 4:
                          self.stepStage = 1
                      else:
                          self.stepStage += 1
                  elif direction == "reverse":
                      if self.stepStage == 1:
                          self.stepStage = 4
                      else:
                          self.stepStage -= 1

                  stepCounter += 1
        </pre>
        <br>
        <p>This first bit of code from line 175 to 185 just sets the motor to zero, which is what we used to zero the arm. Can you recognise what I'm doing? Can you figure out what variables there are? What will happen if I change them?</p>
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          # Detect if the microbit logo has been touched! This will reset it to zero!
          if pin_logo.is_touched():
              # Play a tune
              music.pitch(200, duration=150, wait=True)
              # Set the angle the motor needs to move
              targetAngle = currentAngle
              # Update current angle - go to zero
              currentAngle = 0
              # Display a message
              display.scroll(currentAngle, delay=120, wait=False, loop=False)
              # Rotate the motor
              theBoard.stepperMotorTurnAngle(
                  theBoard, currentRotationMotor, angle=-targetAngle)
        </pre>
        <p>Earlier when I explained the stepper motor, I said it doesn't know what angle it's at. So we have to keep track of it ourselves using the variable 'currentAngle'. We have to use a new variable to hold the value of 'currentAngle', otherwise once we set it to zero, we won't know how much to turn to go back to zero position! So first, we set the variable 'targetAngle' to hold the value of 'currentAngle', before I set 'currentAngle' to zero. Then 'targetAngle' is the angle the motor should turn. Look at lines 186 and 187. It tells the stepper motor to turn angle by a value 'angle=-targetAngle'. </p>
        <p>This picture should help explain the position we're referring to whenever we're updating 'currentAngle'.</p>
        <p><img src="images/Coding/Angles_Position.png" class="img-fluid" alt="angleposition"></p>
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSixE">
        Let's write some code!
      </a>
    </div>
    <div id="collapseSixE" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Now that you have a feel for how the code works, let's try writing some of our own! I've given you a headstart on the A button and B button with the conditionals. This is going to be pretty similar to the previous code. If you're not sure what to do, don't worry, we'll go through it together!</p>
        <br>
        <p>First you'll need to remove the '#' symbol in front of line 118, 122, and 129. The '#' symbol at the front of a line makes that line a comment, and that line will be ignored.</p>
        <p><img src="images/Coding/Remove_comments_stepper.png" class="img-fluid" alt="Where to remove comments-stepper"></p>
        <p>Once you've done that, your code should look like the following:</p>
        <br>
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          #else:

              # Do something if button A is pressed. What do you do if you want button A to increase the angle by 10 degrees every time
              # you press a button?
              #if button_a.is_pressed():
                  #insert code here
                  
                  
          
              # Do something if button B is pressed. What do you do if you want button B to decrease the angle by 10 degrees every time
              # you press a button?
              #if button_b.is_pressed():
                  #insert code here
        </pre>
        <br>
        <p>Give it a bit of a think! If you're confident with Python and microbits, try coding it on your own. If you're not sure, click on the Hint below to get some hints on how to do it. You can also see some example answer code.</p>
        <br>
        <p>
          <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#Stepper-Hint" aria-expanded="false" aria-controls="Stepper-Hint">
            Hint
          </button>
        </p>
        <div class="collapse" id="Stepper-Hint">
          <div class="card card-body">
            
            <ul>
            <li>An easy way to start is copy the code from line 177 to 187, and put it at the '#insert code here'. Then you can have a look at the code and see what you can change.</li>
            <li>If you want to display the new angle of the motor, you will need to add the 'stepAngle' to the 'currentAngle' before you display it. Note that if you don't keep track of the 'currentAngle', you will lose your position!</li>
            <li>Since the function tells the stepper motor to turn a certain amount, you can tell the stepper motor to turn the amount given in the variable 'stepAngle' at line 163 by using the following function.
            <pre class="prettyprint" style ="max-height:300px;overflow:auto">
              theBoard.stepperMotorTurnAngle(theBoard, currentRotationMotor, angle=stepAngle)
            </pre></li>
            <li>Our stepper motor can go all the way around! But in this exercise, you might not want the display value to go below 0 degrees or above 360 degrees. 360 degrees is already one full circle! Look at the image in the previous step to see how we might use the angle on the display to tell us what position the arm is at. How can you keep the motor angle from exceeding these values while still figuring out its position? (Hint hint: You can use a conditional ;))</li>
            <li>You can use a conditional to make sure if it goes into a negative value, it starts again from 360 degrees.
              <pre class="prettyprint" style="max-height:300px;overflow:auto">
                # keep it from going into a negative number
                if currentAngle < 0: 
                    currentAngle = 360 + currentAngle
              </pre>
            </li>
            </ul>
          
          </div>
        </div>

        <p>
          <button class="btn btn-primary" type="button" data-toggle="collapse" data-target="#Stepper-Ans" aria-expanded="false" aria-controls="Servo-Ans">
            Example Answer
          </button>
        </p>
        <div class="collapse" id="Stepper-Ans">
          <div class="card card-body">
            
            <p>This is just one way you can do it!</p>
            <br>
            <pre class="prettyprint" style="max-height:300px;overflow:auto">
              if button_a.is_pressed():
                  # Play a tune
                  music.pitch(200, duration=150, wait=True)
                  # Update current angle
                  currentAngle = currentAngle - stepAngle
                  # Make sure it doesn't turn into a negative number!
                  if currentAngle < 0:
                      currentAngle = 360 + currentAngle
                  # Display a message
                  display.scroll(currentAngle, delay=120, wait=False, loop=False)
                  # Rotate the motor
                  theBoard.stepperMotorTurnAngle(
                      theBoard, currentRotationMotor, angle=-stepAngle)
            </pre>
            <br>
          
          </div>
        </div>

        <p>If you're stuck, you can get the complete script here: <a href="./activity_code/stepper_motor_code.py" download="stepper_motor_code.py" target="_blank"> link</a></p>
        <p>You can also have a play around with the code! Have a think about some of the questions below and see if you can figure them out.</p>
        <ul>
        <li>How can you get the motor to move further when you push the A or B button?</li>
        <li>What types of robots do you think this motor would be good for? What sort of actions?</li>
        </ul>
        <br>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSevenE">
        Let's move the motor!
      </a>
    </div>
    <div id="collapseSevenE" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p style="text-align:center"><span style="color:Red"><b>!!! Make sure your hands are far away from the motor arm! !!!</b></span> </p>
        <p>Try pressing the buttons.</p>
        <p>If you did it the same way as the zero code, button A will increase the angle, and button B will decrease the angle. You can see the angle scrolling across the LEDs, before the arm moves.</p>
        <br>
        <p>Turn off the battery pack. Move the arm a bit, you should be able to move the arm. <b>Keep your hands away</b>, and then turn on the battery pack again. What happens?</p>
        <br>
      </div>
    </div>
  </div>

  

</div>

<br><br>

<!--Comment: This section is markdown again-->

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="Activity6" class="container p-3 my-3 bg-primary text-primary">
<h2>Activity #6</h2>
</div>


<!--Comment: End of html bootstrap -->

<!--Comment: Back to markdown -->

<br>

### How hard did I blow?: A wind speed measuring device!
<br>

Now that you know how to code a motor, let's try making a device that will measure how hard you blow on the microbit, and use the motor to display your 'blow strength level'!

<br>

<!--Comment: End of markdown-->

<!--Comment: Back to html bootstrap -->

<div id="accordion">


  
  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseOneF">
        New Functions
      </a>
    </div>
    <div id="collapseOneF" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>We're going to use a lot of the same code to make our measurement device.</p>

         <p>Download the code with the new functions here: <a href="./activity_code/stepper_motor_loudness_activity_code.py" download="stepper_motor_loudness_activity_code.py" target="_blank"> link</a>.</p>

        <p>This link will download a python file to your computer. </p>
        
        <p>Next, in your python editor click on 'Open' and then select the python file you just downloaded (it's called: stepper_motor_loudness_activity_code.py). The code will load and you will see it on your screen.</p>

        <p>Here there are two functions I've already written for you to use in this activity, and they are on lines 155 to 178. Can you understand what they do?</p>
        
        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          def loudness_to_level(sound_value):
            # give 10 levels of loudness
            return round(sound_value*(10)/256)

          def how_hard_did_i_blow():
              # Play some sound 
              music.pitch(200, duration=150, wait=True)
              sleep(100)
              music.pitch(200, duration=150, wait=True)
              sleep(100)
              music.pitch(200, duration=150, wait=True)

              # Image display!
              display.show(Image.MUSIC_QUAVER)
              sleep(1500)

              # Recording
              loudness = loudness_to_level(microphone.sound_level())

              # Image display to show it has been acquired!
              display.show(Image.YES)
              sleep(500)

              return loudness
        </pre>

        <br>
        <p>'how_hard_did_i_blow()' plays three beeps, then shows a music note image on the microbit display. Once the music note is displayed, you need to blow for at least 2 seconds in the direction of the microbit logo. Once it's done recording, it will show a tick symbol.</p>
        <p>'loudness_to_level()' takes the microphone sound level which will be read as a value of 0 to 256, and will scale it to a value of 0 to 10 so that the motor can show it on your fancy dial!</p>

        <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwoF">
        Edit our code
      </a>
    </div>
    <div id="collapseTwoF" class="collapse" data-parent="#accordion">
      <div class="card-body">

         

        <p>I've added some comments to help you out at lines 203 to 234. Try and look at the previous stepper motor code and see if you can fill in the blanks.</p>

        <pre class="prettyprint" style ="max-height:300px;overflow:auto">
          # Detect if the microbit logo has been touched! This will reset it to zero!
          if pin_logo.is_touched():

              # Play a tune
              

              # Display a message
              

              # Rotate the motor - how much?
              

              # Update current angle - go to zero
              



          # Detect if the button a has been pressed!
          elif button_a.is_pressed():
              
              # Get angle from microphone measurement
              

              # Find the difference so you know how many steps to take


              # Reset currentAngle
              

              # Display a message
              

              # Rotate the motor
        </pre>

        <br>
        <p>If you can't figure it out, you can find the finished code here: <a href="./activity_code/stepper_motor_loudness_code.py" download="stepper_motor_loudness_code.py" target="_blank"> link</a>. But give it a shot first, I believe in you!</p>
        <br> <br>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseThreeF">
        Download our code onto the microbit!
      </a>
    </div>
    <div id="collapseThreeF" class="collapse" data-parent="#accordion">
      <div class="card-body">

        <p> Make sure your battery is turned <b>off</b>!!</p>

        <p>Download the code and transfer it to your microbit by clicking on 'Send to microbit' and following the instructions. If you've got any problems with this you can follow this guide to resolve them: <a href="https://python-editor-2-1-2.microbit.org/help.html?snippets=true" target="_blank">Link here</a></p>

        <br> <br>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFourF">
        Set up the dial
      </a>
    </div>
    <div id="collapseFourF" class="collapse" data-parent="#accordion">
      <div class="card-body">
       
        <p>Take out the dial from the box and place it on top of the base, right up against the motor holder.</p>

        <p><img src="images/LoudnessDial/PutDial.png" class="img-fluid" alt="assemblyImage"></p>

      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseFiveF">
        Zero the arm
      </a>
    </div>
    <div id="collapseFiveF" class="collapse" data-parent="#accordion">
      <div class="card-body">
       
        <p>Make sure the battery pack is turned <b>off</b>.</p>

        <p>Push the motor arm gently so it points to the <b>left</b> so it's over the number 0.</p>

        <p>Press the reset button on the microbit.</p>

        <p><img src="images/LoudnessDial/ZeroArm.jpg" class="img-fluid" alt="assemblyImage"></p>

      </div>
    </div>
  </div>


  <div class="card">
    <div class="card-header">
      <a class="collapsed card-link" data-toggle="collapse" href="#collapseSixF">
        Give it a blow!
      </a>
    </div>
    <div id="collapseSixF" class="collapse" data-parent="#accordion">
      <div class="card-body">
        <p>Turn on the battery pack.</p>
        <p>Press button A. It should beep 3 times and show a little musical note. When you see the musical note, blow at the little red light on the microbit until the image changes to a check mark! The arm should then move to level of how hard you blew on the microphone.</p>
        <p><img src="images/LoudnessDial/Musicnote.jpg" class="img-fluid" alt="assemblyImage"></p>
        <br>
        <p>Good job!</p>
        <br> <br>

      </div>
    </div>
  </div> 

</div>

<br><br>


<br>
<br>



