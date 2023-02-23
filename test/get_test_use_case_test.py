from unittest.mock import MagicMock
import unittest
import asyncio
from automapper import Mapper
from mock import AsyncMock

from src.application.use_cases.test.create_test_use_case import CreateTestUseCase
from src.domain.dto.test_dto import TestDto
from src.domain.interfaces.infrastructure.persistence.repository.i_repository_test import IRepositoryTest
from src.domain.model.test import Test


def mock_responses(responses, default_response=None):
    return lambda input: responses[input] if input in responses else default_response


class TestGetUseCaseTest(unittest.IsolatedAsyncioTestCase):
    async def test_get_test_use_case_success(self):
        request: TestDto = TestDto("pepito", 33, "home inc")
        request_internal: Test = Test("pepito", 33, "home inc")

        repository_mock: IRepositoryTest = AsyncMock()
        repository_mock.create_test.return_value = request_internal

        mapper_test: Mapper = MagicMock()
        mapper_test.map.side_effect = mock_responses(
            {
                request: request_internal,
                request_internal: request
            })

        application = CreateTestUseCase(repository_mock, mapper_test)
        response = await application.handler(request)

        self.assertEqual(response.name, request.name)
