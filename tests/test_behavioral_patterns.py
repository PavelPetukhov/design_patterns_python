from design_patterns.behavioral import (
    chain_of_responsibility,
    command,
    interpreter,
    strategy,
    iterator,
)


def test_chain_of_responsibility_pattern_example_1():
    content_filter = chain_of_responsibility.ContentFilter(
        [chain_of_responsibility.AdsFilter, chain_of_responsibility.OffensiveFilter])
    filtered_result = content_filter.filter(['filter', 'me', 'bad', 'guy', 'and', 'buy', 'x'])
    print(filtered_result)


def test_chain_of_responsibility_pattern_example_2():
    range_handler = chain_of_responsibility.RangeHandler()
    even_handler = chain_of_responsibility.EvenHandler(range_handler)

    numbers_to_check = [1, 3, 100, 20, -5, -2]
    for number in numbers_to_check:
        even_handler.handle(number)


def test_command_pattern():
    history = command.History()
    history.execute(command.CapitalizeString('string1'))
    history.undo()


def test_interpeter_pattern():
    interpreter_ = interpreter.NonterminalExpression(interpreter.TerminalExpression())
    interpreter_.interpret()


def test_strategy_pattern():
    strategy_ = strategy.Context(strategy.ParticularStrategy1())
    strategy_.business_logic(data=[3, 1, 3])

    strategy_.strategy = strategy.ParticularStrategy2()
    strategy_.business_logic(data=[3, 1, 3])


def test_iterator_patter():
    collection = iterator.CustomCollection(['First', 'Second'])
    print('\n'.join(collection))

