# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

- The difficulties are also buggy as the number of attempts aren't consistent with the difficulty level, For example; Easy was 5, Normal was 7 and Hard was 4.

- The game accepted inputs outside the described limits, and the "Range/Attempts allowed description" under the difficulty bar don't match the actual guesses and allowed attempts left.

- Attempts were counting down incorrectly as when a user had 1 attempt left out of 10 for example, it showed the "Out of attempts" message.

- The "New Game" button doesn't start a new game once its clicked, you have to refresh the app, and the guesses don't refresh as well

--- 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
:- I used Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
:-- Correct AI suggestion: So, my Agent correctly suggested that I `Correct the attempt_limit_map in app.py to assign more attempts to Easy (e.g., 10), medium to Normal (e.g., 7), and fewer to Hard (e.g., 5)`, in order to fix the attempts/difficulty mismatch. And so, I verified its correctness when I implemented that suggestion into that part of app.py and checked the webapp to see if the changes have been applied to the attempts for each difficulty level.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
:- The Agent was misleading when it said to `Update the UI info message to dynamically display the correct range (low to high) instead of hardcoded "1 to 100"`, because the range description is actually meant to tell the user the number range it expects them to guess the numbers from based on the selected difficulty, and not some arbitrary info like "low to high".

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
:- I decided if a bug was really fixed by reloading the webapp and checking to see if there's any difference between what once was and what I just implemented, to verify if it worked the way I wanted it to.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
:- So I ran two tests manually; One to verify the changes made regarding the attempt/difficulty level matching, and the other to make sure that everything resets and restarts once the "New Game" button is clicked on, or the user switches between difficulty levels.

- Did AI help you design or understand any tests? How?
:- Yes it did, as the chat outputs also included suggestions on how to go about testing and the steps to take, to make sure the changes implemented were working as intended.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
:- It's because we weren't using streamlit's session state to store the secret numbers, they were originally just random standalone integers, hence why it refreshed everytime the user submits.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
:- I would say: I think of reruns in the same way you refresh a website, and session state is kind of a 'container' in a sense that you can use to store special values you want across each website refresh, so you don't lose any important info that you might have filled out on the website somewhere before you refreshed it.

- What change did you make that finally gave the game a stable secret number?
:- Used session state to store the secret number

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
:- One thing I definitely look forward to reusing and taking full advantage of, is how to use Copilot Agents more when working on projects or just coding in general. I found it pretty cool to use for the first time in seeing how it can suggest in-line code changes, and its up to you to either keep or ignore the suggestions.

- What is one thing you would do differently next time you work with AI on a coding task?
:- Definitely using Agents more, especially after finding out I can make my own agents by creating a new custom agent using the Command Palette

- In one or two sentences, describe how this project changed the way you think about AI generated code.
:- I think that depending on how exactly you use it(with code suggestions from Copilot Agent and whatnot), it can either speed up and make your workflow more convenient, or it can just be a waste of time reviewing it and could potentially make other parts of the codebase more buggy if not understood and implemented. 
