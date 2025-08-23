**FromOceanToPlate** is a decentralized supply chain application that brings transparency to the journey of seafood — from the moment it is caught, all the way to when it reaches your plate. This DApp ensures accountability and trust across all stakeholders: licensed fishermen, processing companies, and distributors.

This is my **Bachelor Thesis Project**, aiming to demonstrate how blockchain technology can revolutionise food traceability and integrity.

---
## Tech Stack

- **Frontend**: React.js
- **Backend**: Solidity Smart Contracts
- **Blockchain Simulation**: Ganache (for local Ethereum development)
- **Ethereum Tools**: MetaMask, Truffle/Hardhat (optional for deployment/testing)

---
## Features
- **Licensed Fishermen Only**: Items can only be added by verified fishermen via a licensing system.
- **Add & Track Seafood**: Each item is uniquely identified and stored with length, weight, quantity, and more.
- **Processing Stage**: Items can be marked as processed by a predefined processing company.
- **Distribution Stage**: Processed items can be marked as distributed by a predefined distributor.
- **Purchase System**: Buyers can purchase distributed items (with price scaling logic and bulk discounts).
- **Audit Trail**: Each item retains its full history including timestamps and handling entities.
- **Data Access**: Public functions to retrieve all added items and purchase records.

---
## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/boatman-27/FromOceanToPlate
cd FromOceanToPlate
```

### 2. Download Ganache
Visit [Ganache Download](https://archive.trufflesuite.com/ganache/) to download and install the appropriate version of Ganache for your operating system.

### 3. Install Truffle
Install Truffle globally using npm:
```bash
npm install -g truffle
```

### 4. Link Project to Ganache
To link your Truffle project to Ganache:
Follow this guide: [How to link a Truffle project to Ganache](https://archive.trufflesuite.com/docs/ganache/how-to/link-a-truffle-project/)

### 5. Install MetaMask
Install the MetaMask browser extension from [https://metamask.io/](https://metamask.io/), create a wallet (or import one), and connect it to the local blockchain provided by Ganache.

### 6. Compile & Deploy Smart Contracts
In `smartContracts` directory run:
```bash
truffle compile
truffle migrate
```

### 7. Run the React Frontend
Install dependencies and start the app:
```bash
cd fromOceanToPlate
npm install
npm run dev
```

---
## Smart Contracts Overview
- ### AddItems.sol
	- This contract manages seafood items through their supply chain lifecycle: **addition**, **processing**, **distribution**, and **purchase**.
	- **Key Features**
		- **Item Addition**
		    - Only licensed fishermen (checked via `License` contract) can add items.
		    - Each item has type, species, length, weight, quantity, and a calculated price.
		    - A unique `itemId` is generated for each item.
		- **Processing & Distribution**
		    - Items are marked as `processed` and `distributed` via separate functions.
		    - Ownership is updated to designated processing (`pCom`) and distribution (`dCom`) addresses.
		- **Purchase**
		    - Buyers can purchase items if:
		        - They’re not the original holder.
		        - The item is both processed and distributed.
		        - Sufficient quantity exists.
		- **Events**
		    - `Add`: Emitted when an item is added.
		    - `Purchase`: Emitted when an item is purchased.
		- **Data Access**
		    - `getAllItems()`: Returns all active items.
		    - `getAllPItems()`: Returns all purchased item records.
		    - `getItemsCount()`: Returns total items count.
	- **Structs**
		- `ItemsStruct`: Metadata for each item, including lifecycle states.
		- `PurchasedItemsStruct`: Records of completed purchases.
- ### License.Sol
	- This contract manages **licenses for fishermen** by allowing the contract owner to grant or revoke permissions.
	- **Key Features**
		- **Ownership**
		    - Only the contract deployer (owner) can manage licenses.
		- **License Management**
		    - `grantLicense(address)`: Adds a new fisherman to the licensed list.
		    - `revokeLicense(address)`: Removes a fisherman’s license.
		- **Validation**
		    - `hasLicense(address)`: Returns `true` if the address is licensed.
		- **Tracking**
		    - `getLCount()`: Returns the total number of active licenses.
	- **Internal Utilities**
		- `isAddressInArray()`: (Implicit) Used to check if an address is already licensed.
		- `removeElement()`: Removes a specific address from the license list by replacing it with the last one.
- ### Transactions.Sol
	- **Key Features**
		- **Transaction Logging**
		    - `addToBlockchain(sender, receiver, amount, message, keyword)`: Logs a transaction with metadata and emits a `Transfer` event.
		- **Event Emission**
		    - `Transfer`: Triggered for every new transaction.
		- **Data Retrieval**
		    - `getAllTransactions()`: Returns an array of all transactions.
		    - `getTransactionCount()`: Returns the number of logged transactions.
	- **Stored Transaction Data**
		- `sender` and `receiver` addresses
		- `amount` transferred
		- `message`
		- `timestamp`
		- `keyword` (for gif)

---
### Items Context Overview (`ItemsContext.jsx`)
- **Context-based Ethereum smart contract integration** for managing marketplace items in a React app.
- **Initializes an Items smart contract** instance using `ethers.js` and provides interaction methods across the app.
- **Core functions provided via context:**
    - `addItemToMarket`: Adds a new item to the blockchain, after verifying the user's license.
    - `getItems`: Retrieves and structures all item data from the smart contract.
    - `processItem`: Allows a designated processing address to process an item and logs the transaction.
    - `distributeItem`: Allows a designated distribution address to distribute an item and logs the transaction.
    - `buyItem`: Enables users to purchase a portion of an item, transferring funds and calling smart contract functions.
- **Handles ETH transfers manually** using `ethereum.request({ method: "eth_sendTransaction" })` for precise control.
- **Integrates with**:
    - `LicenseContext` to check user license status.
    - `TransactionsContext` to log actions (e.g. purchases, processing, distribution).
- Uses `ethers.utils.parseUnits(..., "gwei")` to compute transaction values accurately.
- Built-in **role-based access control** for processing and distribution actions using hardcoded Ethereum addresses.
- Includes **basic error handling and validation**, such as preventing users from buying their own items.

### License Context Overview (`LicenseContext.jsx`)
- **Context wrapper for interacting with the License smart contract** using `ethers.js` and React hooks.
- Initializes the contract once on mount and stores the instance in state using `useEffect`.
- **Core features exposed through context:**
    - `checkUserLicense(address)`: Checks if a given Ethereum address holds a valid license.
    - `grantLicense(address, ownerAddress)`: Allows the contract owner to grant a license to a user.
    - `revokeLicense(address, ownerAddress)`: Allows the contract owner to revoke a user’s license.
- Automatically connects to MetaMask via `eth_requestAccounts`.
- Wraps contract logic in error-handling blocks to ensure graceful failure.
- **Validates license status before granting or revoking**, preventing duplicate or invalid actions.
- Integrates seamlessly with other contexts like `ItemsContext` for license-dependent features (e.g. posting items).

### Transactions Context Overview (`TransactionsContext.jsx`)
- **Manages all logic related to sending and tracking Ether transactions** through the Transactions smart contract using `ethers.js`.
- Connects to MetaMask on load via `eth_requestAccounts`, then instantiates a contract with the user's signer.
- **Main features exposed via context:**
    - `getAllTransactions()`: Fetches all past transactions from the contract and formats them into readable objects.
    - `transferEther(transferData)`: Sends Ether from the user to another address and logs the transaction on-chain.
- Uses `localStorage` to cache the transaction count between sessions for quick lookup.
- **Automatically checks for wallet connection** using the `isWalletConnected()` service on mount.
- Stores and updates `transactionsCount`, refreshing on successful transactions.
- Formats timestamps and Ether amounts into human-readable values.
- Ensures contract is initialized and available before any transaction logic is run.
- Exposes `transactionsContract` instance for deeper integrations.
---
## License
This project is licensed under the MIT License. Feel free to use it as a learning reference or extend it for your own supply chain ideas.

---
## Acknowledgements
- Ganache – Personal blockchain for Ethereum development.
- Academic supervision at **German University of Technology in Oman (GUtech)**.