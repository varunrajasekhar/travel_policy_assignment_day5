"""Travel-policy coordinator and three specialist Deep Agent workers."""
from deepagents import (
    GeneralPurposeSubagentProfile, HarnessProfile,
    create_deep_agent, register_harness_profile,
)
from mcp_tools import mcp_search_travel_knowledge

# Match the training demo: disable the automatic general-purpose worker.
register_harness_profile("ollama", HarnessProfile(
    general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)
))

# TODO 6: write each specialist's prompt. Require MCP retrieval before
# policy conclusions, citations, scope boundaries, and no invented rules.
TRANSPORT_PROMPT = "TODO 6: airfare and ground transportation specialist"
STAY_MEALS_PROMPT = "TODO 6: lodging and meals specialist"
EXCEPTIONS_PROMPT = "TODO 6: exceptions and approvals specialist"

# TODO 7: build three dictionaries, each with name, description,
# system_prompt, and tools=[mcp_search_travel_knowledge]. Required names:
# transport-agent, stay-meals-agent, exceptions-agent.
SUBAGENTS = []

# TODO 8: coordinator delegates to relevant specialists, passes the complete
# question and known facts, combines evidence, retains citations and missing
# information, and does not retrieve policy directly. Exceptions questions
# also need the relevant category specialist when category rules matter.
COORDINATOR_PROMPT = "TODO 8: write the coordinator instructions"

def build_agent(model):
    # TODO 9: create_deep_agent(model=model, tools=[],
    # subagents=SUBAGENTS, system_prompt=COORDINATOR_PROMPT).
    raise NotImplementedError("TODO 9: build the coordinator")
