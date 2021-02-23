import pytest

from hama.tagging import tag


def test_tag():
    text = "돼지가 아니라 하마입니다."
    tags = tag(text)
    # print(tags)

    text = "밥주세요."
    tags = tag(text, zipped=True)
    # print(tags)

    text = "프론트엔드 에서도 돌아갑니다"
    tags = tag(text)
    # print(tags)
