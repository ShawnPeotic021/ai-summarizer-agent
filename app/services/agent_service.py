from rich import print_json

from app.core.graph_builder import build_graph,Context

transcript1 = '''
    Agent: Hi Emma, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Sorry, just cancel it for me.
    Agent: sure
    '''
transcript2 = '''
    Agent: Hi Jane, how are you finding your Basic Plan?
    Customer: It’s fine, but I wish it had more storage.
    Agent: We have a Plus Plan with 200GB more for $5 extra per month.
    Customer: Ok, Sounds good.
    '''
transcript3 = '''
    Agent: Hi Thomas, I see you have the Premium Package.
    Customer: yes, but I want to cancel my service.
    Agent: I'm sorry to hear that. May I offer you free access for 3 months?
    Customer: Hold on.
    Agent: Sure.
    Customer: Sorry, I still want to cancel it.
    Agent: Sure.
    '''

def run_agent():
    # Initialize agent
    summarizer_agent = build_graph()
    config = {"configurable": {"thread_id": "1"}}

    # Run agent
    # `thread_id` is a unique identifier for a given conversation.

    response = summarizer_agent.invoke(
        {"transcript": transcript3},
        config=config,
        context=Context(user_id="1")
    )

    clean_summary = response.get("validated_summary", {})["summary"]
    print("\n")
    print("✅ Final structured result:")
    print_json(data=clean_summary,indent=2)



