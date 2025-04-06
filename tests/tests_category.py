import pytest
from main import Category
from tests.tests_product import sample_product


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Category Description", [sample_product])


def test_category_creation(sample_product, sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Test Product"


def test_category_counts(sample_product, sample_category):
    assert Category.category_count == 1
    assert Category.product_count == 1
    category2 = Category("Test Category 2", "...", [sample_product, sample_product])
    assert Category.category_count == 2
    assert Category.product_count == 3
