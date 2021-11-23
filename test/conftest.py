from litetable import LiteTable
import pytest


@pytest.fixture
def lt(list_of_dicts):
    return LiteTable(list_of_dicts)


@pytest.fixture
def lt_col_names():
    return LiteTable(
        [
            {
                'sum': 1,
                '% of total': 0.1
            },
            {
                'sum': 2,
                '% of total': 0.2
            },
            {
                'sum': 3,
                '% of total': 0.3
            }
        ]
    )


@pytest.fixture
def lt_c2_sum_c1():
    # Result of
    # dt('select c2, sum(c1) as sum_c1 from :this group by c2 order by c2')
    return LiteTable([
        {
            'c2': 1,
            'sum_c1': 5
        },
        {
            'c2': 2,
            'sum_c1': 4
        },
        {
            'c2': 3,
            'sum_c1': 3
        },
    ])


@pytest.fixture
def list_of_dicts():
    data = [
        {
            'c1': 1,
            'c2': 2,
            'c3': 3,
        },
        {
            'c1': 1,
            'c2': 3,
            'c3': 2,
        },
        {
            'c1': 2,
            'c2': 1,
            'c3': 3,
        },
        {
            'c1': 2,
            'c2': 3,
            'c3': 1,
        },
        {
            'c1': 3,
            'c2': 1,
            'c3': 2,
        },
        {
            'c1': 3,
            'c2': 2,
            'c3': 1,
        },

    ]
    return data
