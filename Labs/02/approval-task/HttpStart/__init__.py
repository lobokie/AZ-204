# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new(req.route_params["functionName"], None, None)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    return client.create_check_status_response(req, instance_id)


# const df = require("durable-functions");

# module.exports = async function (context, req) {
#     const client = df.getClient(context);
#     const instanceId = await client.startNew(req.params.functionName, undefined, req.body);

#     context.log(`Started orchestration with ID = '${instanceId}'.`);

#     return client.createCheckStatusResponse(context.bindingData.req, instanceId);
# };