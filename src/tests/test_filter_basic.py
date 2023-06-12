import pytest

from filter_service import FilterServiceBasic, Rules


@pytest.mark.parametrize(
    "rules, text, expected_result",
    [
        (["text to include"], "this is input test with some text to include.", True),
        (["text to include"], "this is input test with some text to includ.", False),
        (["text to include", "something else"], "this is something else", True),
        (["text to include", "something else"], "Nothing else here", False),
        ([], "Try to find something here", False),
        (["BIG RULES"], "i seek for big rules", True),
        (["small rules"], "i seek for small rules", True),
    ],
)
def test_service_basic_rules(rules, text, expected_result):
    rules = Rules(include=rules)
    service = FilterServiceBasic(rules)

    result = service.handle(text)
    if expected_result:
        assert result == text
    else:
        assert result is None
