# AP Computer Science Principles
Monday, October 27th 2025

### Introduction to Functions
<table>
  <tr>
    <td markdown>
      <b>DO NOW:</b><br><br>
      <b>If you need a laptop, remember to exchange your student ID for a laptop as you enter the room.</b><br><br>
      1. Navigate to <a href = https://academy.cs.cmu.edu/>CMU Graphics</a>, and sign in.<br>
      2. Click the "Sandbox" button.<br>
      3. Start a new file.<br>
      4. Copy/Paste the following code into the sandbox, and click the green "Run" button.<br><br>
<pre><code># Function Definition:
def draw_house(left, top):
  Rect(left, top, 50, 50, fill='yellow', border='black')
  Polygon(left-10, top + 10, left + 60, top + 10, left + 25, top - 25, fill = 'brown', border = 'black')
  Rect(left + 20, top + 20, 20, 30, fill = 'tan', border = 'black')
  Circle(left + 26, top + 35, 3)
# Function Call(s):
draw_house(175,175)</code></pre>
      5. Start exploring!
      <ul>
        <li>What happens when you run the code?
        <li>On line 8, try changing the arguments to different values and run the code again.  What happens?  What might these arguments control?</li>
        <li>Copy/paste <code>draw_house(175,175)</code> to a new line, try changing the arguments, and run the code again.  What happens this time?  What do you think will happen if you copy/paste <code>draw_house()</code> a third time with new property values?</li>
        <li>In general, what do you think <code>draw_house()</code> accomplishes?</li>
        <li>Try deleting lines 1 through 6, and run the code again.  What happens? Why might this have happened?</li>
      </ul>
      <b>Be prepared to share your responses.</b> 
   </td>
  </tr>
</table>

**AIM:** How can we define and call our own functions in CMU Graphics?

**ANCHOR SKILL(S) AND POWER STANDARD(S):** 

 - [ ] <ins>TYS61XT.2</ins>: Apply computational thinking to a variety of tasks.
 - [ ] <ins>TYS61XT.3</ins>: Code using appropriate logic and syntax.
 
**SUCCESS CRITERIA:**
- [ ] I know the essential ingredients of functions and function calls.
- [ ] I can write-student defined functions that draw images composed of a few shapes.
- [ ] I can call student-defined functions.

**AGENDA:**

1. Construction
2. Functions
    * All About Functions
    * Function Definition Syntax:
     ```python
     def function_name(parameter_1, parameter_2, etc.):
       # Body: 
       # -code to be executed every time the function is called
       # -always indented
       # -return (the data the function outputs to the program) (OPTIONAL)
     ```
    * Function Call Syntax:
     ```python
     function_name(argument_1, argument_2, etc.)
     ```
3. Planting Flowers
    * Petals
    * Center
    * Stem
    * Leaves
4. Check for Understanding

**HOMEWORK:** 

[AP CSP - Unit 3, Assignment 2 - Interactive Image Task Define Stage and My First Function Code](https://github.com/MrJSwotinsky/AP_Computer_Science_Principles_2025_2026/blob/main/Unit_3_Functions_Mouse_Events_and_Conditionals/Assignments/Assignment_02_Interactive_Image_Task_Define_Stage_and_My_First_Function_Code.md)
