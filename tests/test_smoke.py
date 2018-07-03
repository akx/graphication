import pytest
from examples import forcerel, random_doughnut, random_linegraph, random_wavegraph, lastfm_wavegraph

examples = [
    forcerel,
    lastfm_wavegraph,
    random_doughnut,
    random_linegraph,
    random_wavegraph,
]

@pytest.mark.parametrize('example', examples, ids=[e.__name__ for e in examples])
def test_smoke(tmpdir, example):
    tmpdir.chdir()
    example.main()