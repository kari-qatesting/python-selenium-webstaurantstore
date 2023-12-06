from selenium.webdriver import Keys


def test_landing_page(py):
    py.visit("https://www.webstaurantstore.com")
    assert py.should().contain_title("WebstaurantStore: Restaurant Supplies & Foodservice Equipment")
    assert py.getx("(//nav)[1]").should().have_attr("aria-label", "primary navigation")

def test_product_search(py):
    py.visit("https://www.webstaurantstore.com")
    py.getx("(//input[@name='searchval'])[1]").type("Air Fryer", Keys.ENTER)
    assert py.should().contain_title("Air Fryer")
    assert py.getx("//h1[contains(., 'Results for:')]/span[contains(., 'air fryer')]").should().be_visible()
    py.getx("(//span[contains(@data-filter-content, 'filter-list__content') and text()='Entry Level'])[2]").click()
    py.getx("//span[contains(., 'TurboChef Fire Black')]").click()

    # If I were employed in your organization, one step I would take to make the code more reusable
    # is by developing custom functions that handle product data validation.
    # Take a look at the following method "verify_product_id()".
    assert verify_product_id(py, "532FIREBLK", "//span[@class='item-number']/span[last()]")

def verify_product_id(py, p_id: str, xpath: str):
    return py.getx(xpath).should().contain_text(p_id)
    # This will return a boolean value of either True or False.
    # This will be placed following an assertion declaration, rendering this test step passing or failing.
    # Since WebstaurantStore uses C# as it's language for development,
    # this can also be implemented in a similar fashion.

def test_add_product_to_cart(py):
    py.visit("https://www.webstaurantstore.com")
    py.getx("(//input[@name='searchval'])[1]").type("air fryer", Keys.ENTER)
    assert py.should().contain_title("Air Fryer")
    assert py.getx("//h1[contains(., 'Results for:')]/span[contains(., 'air fryer')]").should().be_visible()
    py.getx("(//span[contains(@data-filter-content, 'filter-list__content') and text()='Entry Level'])[2]").click()
    py.getx("//span[contains(., 'TurboChef Fire Black')]").click()
    py.get("#buyButton").click()
    py.get("button[data-testid=cancel-button]").click()
    assert py.get("#cartItemCountSpan").should().have_text("1")