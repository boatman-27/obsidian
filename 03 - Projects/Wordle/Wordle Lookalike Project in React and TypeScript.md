#project 
This document provides an explanation of a Wordle lookalike project built using React and TypeScript. The project replicates the gameplay of the popular word-guessing game Wordle, including features such as a grid-based guessing system, letter validation, and game completion logic.

---

## Overview

The Wordle lookalike project is designed as a React application written in TypeScript for type safety and improved development experience. The game allows players to guess a hidden word by entering letters into a 6x5 grid, receiving feedback on each guess. Players aim to guess the correct word within six attempts.

### Key Features

1. **Grid-based Gameplay**: Players interact with a grid where they can input letters to form guesses.
2. **State Management**: The game uses the React Context API and the `useReducer` hook to manage state.
3. **Feedback Mechanism**: Letters are color-coded based on their correctness:
    - Green: Correct letter in the correct position.
    - Yellow: Correct letter in the wrong position.
    - Gray: Incorrect letter.
4. **Endgame Logic**: Players win by guessing the word correctly or lose after six incorrect attempts.
5. **TypeScript Integration**: Strong type definitions enhance code reliability and readability.

---

## Project Structure
### Core Components

1. **Board**:
    
    - Displays the 6x5 grid for letter input.
    - Dynamically updates based on user interactions.
2. **Keyboard**:
    
    - Provides an on-screen keyboard for entering letters.
    - Disables keys for letters already guessed.
3. **Tile**:
    - Represents individual cells in the grid.
    - Changes color based on the feedback for guessed letters.

---
## State Management

### WordContext [[Context Provider]]

The `WordContext` is implemented using React's Context API. It provides global state and dispatch functions to manage game logic.

```tsx
const WordContext = createContext<{
  state: InitialState;
  dispatch: React.Dispatch<Action>;
}>({
  state: initialState,
  dispatch: () => undefined,
});
```

### Reducer Function

The `wordReducer` handles state transitions based on dispatched actions:

- **SetWord**: Sets the target word for the game.
- **MakeGuess**: Adds a guessed letter to the grid.
- **DeleteLastGuess**: Removes the last entered letter.
- **CheckLastWord**: Validates the guessed word against the target word.

---

## Gameplay Logic

1. **Input Handling**:
    
    - Players use the keyboard or on-screen buttons to input letters.
    - Input is validated to ensure it adheres to game rules.
2. **Feedback**:
    
    - After each guess, the grid updates to show feedback for each letter.
    - Feedback is color-coded for clarity.
3. **Win/Lose Conditions**:
    
    - The game ends when the player correctly guesses the word or exhausts all attempts.

---
## TypeScript Integration

TypeScript is used throughout the project to ensure type safety. Key types include:

```ts
// Define the initial state structure
export interface InitialState {
	wordToGuess: string | null;
	currentBoard: string[][];
	currentRow: number;
	currentColumn: number;
	allowMoreGuesses: boolean;
	letters: {
		correctLetters: string[];
		wrongLetters: string[];
		misplacedLetters: string[];
	};
	gameStatus: GameStatus;
	checkedRows: number[];
}
```

---
## Future Enhancements

1. **Multiplayer Mode**: Allow two players to compete in guessing words.
2. **Word Database**: Use a dynamic word list sourced from an external API.
3. **Accessibility Improvements**: Enhance keyboard navigation and screen reader support.
4. **Mobile Optimization**: Improve responsiveness and usability on smaller screens.

---
