def main():
    from chatterbot import ChatBot
    import engine.login as ln
    
    login_aut = ln.login()

    bot = ChatBot(
        "terminal",
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ],
        logic_adapters=[
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.BestMatch"
        ],
        input_adapter="chatterbot.input.TerminalAdapter",
        output_adapter="chatterbot.output.TerminalAdapter",
        database='data/db/' + login_aut['name'] + '.db',
        user=login_aut['name'],
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )

    if login_aut['is_new']:
        bot.train('chatterbot.corpus.english')

    while True:
        try:
            bot.get_response(None)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == '__main__':
    main()