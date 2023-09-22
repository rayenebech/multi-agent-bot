from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage,
)
from typing import List


class EmployeeAgent:
    def __init__(self, system_message: SystemMessage, llm) -> None:
        self.system_message = system_message
        self.model = llm
        self.memory_size = 5
        self.init_messages() # method to initialize the stored_messages instance variable.

    def reset(self) -> None:
        self.init_messages()
        return self.stored_messages

    def init_messages(self) -> None:
        self.stored_messages = [self.system_message]

    def update_messages(self, message: BaseMessage) -> List[BaseMessage]:
        self.stored_messages.append(message)
        return self.stored_messages

    def step(self, input_message: HumanMessage) -> AIMessage:
        messages = self.update_messages(input_message)
        output_message = self.model(messages)
        self.update_messages(output_message)
        if len(messages) > self.memory_size + 1:
            self.stored_messages = self.reset()
            self.stored_messages.extend(messages[-self.memory_size:])
        return output_message