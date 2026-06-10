from aiogram.fsm.state import StatesGroup, State

class AdminState(StatesGroup):
    broadcasting = State()
    adding_balance_userid = State()
    adding_balance_amount = State()
