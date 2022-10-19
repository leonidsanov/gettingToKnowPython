# модуль контроллер, который свяжет все модули

import task01_12102022
import task02_12102022
import modul_mult as modul

def button_click():
    value_a = task02_12102022.get_value()
    value_b = task02_12102022.get_value()
    modul.init(value_a, value_b)
    result = modul.mult()
    task02_12102022.view(result)