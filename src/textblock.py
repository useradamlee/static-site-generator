from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "unordered_list"

def markdown_to_blocks(markdown):
    return list(map(lambda line: line.strip(), markdown.split("\n\n")))
# I realised that map would work in this context

def block_to_block_type(block):
    if block.startswith('#'):
        parts = block.split(' ', 1)
        if len(parts) > 1:
            hashes = parts[0]
            if hashes.count('#') == len(hashes) and 1 <= len(hashes) <= 6:
                return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        lines = block.split('\n')
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        lines = block.split('\n')
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1.'):
        lines = block.split('\n')
        for i, line in enumerate(lines):
            # Check if line starts with the expected number
            expected_start = f"{i + 1}. "
            if not line.startswith(expected_start):
                # Not an ordered list
                return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
