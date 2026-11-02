import pytest
from pages.percent_calculator_page import PercentCalculatorPage

# Корректный расчёт (минимум 5 наборов данных)
@pytest.mark.parametrize("percent, of_value, expected", [
    (10, 200, "20"),
    (25, 80, "20"),
    (0, 500, "0"),
    (100, 37, "37"),
    (33, 100, "33")
])
def test_percent_calculation_correct(driver, percent, of_value, expected):
    page = PercentCalculatorPage(driver)
    page.open().enter_percent(percent).enter_of(of_value).click_calculate()
    assert page.get_result() == expected

# Граничные значения (отрицательные значения и большие числа)
@pytest.mark.parametrize("percent, of_value, expected", [
    (-10, 100, "-10"),
    (999999, 10, "99999.9")
])
def test_percent_calculation_boundaries(driver, percent, of_value, expected):
    page = PercentCalculatorPage(driver)
    page.open().enter_percent(percent).enter_of(of_value).click_calculate()
    assert page.get_result() == expected

# Неверный ввод (буквы) и проверка текста ошибки
def test_percent_invalid_input_letters(driver):
    page = PercentCalculatorPage(driver)
    page.open().enter_percent("abc").enter_of("xyz").click_calculate()
    error_text = page.get_error_text()
    assert "Please provide two numeric values" in error_text

# Поведение кнопки «Clear»
def test_clear_button(driver):
    page = PercentCalculatorPage(driver)
    page.open().enter_percent(50).click_reset()
    assert page.get_percent_value() == ""