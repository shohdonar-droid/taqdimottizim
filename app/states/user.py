from aiogram.fsm.state import StatesGroup, State

class OrderState(StatesGroup):
    choosing_service = State()
    entering_topic = State()
    entering_requirements = State()
    uploading_file = State()
    confirming = State()
    
class PaymentState(StatesGroup):
    uploading_receipt = State()
    entering_amount = State()

class AIChatState(StatesGroup):
    chatting = State()
