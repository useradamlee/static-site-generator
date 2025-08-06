def markdown_to_blocks(markdown):
    return list(map(lambda line: line.strip(), markdown.split("\n\n")))
# I realised that map would work in this context
