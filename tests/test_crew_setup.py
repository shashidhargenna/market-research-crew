from crew.crew import market_research_crew


def test_crew_initialization():
    assert market_research_crew is not None
    print("\nCrew Initialized Successfully")


def test_crew_agents():

    assert len(market_research_crew.agents) == 3

    print("\nAll Three Agents Registered Successfully")


def test_crew_tasks():

    assert len(market_research_crew.tasks) == 3

    print("\nAll Three Tasks Registered Successfully")


def test_crew_process():

    assert market_research_crew.process is not None

    print("\nCrew Process Configured Successfully")