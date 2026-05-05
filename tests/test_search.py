import pytest
from pathlib import Path
from app.search import Searcher

CORPUS_PATH = Path(__file__).resolve().parent.parent / "data" / "corpus_vn.jsonl"

@pytest.fixture(scope="module")
def searcher():
    return Searcher.from_corpus(CORPUS_PATH)

def test_search_keyword(searcher):
    hits = searcher.search("cloud computing", mode="keyword", top_k=5)
    assert len(hits) == 5
    assert all(h.score > 0 for h in hits)

def test_search_semantic(searcher):
    hits = searcher.search("trí tuệ nhân tạo", mode="semantic", top_k=5)
    assert len(hits) == 5
    assert all(h.score > 0 for h in hits)

def test_search_hybrid(searcher):
    hits = searcher.search("hybrid cloud deployment", mode="hybrid", top_k=5)
    assert len(hits) == 5
    # RRF scores are usually small fractions
    assert all(h.score > 0 for h in hits)

def test_rrf_logic(searcher):
    # Test RRF with specific k
    hits_k60 = searcher.search("test", mode="hybrid", top_k=5, rrf_k=60)
    hits_k100 = searcher.search("test", mode="hybrid", top_k=5, rrf_k=100)
    assert len(hits_k60) == 5
    assert len(hits_k100) == 5
    # Different k should produce different scores (usually)
    assert hits_k60[0].score != hits_k100[0].score
