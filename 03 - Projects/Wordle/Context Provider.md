This document provides a detailed explanation of the `WordProvider` component and its associated functionalities. The context and reducer-based architecture is used to manage the state of a Wordle-like game.

---

## Overview

The `WordProvider` component utilizes the React Context API and the `useReducer` hook to manage the state of a Wordle-like game. It provides state and actions to its child components for managing game logic, such as guessing letters, deleting guesses, and checking words.

### Key Concepts:

1. **Context API**: Provides a way to pass state and dispatch function down the component tree without prop drilling.
2. **Reducer Pattern**: Encapsulates state transitions in a single function (`wordReducer`) based on dispatched actions.
3. **Side Effects**: The `useEffect` hook is used to check the previous row's word when conditions are met.

---

## Code Breakdown

### Context Creation

```tsx
const WordContext = createContext<{
  state: InitialState;
  dispatch: React.Dispatch<Action>;
}>({
  state: initialState,
  dispatch: () => undefined,
});
```

The `WordContext` is created to share `state` and `dispatch` functions throughout the component tree.

### Initial State

```tsx
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

The initial state defines the structure and default values for the game:

- **`wordToGuess`**: The target word to guess.
- **`currentBoard`**: A 6x5 matrix representing the game board.
- **`currentRow`/`currentColumn`**: Track the current position for input.
- **`allowMoreGuesses`**: To check if the cursor is at the last column of any row.
- **`letters`**: Contains **Correct**, **Wrong**, and **Misplaced** letters to help with letter highlighting.
- **`gameStatus`**: Either **inProgress**, **won**, and **lost**.
- **`checkedRows`**: A number array to store the numbers that has already been checked.

### Actions

```tsx
export type Action =
  | { type: "SetWord"; payload: string }
  | { type: "MakeGuess"; payload: string }
  | { type: "DeleteLastGuess" }
  | { type: "CheckLastWord"; payload: string };
```

The actions represent possible state transitions:

- **`SetWord`**: Sets the word to guess.
- **`MakeGuess`**: Adds a guessed letter to the board.
- **`DeleteLastGuess`**: Removes the last guessed letter.
- **`CheckLastWord`**: Compares the user's guess with the target word.

### Reducer Function

The `wordReducer` function manages state transitions based on actions.

#### 1. Set Word

```tsx
case "SetWord": {
  return {
    ...state,
    wordToGuess: action.payload,
  };
}
```

This action updates the `wordToGuess` with the payload.

#### 2. Make Guess

```tsx
case "MakeGuess": {
	const guessedLetter = action.payload;
	const newBoard = state.currentBoard.map((row) => [...row]);
	const currentRow = state.currentRow;
	const currentColumn = state.currentColumn;
	const allowMoreGuesses = state.allowMoreGuesses;
	  
	// Place the guessed letter
	newBoard[currentRow][currentColumn] = guessedLetter;
	  
	// Determine whether to move to the next row or column
	const isEndOfRow = currentColumn === newBoard[currentRow].length - 1;
	
	if (isEndOfRow) {
		return {
			...state,
			currentBoard: newBoard,
			allowMoreGuesses: true,
			currentColumn,
		};
	}
	
	// Check if guesses are allowed
	if (!allowMoreGuesses) {
		return {
			...state,
		};
	}
	
	return {
		...state,
		currentBoard: newBoard,
		currentColumn: currentColumn + 1, // Move to the next column
	};

}
```

This action updates the board with the guessed letter and moves the position forward. If at the last column then no more guesses are allowed.

#### 3. Delete Last Guess

```tsx
case "DeleteLastGuess": {
	const newBoard = state.currentBoard.map((row) => [...row]);
	const currentRow = state.currentRow;
	let currentColumn = state.currentColumn;
	
	// Check if the current column is at the start and no letters are present
	if (currentColumn === 0 && newBoard[currentRow][currentColumn] === "") {
		return state; // Nothing to delete if at the start of the row and the cell is empty
	}
	
	  
	// Adjust the column index to the last filled cell
	if (newBoard[currentRow][currentColumn] === "") {
		currentColumn--; // Move back only if the current cell is empty
	}
	
	  
	// Remove the letter from the board
	newBoard[currentRow][currentColumn] = "";
	  
	return {
		...state,
		currentBoard: newBoard,
		currentColumn: currentColumn > 0 ? currentColumn : 0, // Ensure column index doesn't go negative
	};
}
```

This action removes the last guessed letter and adjusts the cursor position accordingly.

#### 4. Check Last Word

```tsx
case "CheckLastWord": {
	const currentBoard = state.currentBoard;
	const currentRow = state.currentRow;
	const wordToCheck = currentBoard[currentRow].join("");
	const wordToGuess = state.wordToGuess!;
	  
	// Arrays to track feedback
	const wrongLetters = [...state.letters.wrongLetters];
	const correctLetters = [...state.letters.correctLetters];
	const misplacedLetters = [...state.letters.misplacedLetters];
	
	// Create arrays for feedback for this guess
	const guessFeedback = Array(wordToGuess.length).fill("");
	
	// Map to track letter occurrences in the wordToGuess
	const letterCount: { [char: string]: number } = {};
	for (const char of wordToGuess) {
		letterCount[char] = (letterCount[char] || 0) + 1;
	}
	
	// First pass: Check for correct letters in the right position
	for (let i = 0; i < wordToCheck.length; i++) {
		if (wordToCheck[i] === wordToGuess[i]) {
			guessFeedback[i] = "correct";
			letterCount[wordToCheck[i]]--;
			if (!correctLetters.includes(wordToCheck[i])) {
				correctLetters.push(wordToCheck[i]);
			}
		}
	} 
	
	// Second pass: Check for misplaced letters
	for (let i = 0; i < wordToCheck.length; i++) {
		if (
			guessFeedback[i] === "" && // Not already marked as correct
			wordToGuess.includes(wordToCheck[i]) && // Letter is in the wordToGuess
			letterCount[wordToCheck[i]] > 0 // Letter has not been fully used
		) {
			guessFeedback[i] = "misplaced";
			letterCount[wordToCheck[i]]--;
			if (!misplacedLetters.includes(wordToCheck[i])) {
				misplacedLetters.push(wordToCheck[i]);
			}
		}
	}
	 
	
	// Third pass: Mark remaining as wrong letters
	for (let i = 0; i < wordToCheck.length; i++) {
		if (guessFeedback[i] === "") {
			guessFeedback[i] = "wrong";
			if (!wrongLetters.includes(wordToCheck[i])) {
				wrongLetters.push(wordToCheck[i]);
			}
		}
	}
	
	  
	// Check if the word is correct and move to the next state
	const isCorrectWord = wordToCheck === wordToGuess;
	
	return {
		...state,
		letters: {
		correctLetters: correctLetters,
		wrongLetters,
		misplacedLetters: misplacedLetters,
		},
		currentRow: isCorrectWord ? currentRow : currentRow + 1,
		currentColumn: 0,
		allowMoreGuesses: !isCorrectWord,
		gameStatus: isCorrectWord
		? GameStatus.won
		: currentRow + 1 >= currentBoard.length
		? GameStatus.lost
		: GameStatus.inProgress,
		checkedRows: [...state.checkedRows, currentRow],
	};
}
```

This action validates the guessed word. If correct, it updates the game state to "end."
### Provider Component

```tsx
const WordProvider = ({ children }: { children: ReactNode }) => {
  const [state, dispatch] = useReducer(wordReducer, initialState);

  return (
    <WordContext.Provider value={{ state, dispatch }}>
      {children}
    </WordContext.Provider>
  );
};
```

The `WordProvider` initializes the state with the reducer and provides the context to children. 
### Custom Hook

```tsx
const UseWord = () => {
  const context = useContext(WordContext);
  if (context === undefined)
    throw new Error("WordContext was used outside of the WordProvider");
  return context;
};
```

The `UseWord` hook simplifies accessing the `WordContext`.