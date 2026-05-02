import time
import logging

def retry(max_retries=3, delay=1, backoff=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay

            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    logging.warning(
                        f"Retry {retries}/{max_retries} after error: {str(e)}"
                    )

                    if retries == max_retries:
                        logging.error("Max retries reached. Failing.")
                        raise

                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper
    return decorator