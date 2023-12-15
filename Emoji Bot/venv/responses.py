import random
import emoji
import llama2inferencecleanedipynb
import torch
import gc

def handle_response(msgin) -> str:
    msg = msgin.lower()
    # msg = msg.split(" ")
    print(msg)
    if msg == 'hello' :
        return 'hi'

    if msg[0:8] == "analyze ":
        msgs = msg.split("analyze ")[1]
        print(msgs)

        demojize_text = emoji.demojize(msgs)
        emojize_text = emoji.emojize(msgs)
        analyzed_text = list(emoji.analyze(msgs, join_emoji=False))
        unicode_text = msgs.encode('unicode-escape').decode()
        return ("demojize_text :", demojize_text, "\n emojize_text :", emojize_text, "\nanalyzed_text :", analyzed_text, "\nunicode_text :", unicode_text)


    if msg[0:9] == 'generate ' :
        msgs = msg.split("generate ")[1]
        demojize_text = emoji.demojize(msgs)
        
        PreprocessZero = demojize_text.replace(" ", "")
        PreprocessOne = PreprocessZero.replace("::", ", ")
        PreprocessTwo = PreprocessOne.replace(":", "")
        PromptResult = "Please create a sentence from these 3 aspects: " + PreprocessTwo +"."
        
        SCurModel, SCurTokenizer = llama2inferencecleanedipynb.Get_ModelTokenizer()
        SCurDevice = llama2inferencecleanedipynb.Get_Current_Device()    
        
        SResult = llama2inferencecleanedipynb.GetInference(PromptResult, SCurModel, SCurTokenizer, SCurDevice)
        print("Prompt0: " + PreprocessOne)
        print("Prompt0: " + PreprocessTwo)
        print("Prompt0: " + PromptResult)
        print("Result: " + SResult)
        del SCurModel
        del SCurTokenizer
        del SCurDevice
        gc.collect()
        torch.cuda.empty_cache()
        return(SResult)

        # print(msgs)
        # return(demojize_text)

    # demojize_text = emoji.demojize(msg)
    # emojize_text = emoji.emojize(msg)
    # analyzed_text = list(emoji.analyze(msg, join_emoji=False))
    # unicode_text = msg.encode('unicode-escape').decode()

    # print("demojize_text :", demojize_text, "\n emojize_text :", emojize_text, "\nanalyzed_text :", analyzed_text, "\nunicode_text :", unicode_text)
    print(msg)
    return("Unknown Command")