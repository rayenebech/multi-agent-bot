# Incident Response Simulation

## Overview

This repository contains code for an Incident Response Simulation tool. The tool simulates incident response scenarios and provides a conversational interface for users to interact with a multiple AI agent.

## Features

- Simulate incident response scenarios.
- Engage in conversations with an AI agent.
- Display AI agent responses in a user-friendly interface.
- Customizable system prompts.

## Prerequisites

Before running the code, make sure you have the following installed:

- Python 3.8 or higher
- Required Python packages listed in `requirements.txt`
- An OpenAI API key (set as an environment variable)

## Configuration

- multi-aagets.py: This is the main application script. You can customize the behavior, chat model, and application flow within this file.

- helpers.py: Contains functions for building prompts from a database or other sources. You can modify this file to change how prompts are generated.

- agent.py: Defines the behavior of the AI agent. You can customize the agent's responses and logic in this file.
