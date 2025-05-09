# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class KeyIndicatorsItemExtraKpisItem(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The key for this KPI, where you can find the value from inside main_kpi
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The label for this KPI, to be displayed to the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
