# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(name: str) -> str:
    return f"Your project design proposal has been -  {name}!"


# module.exports = async function (context) {
#     return `Your project design proposal has been -  ${context.bindings.name}!`;
# };