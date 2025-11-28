import Lab2

def test_min_max():
    num_list = [5.0, 67.0, 32.0, -10.0, 0.0]
    result = Lab2.find_min_max(num_list)
    assert result == [-10.0, 67.0]

def test_average():
    num_list = [5.0, 15.0, 25.0]
    result = Lab2.calc_average(num_list)
    assert result == 15.0

def test_median_temperature_odd():
    num_list = [5.0, 15.0, 25.0]
    result = Lab2.calc_median_temperature(num_list)
    assert result == 15.0

def test_median_temperature_even():
    num_list = [5.0, 15.0, 25.0, 35.0]
    result = Lab2.calc_median_temperature(num_list)
    assert result == 20.0