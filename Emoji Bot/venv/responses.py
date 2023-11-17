import random
import emoji


def handle_response(msgin) -> str:
    msg = msgin.lower()
    
    if msg == 'hello' :
        return 'hi'
    
    if msg == 'help' :
        return 'I Have Nothing To Help This is A Test Bot Dumb Ass'
    

    demojize_text = emoji.demojize(msg)
    emojize_text = emoji.emojize(msg)
    analyzed_text = list(emoji.analyze(msg, join_emoji=False))
    unicode_text = msg.encode('unicode-escape').decode()

    print("demojize_text :", demojize_text, "\n emojize_text :", emojize_text, "\nanalyzed_text :", analyzed_text, "\nunicode_text :", unicode_text)
    return("demojize_text :", demojize_text, "\n emojize_text :", emojize_text, "\nanalyzed_text :", analyzed_text, "\nunicode_text :", unicode_text)