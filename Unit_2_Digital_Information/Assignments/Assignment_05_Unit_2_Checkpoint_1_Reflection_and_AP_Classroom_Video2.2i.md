## AP Computer Science Principles - Unit 2, Assignment 1 - AP Classroom Video 2.1i and Binary Exercises
Due: Tuesday, October 14th 2025

### AP Classroom:

Watch the entirety of AP Classroom Video 2.2 - Video 1.  As you watch, take notes, and write down questions.

### Unit 2 Checkpoint 1 Reflection:

1. Create a file in your Assignments folder titled, `LastNameFirstInitial_U2_CP1_Binary_Overflow_Errors_Roundoff_Errors_Reflection.md`.

2. Copy/paste the code at the bottom of this assignment.

3. For each question, respond to each of the following prompts.
   * What answer choice(s) did you select?  **Write out the complete answer choice(s).**
   * What answer choice(s) were correct? **Write out the complete answer choice(s).**
   * If you answered **correctly**, identify one **incorrect** answer choice and explain the error in reasoning that could have led someone to select that answer choice.
   * If you answered **incorrectly**, explain your own own error in reasoning and justify why the correct answer choice is correct.

**Example 1/**

> ## Question 1/ An online store uses 6-bit binary sequences to identify each unique item for sale.  The store plans to increase the number of items it sells and is considering using 7-bit binary sequences.   Which of the following bet describes the result of using 7-bit binary sequences instead of 6-bit binary sequences?
> * My answer choice was C, 2 times as many items can be uniquely identified.
> * The correct answer choice was C, 2 times as many items can be uniquely identified.
> * Someone may have incorrectly selected A, 2 more items can be uniquely identified.  Their error in reasoning might have been misunderstanding the rule that when you add a bit, the number of unique sequences doubles.  They might have thought that instead of doubling it increases by 2.

**Example 2/**

> ## Question 2/ Each student that enrolls at a school is assigned a unique ID number, which is stored as a binary number.  The ID numbers increase sequentially by 1 with each newly enrolled student.  If the ID number assigned to the last student who enrolled was the binary number 1001 0011, what binary number will be assigned to the next student who enrolls?
> * My answer choice was C, 1101 0100
> * The correct answer choice was A, 1001 0100
> * My error in reasoning was that I didn't pay close attention to the first four digits.  I knew that the last four digits had to be 0100, because 0100 is the next binary number after 0011, but if I had looked at the first four digits as well, I would have realized that the correct answer choice was A, 1001 0100.

4. Commit your progress.  Remember to write an appropriate commit message.  For example, *"Completed unit 2 checkpoint 1 reflection."*

```markdown
# Reflection - Unit 2, Checkpoint 1, Binary, Overflow Errors, and Roundoff Errors

## Question 1/ An online store uses 6-bit binary sequences to identify each unique item for sale.  The store plans to increase the number of items it sells and is considering using 7-bit binary sequences.   Which of the following bet describes the result of using 7-bit binary sequences instead of 6-bit binary sequences?

## Question 2/ Each student that enrolls at a school is assigned a unique ID number, which is stored as a binary number.  The ID numbers increase sequentially by 1 with each newly enrolled student.  If the ID number assigned to the last student who enrolled was the binary number 1001 0011, what binary number will be assigned to the next student who enrolls?

## Question 3/ Which of the following can be represented by a single binary digit. **Select two answers**

## Question 4/ A shopping app uses 7-bit binary sequences to represent data. For example, the binary sequence, 0011001 is used to represent the price, 25 dollars.  A user places two items in their shopping cart.  One item costs 80 dollars.  The other item costs 50 dollars.  What will happen when the app tries to calculate the cost of the two items?

## Question 5/ ASCII is a method of encoding characters in which a decimal number is used to encode each character.  For example 'A' is rpersented by the decimal number, 65.  A partial list of ASCII values and their corresponding characters are displayed in the table below.  Which character corresponds to the binary sequence, 110001?

## Question 6/ Program A uses 16 bit binary sequences to store unique ID numbers. Program B uses 32-bit binary sequences to store unique ID numebrs.  Which of the following best describes the relationship between the number of unique ID's that can be stored by program B compared to program A?

## Question 7/ In a video game, a user can create up to 12 custom characters, each of which can be references using a unique binary sequence.  What is the minimum number of bits required to represent up to 12 custom characters

## Question 8/ Which of the following types of data can be represented with a binary sequence?

## Question 9/ Which of the following statements about overflow and roundoff errors is true?

## Question 10/ A bank account has a balance of 950 million dollars.  After an additional 100 million is deposited, the balance of the bank account displays a negative number.  What most likely explains the bank error?

## Question 11/ What is the effect of appending two 0's to the end of a binary number? For example, converting 1011 to 101100.

## Question 12/ Consider the following values: Binary 11000, Binary 10101, Decimal 20, Decimal 30.  Which of the following correctly orders the values from least to greatest?

## Question 13/ Which of the following best explains how a video is stored by a computer?
```

