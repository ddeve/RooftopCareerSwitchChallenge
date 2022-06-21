import pytest
from source.riddle import RiddleMock


class TestRiddle:
    def test_Riddle(self):
        Service = RiddleMock
        token = Service.getToken()
        unsortedBlocks = Service.getBlocks(token=token)
        unsortedBlocks_length = len(unsortedBlocks)
        orderedBlocks = Service.check(blocks=unsortedBlocks, token=token)
        # validate inicial blocks amount = final blocks amount
        assert unsortedBlocks_length == len(orderedBlocks)
        result = Service.verify(blocks=orderedBlocks, token=token)
        # validate result is correct
        assert result
