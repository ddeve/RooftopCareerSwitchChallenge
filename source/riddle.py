from typing import List
import requests
import abc


class IRinddle(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def getToken(cls) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def getBlocks(cls, token: str) -> List[str]:
        pass

    @classmethod
    def check(cls, blocks: List[str], token: str) -> List[str]:
        """
        Sort blocks of the riddle and returns in a new list
        """

        orderedBloks: List[str] = []
        correctBlock = blocks.pop(0)
        orderedBloks.append(correctBlock)
        while len(blocks) > 0:
            for index in range(0, len(blocks)):
                if cls.correctBlockOrder(correctBlock, blocks[index], token):
                    correctBlock = blocks.pop(index)
                    orderedBloks.append(correctBlock)
                    break
        return orderedBloks

    @classmethod
    @abc.abstractmethod
    def correctBlockOrder(cls, correctBlock: str, verifyBlock: str, token: str) -> bool:
        pass

    @classmethod
    @abc.abstractmethod
    def verify(cls, blocks: List[str], token: str) -> bool:
        pass


class Riddle(IRinddle):
    session = requests.session()
    api_url = "https://rooftop-career-switch.herokuapp.com"
    email = "deve.daniel@gmail.com"
    token = ""

    @classmethod
    def getToken(cls) -> str:
        """
        Get a Token to call the others endpoints in base of configured email
        """
        if not cls.token:
            url = f"{cls.api_url}/token?email={cls.email}"
            response = cls.session.get(url=url)
            if response.status_code == 200:
                cls.token = response.json().get("token")
            else:
                cls.raiseServerError(url=url, status_code=response.status_code)
        return cls.token

    @classmethod
    def getBlocks(cls, token: str) -> List[str]:
        """
        Get a riddle, return an unsorted list of strings
        """
        url = f"{cls.api_url}/blocks?token={token}"
        response = cls.session.get(url=url)
        if response.status_code == 200:
            return response.json().get("data")
        else:
            cls.raiseServerError(url=url, status_code=response.status_code)

    @classmethod
    def check(cls, blocks: List[str], token: str) -> List[str]:
        """
        Sort blocks of the riddle and returns in a new list
        """

        return super().check(blocks=blocks, token=token)

    @classmethod
    def correctBlockOrder(cls, correctBlock: str, verifyBlock: str, token: str) -> bool:
        """
        if verifyBlock is in correct order returns True
        else returns False
        """
        data = {"blocks": [correctBlock, verifyBlock]}
        url = f"{cls.api_url}/check?token={token}"
        response = cls.session.post(url=url, data=data)
        if response.status_code == 200:
            return response.json().get("message")
        else:
            cls.raiseServerError(url=url, status_code=response.status_code)

    @classmethod
    def verify(cls, blocks: List[str], token: str) -> bool:
        """
        Verify if blocks are in correct order.
        If that is the case returns True
        otherwise returns False
        """

        data = {"encoded": "".join(blocks)}
        url = f"{cls.api_url}/check?token={token}"
        response = cls.session.post(url=url, data=data)
        if response.status_code == 200:
            return response.json().get("message")
        else:
            cls.raiseServerError(url=url, status_code=response.status_code)

    @staticmethod
    def raiseServerError(url: str, status_code: int):
        raise Exception(f"Server Error: {url} \nStatus Code: {str(status_code)}")


class RiddleMock(IRinddle):
    token = "this_is_a_mock_token"
    blocks = ["f319", "3720", "4e3e", "46ec", "c7df", "c1c7", "80fd", "c4ea"]
    ordered_blocks = ["f319", "46ec", "c1c7", "3720", "c7df", "c4ea", "4e3e", "80fd"]
    correct_order = {
        "f319": "46ec",
        "46ec": "c1c7",
        "c1c7": "3720",
        "3720": "c7df",
        "c7df": "c4ea",
        "c4ea": "4e3e",
        "4e3e": "80fd",
    }

    @classmethod
    def getToken(cls) -> str:
        """
        Get a Token to call the others endpoints in base of configured email
        """
        return cls.token

    @classmethod
    def getBlocks(cls, token: str) -> List[str]:
        """
        Get a riddle, return an unsorted list of strings
        """
        return cls.blocks

    @classmethod
    def check(cls, blocks: List[str], token: str) -> List[str]:
        """
        Sort blocks of the riddle and returns in a new list
        """
        return super().check(blocks=blocks, token=token)

    @classmethod
    def correctBlockOrder(cls, correctBlock: str, verifyBlock: str, token: str) -> bool:
        """
        if verifyBlock is in correct order returns True
        else returns False
        """
        return cls.correct_order[correctBlock] == verifyBlock

    @classmethod
    def verify(cls, blocks: List[str], token: str) -> bool:
        """
        Verify if blocks are in correct order.
        If that is the case returns True
        otherwise returns False
        """
        expected = "".join(cls.ordered_blocks)
        result = "".join(blocks)
        return expected == result
