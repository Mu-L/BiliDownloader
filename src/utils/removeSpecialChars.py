_TITLE_SIZE_LIMIT = 20


def removeSpecialChars(original: str, limit=_TITLE_SIZE_LIMIT):
    spe = ":~!?@#$%^&*()+*/<>,.[]\\|\"' "
    ret = original[:]
    for ch in spe:
        ret = ret.replace(ch, "_")
    if limit:
        if len(ret) > _TITLE_SIZE_LIMIT:
            ret = ret[:_TITLE_SIZE_LIMIT]
    if len(ret) == 0:
        ret = "_"
    return ret
