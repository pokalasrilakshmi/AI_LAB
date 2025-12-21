## Aim
To implement a **Table-Driven Vacuum Agent** using PyScript that cleans all rooms in a simple vacuum world.

## Introduction
A Table-Driven Agent selects actions by looking up a predefined table based on the **history of percepts**.  
It does not use reasoning or learning and purely relies on stored percept–action mappings.

## Problem Description
The vacuum world consists of two rooms:
- Room A
- Room B  

Each room can be either **Clean** or **Dirty**.  
The agent perceives the room state and performs actions to clean the environment.

## Agent Actions
- **Suck** – Cleans the current room  
- **Left / Right** – Moves between rooms  
- **Exit** – Stops execution when all rooms are clean  

## Working
1. The agent perceives the current room and its condition.
2. The percept is added to the percept history.
3. The agent matches the percept sequence with a lookup table.
4. The corresponding action is executed.
5. The process continues until the agent exits.

## Implementation
- Implemented using HTML and PyScript
- Uses Python classes for environment and agent
- A predefined table maps percept sequences to actions

## Output
The agent cleans all dirty rooms and exits successfully after the task is completed.

## Conclusion
This experiment demonstrates the working of a **Table-Driven Agent** and helps understand percept history and action selection in Artificial Intelligence.





SCREENSHOT:

<img width="1091" height="512" alt="image" src="https://github.com/user-attachments/assets/2da997df-3ca9-4858-9f5f-9c6ecf616a44" />
