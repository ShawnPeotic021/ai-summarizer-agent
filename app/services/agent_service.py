from rich import print_json

from app.core.graph_builder import build_graph,Context

def run_agent():
    # Initialize agent
    summarizer_agent = build_graph()

    transcript = '''
        Agent: Hi Emma, how are you finding your Basic Plan?
        Customer: It’s fine, but I wish it had more storage.
        Agent: We have a Plus Plan with 200GB more for $5 extra per month.
        Customer: That sounds reasonable. Let’s upgrade to the Plus Plan.
        '''

    config = {"configurable": {"thread_id": "1"}}

    # Run agent
    # `thread_id` is a unique identifier for a given conversation.

    response = summarizer_agent.invoke(
        {"transcript": transcript},
        config=config,
        context=Context(user_id="1")
    )

    clean_summary = response.get("validated_summary", {})
    print("✅ Final structured result:")
    print_json(data=clean_summary,indent=2)



"""
Agent: Hi Sarah, I see you have the beginner Package.
Customer: yes, but I want to cancel my service.
Agent: I'm sorry to hear that. May I offer you free access for 3 months?
Customer: That sounds good.


Agent: Hi Emma, how are you finding your Basic Plan?
Customer: It’s fine, but I wish it had more storage.
Agent: We have a Plus Plan with 200GB more for $5 extra per month.
Customer: That sounds reasonable. Let’s upgrade to the Plus Plan.
"""