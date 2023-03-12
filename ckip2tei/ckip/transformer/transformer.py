import asyncio

from ..model import CKIPClient

ws_driver, pos_driver = CKIPClient().connect()


async def pack_ws_pos(ws_pos_pair: tuple) -> list[tuple]:
    """The pack_ws_pos_sentece method packs a word and its part-of-speech to a pair.

    Args:
        ws_pos_pair (tuple): the pair of a word and its corresponding part-of-speech
    Returns:
        a list of tuples: [
            ('我', 'Nh'),
            ('喜歡', 'VK'),
            ('程式', 'Na')
        ]
    """
    sentence_ws, sentence_pos = ws_pos_pair
    assert len(sentence_ws) == len(sentence_pos)
    return list(zip(sentence_ws, sentence_pos))


async def transform(sentence: str):
    """The transform method transforms the sentences in a list to word segmentation and
    part-of-speech results.
    """
    stripped_sentence = sentence.strip()

    if not stripped_sentence:
        return []

    ws_pipeline = ws_driver([stripped_sentence], use_delim=True)
    pos_pipeline = pos_driver(ws_pipeline, use_delim=True)
    return await asyncio.gather(*map(pack_ws_pos, zip(ws_pipeline, pos_pipeline)))
