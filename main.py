import time
import pytz
import logging
import warnings
from data.site import get_site, create_driver, screenshot
from controllers.conf import format_time_exec, time_converter

logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
warnings.filterwarnings("ignore")

logging.Formatter.converter = time_converter(pytz.timezone('America/Mexico_City'))
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='log.log',
    filemode='w')

def main():
    inicio = time.time()
    driver = create_driver()
    get_site(driver)
    time.sleep(5)
    screenshot(driver,'test')
    driver.quit()
    logging.info(format_time_exec(inicio))
    print('Done')
if __name__ == "__main__":
    main()