def get_response(msg):
    """
    you can place your mastermind AI here
    could be a very basic simple response like "معلش"
    or a complex LSTM network that generate appropriate answer
    """
    if msg == 'solva':
        var = '300%'
    elif msg == 'perf':
        var = 'action +12%'
    else:
        var = 'cacsh !'

    return var
