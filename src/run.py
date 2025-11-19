from pipeline import EduMatePipeline

if __name__ == "__main__":
    bot = EduMatePipeline()
    q = input("Ask something: ")
    print(bot.run(q))
