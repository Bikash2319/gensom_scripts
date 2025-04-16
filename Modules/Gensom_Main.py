from Make import Make
from Setup import Setup

class Gensom:

    Setup = Setup()
    driver , wait = Setup.initialize_driver()
    make = Make(driver, wait)


    make.open_make_module()
    make.click_on_add_make_button()
    make.enter_make()
    make.click_on_save_button()


