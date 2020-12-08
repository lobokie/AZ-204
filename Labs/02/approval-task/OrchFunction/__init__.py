# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    outputs = []
    approve = yield context.call_activity("Approval", "Approved")
    reject = yield context.call_activity("Approval", "Rejected")
    
    return [approve, reject]

main = df.Orchestrator.create(orchestrator_function)


# const df = require("durable-functions");

# module.exports = df.orchestrator(function* (context) {
#     const outputs = [];

#     /*
#     * We will call the approval activity with a reject and an approved to simulate both
#     */

#     outputs.push(yield context.df.callActivity("Approval", "Approved"));
#     outputs.push(yield context.df.callActivity("Approval", "Rejected"));

#     return outputs;
# });