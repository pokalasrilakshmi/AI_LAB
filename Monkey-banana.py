def monkey_banana(): 
    state = {"monkey": "door", "box": "window", "banana": "middle", "has": False} 
    print("Initial State:", state) 
    state["monkey"] = "window" 
    print("\nStep 1: Monkey walks from door to window") 
    print("State:", state) 
    state["box"] = "middle" 
    print("\nStep 2: Monkey pushes box from window to middle") 
    print("State:", state) 
    state["monkey"] = "middle" 
    print("\nStep 3: Monkey walks to middle (climbs box)") 
    print("State:", state) 
    state["has"] = True 
    print("\nStep 4: Monkey grabs the banana!") 
    print("State:", state) 
    print("\nGoal Achieved: Monkey has the banana!") 
monkey_banana()