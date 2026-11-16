from crew.agents import researcher, analyst, writer


def test_researcher_agent():
    assert researcher is not None
    assert researcher.role
    print("\nResearcher Agent Created Successfully")


def test_analyst_agent():
    assert analyst is not None
    assert analyst.role
    print("\nAnalyst Agent Created Successfully")


def test_writer_agent():
    assert writer is not None
    assert writer.role
    print("\nWriter Agent Created Successfully")