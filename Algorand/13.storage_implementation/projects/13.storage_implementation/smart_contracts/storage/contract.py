from algopy import ARC4Contract, String, UInt64, Bytes, LocalState, GlobalState
from algopy.arc4 import abimethod  # Use Account from algopy.arc4
import typing as t
from algopy import Box, arc4, Account, op

class Storage(ARC4Contract):
    def __init__(self) -> None:
        # Global storage variables
        self.global_storage1 = GlobalState(String, key="Storage1")
        self.global_storage2 = GlobalState(String, key="Storage2")
        self.global_integer = GlobalState(UInt64, key="IntegerKey")
        self.global_bytes = GlobalState(Bytes, key="ByteKey")

        # Local storage variables (for specific accounts)
        self.local_storage1 = LocalState(String, key="LocalStorage1")
        self.local_storage_int = LocalState(UInt64, key="LocalStorageInt")

        # Box storage
        self.box_a = Box(arc4.StaticArray[arc4.UInt32, t.Literal[20]], key=b"boxA")

    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name

    @abimethod()
    def global_storage_update(self) -> None:
        # Directly assigning new values to global storage variables
        self.global_storage1.value = String("Storage1 Updated")
        self.global_storage2.value = String("Storage2 Updated")
        self.global_integer.value = UInt64(42)
        self.global_bytes.value = Bytes(b"Global Bytes Data")

    @abimethod()
    def local_storage(self, user: Account, new_value: String) -> None:
        # Local storage assignment for a specific account
        self.local_storage1[user] = new_value
        self.local_storage_int[user] = UInt64(100)

    @abimethod()
    def box_storage(self) -> bool:
        # Check if the box exists and then update or set the box storage
        if self.box_a:
            self.box_a.value[2] = arc4.UInt32(40)
        else:
            self.box_a.value = arc4.StaticArray[arc4.UInt32, t.Literal[20]].from_bytes(op.bzero(20 * 4))
        return self.box_a.value[4] == arc4.UInt32(2)
