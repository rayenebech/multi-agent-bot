
from typing import Dict
import json

def load_database(database_path: str) -> Dict:
    """
    Load a database from a json file.
    """
    with open(database_path, "r", encoding="utf-8") as f:
        database = json.load(f)
    return database


def build_prompt_from_database(database_path : str, human_name: str) -> str:
    """
    Build a prompt from a database dictionary.
    """
    database = load_database(database_path)
    if not database:
        raise ValueError("Database is empty")
    agent_names = [agent.get("first_name") for agent in database["agents"]]
    company_name = database["company_name"]
    prompt = f"You are a multi-agent chatbot. {human_name} is an engineer working at {company_name}. " + " ".join(agent_names[:-1]) + f" and {agent_names[-1]} are {len(agent_names)} other people working at {company_name} company. You will play the role of " + " or ".join(agent_names) + f" to have a conversation with the human {human_name}. "
    prompt += f"Your task is to help {human_name} to respond well to an incident. You will have a natural conversation with {human_name}. According to your personality, you will interact with {human_name}'s messages.\n\n"
    prompt += f"The incident response process can be divided into four phases: detection, analysis, response and recovery. You will have to identify the phase and choose the best role to play.\n\n"
    prompt += "Here is a description of each role:\n\n"
    for agent in database["agents"]:
        prompt += f"->{agent.get('first_name')}: {agent.get('role')} at {company_name}. {agent.get('bio')} \n"
        prompt += "Some of the directives include:\n"
        for directive in agent.get("directives"):
            prompt += f"- {directive}\n"
        prompt += "\n"
    prompt += f"You should write short and human-like answers. Do not introduce yourself. One role should not dominate the conversation. The human {human_name} should be able to interact with you in a natural way.\n\n"
    return prompt
