# Copyright 2023-2024 SGLang Team
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Event handling system for SGLang tracing."""

from enum import StrEnum
from typing import Any, Dict


class EventType(StrEnum):
    SCHEDULER = "scheduler"
    GENERATE = "generate"

    def process_attrs(self, attrs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Static method to process attributes based on event type
        """
        if self == EventType.GENERATE:
            return self._process_generate_attrs(attrs, **kwargs)
        else:
            return self._process_general_attrs(attrs, **kwargs)

    @staticmethod
    def _process_general_attrs(attrs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Process attributes for general events
        """
        return attrs

    @staticmethod
    def _process_generate_attrs(attrs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Process attributes for generate events
        """
        if "req" in kwargs and kwargs["req"]:
            req = kwargs["req"]
        attrs.update(
            {
                "output_ids": req.output_ids[-req.new_accepted_len :],
            }
        )
        return None
