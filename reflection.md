# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- when run the app.py, I typed the number, it always show go lower, never show go higher. Second when you run out of attempt, if you want to restart a new game, it won't allow you to start a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Claude on this project, I told them what bugs i found in the program, and ask AI to show me the related code there, and ask AI what wrong with the code that lead to the issues that I found.
- AI suggest that orignal code is compare string to integer, thats why it always so to go lower, AI give a example that if guess = "75" and we have "42" so it compare "7" and "4" alphabetically.
- After i fix the first bug, the program still go lower, so i ask the AI , and AI said everything should run smoothly. But when i point out the bug again it go through the code again, and it said it found out the bug that i found.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I found a bug, and i will ask AI which set of function will affect the part that i mentioned, and I will use AI to help me to fix the bug, and I will use AI to explain why the code were wrong, and how should i fix it, or ask AI to give me recommedation to fix the bug.
- I ran it manual, after I fix the bug, I will re-run the program to see if the bug still here or not.
- Yes AI also help me to design  a test to test the program, i told AI use my app.py and logic_utils as a context for the program, and let AI to see what the function we need to test and how we can test it.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?


- Every time i click a button or type something in the program, the app.py script re-runs from the beginning, so in the original version, random.randint() was called unconditionally. Thats why teh brand new secret number was generated every time
- I will tell them that we can imagine a web page which will refreshes itself everytime when you click a button and all variables will reset to zero.
- I change random.randint(), so the new scret number only generated when the game is brand new or when the diffculty change.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I would love to read to code first, when I see something is weird to me, I will mark it down first, then I will let AI to help me to understand the project logic, to make sure i understand what the program does.
- I will change the way that I told AI I found a bug, because the AI will help you fix the bug without explainning what they change and why that is correct, I will try to tell the AI where is the bug and told AI  my solution, and AI could assisit me to write the code and test it.
This project show me AI is a tool to assist/support me to do my job. AI is not the answer of all code. 
