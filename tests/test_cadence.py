from datetime import date, timedelta

from pkm_workflow.cadence import edition_for, sections_for


def test_two_modules_rotate_and_sunday_is_weekly():
    monday = date(2026, 9, 7)
    expected = [("research", "ai_practice"), ("builder", "vc"), ("cognition", "github")]
    for offset in range(6):
        day = monday + timedelta(days=offset)
        assert edition_for(day) == "daily"
        assert sections_for(day, "daily") == expected[offset % 3]
    assert edition_for(monday + timedelta(days=6)) == "weekly"
    assert set(sections_for(monday, "weekly")) == {key for pair in expected for key in pair}


def test_sparse_research_days_still_explore_rl_and_deep_learning():
    from pkm_workflow.paper_collection import research_topic
    monday = date(2026, 9, 7)
    assert {research_topic(monday + timedelta(days=7 * n)) for n in range(3)} == {"agents"}
    assert {research_topic(monday + timedelta(days=3 + 7 * n)) for n in range(3)} == {"agents", "rl", "deep_learning"}
