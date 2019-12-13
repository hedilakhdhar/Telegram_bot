from .financials import get_financial_data

def get_response(msg):
    """
    you can place your mastermind AI here
    could be a very basic simple response like "معلش"
    or a complex LSTM network that generate appropriate answer
    """
    perf = get_financial_data(msg)

    return 'as of {} : {}%'.format(last, np.round(perf * 100,2))
