

'''

Algorand smart contracts have three different types of on-chain storage they can utilise: Global storage, Local storage, Box Storage, and Scratch storage.



1. Local Storage
Local storage refers to the storage that is associated with a specific user’s account. Each account can interact with a stateful smart contract and have its own set of key-value pairs stored locally, separate from the global state of the contract.

Size Limitations: Local storage for each account has a maximum size of 16 key-value pairs. Each key and value are both 64 bytes.
Cost: Each key-value pair in local storage consumes part of the account’s minimum balance. Every entry in local storage requires an additional 0.1 ALGO in the minimum balance.
Scope: Data stored in local storage is specific to the user interacting with the contract. This allows for personalized state, which is useful for tracking user-specific data, such as account balances in decentralized applications (dApps) or user settings in a contract.


1. Global Storage
Global storage refers to the storage available to the smart contract itself. This is not tied to individual accounts but is accessible by all users interacting with the contract.

Size Limitations:
Global storage has a maximum size of 64 key-value pairs, where each key and value are both 64 bytes.
This means that the total storage capacity for global state is 64 * 64 bytes for keys and 64 * 64 bytes for values.
Cost:
Each key-value pair stored in the global state increases the minimum balance required for the contract. Every key-value pair costs an additional 0.1 ALGO in the contract's minimum balance.
Scope:
Global storage is accessible to all accounts interacting with the smart contract. It is useful for storing data that is relevant across all users of the contract, such as token supply, governance parameters, or shared settings.




2. Box Storage
Box storage is a newer feature introduced to allow smart contracts to store larger amounts of data by allocating additional storage in “boxes.” Boxes are external storage units that can store more data beyond the global and local storage limitations.

Size Limitations:
Box storage allows smart contracts to allocate boxes of up to 32KB of data each.
Each box is associated with a specific key, and the number of boxes a contract can allocate is flexible but comes with a cost.
Cost:
The cost for using box storage depends on the size of the box and the number of boxes being created. It adds extra transaction fees for creating and accessing boxes, and it affects the minimum balance required by the contract.
Scope:
Boxes allow for much larger storage needs, which can be beneficial for applications that handle large datasets, such as NFTs, metadata, or storing user-specific large objects. Boxes are accessible to the smart contract but can hold more complex or bulk data than the standard key-value storage.



3. Scratch Storage
Scratch storage is temporary storage used during the execution of smart contract logic. It allows contracts to store intermediate values without committing them to global or local storage.

Size Limitations:
Scratch storage is volatile and only exists during the execution of a single transaction or atomic group of transactions. It can store 256 slots, and each slot is 64 bytes.
Cost:
Scratch storage does not incur additional minimum balance or transaction fees since it is not persistent beyond the execution of the transaction.
Scope:
Scratch storage is used for temporary variables, intermediate calculations, or data that is only relevant during a transaction’s execution. It is particularly useful in more complex logic flows where multiple calculations or conditions need to be tracked within the contract’s execution.

'''