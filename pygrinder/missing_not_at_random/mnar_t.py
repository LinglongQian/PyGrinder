"""
Corrupt data by adding missing values to it with MNAR (missing not at random) pattern.
"""

# Created by Jun Wang <jwangfx@connect.ust.hk> and Wenjie Du <wenjay.du@gmail.com>
# License: BSD-3-Clause

from typing import Optional, Union, Tuple, overload

import numpy as np
import torch


@overload
def mnar_t(
    X: Optional[Union[np.ndarray, torch.Tensor]],
    cycle: float,
    pos: float,
    scale: float,
    return_masks: bool = True,
    nan: Union[float, int] = 0,
) -> Union[Tuple[np.ndarray, ...], Tuple[torch.Tensor, ...], np.ndarray, torch.Tensor]:
    raise NotImplementedError()


@overload
def mnar_t(
    X: Optional[Union[np.ndarray, torch.Tensor]],
    cycle: float,
    pos: float,
    scale: float,
    return_masks: bool = False,
    nan: Union[float, int] = 0,
) -> Union[Tuple[np.ndarray, ...], Tuple[torch.Tensor, ...], np.ndarray, torch.Tensor]:
    raise NotImplementedError()


def mnar_t(
    X: Optional[Union[np.ndarray, torch.Tensor]],
    cycle: float = 20,
    pos: float = 10,
    scale: float = 3,
    return_masks: bool = True,
    nan: Union[float, int] = 0,
) -> Union[Tuple[np.ndarray, ...], Tuple[torch.Tensor, ...], np.ndarray, torch.Tensor]:
    """Create not-random missing values related to temporal dynamics (MNAR-t case).
    In particular, the missingness is generated by an intensity function f(t) = exp(3*torch.sin(cycle*t + pos)).
    This case mainly follows the setting in https://hawkeslib.readthedocs.io/en/latest/tutorial.html.

    Parameters
    ----------
    X :
        Data vector. If X has any missing values, they should be numpy.nan.

    cycle :
        The cycle of the used intensity function

    pos :
        The displacement of the used intensity function

    scale :
        The scale number to control the missing rate

    return_masks : bool, optional, default=True
        Whether to return the masks indicating missing values in X and indicating artificially-missing values in X.
        If True, return X_intact, X, missing_mask, and indicating_mask (refer to Returns for more details).
        If False, only return X with added missing not at random values.

    nan : int/float, optional, default=0
        Value used to fill NaN values. Only valid when return_masks is True.
        If return_masks is False, the NaN values will be kept as NaN.


    Returns
    -------
    If return_masks is True:

        X_intact : array,
            Original data with missing values (nan) filled with given parameter `nan`, with observed values intact.
            X_intact is for loss calculation in the masked imputation task.

        X : array,
            Original X with artificial missing values. X is for model input.
            Both originally-missing and artificially-missing values are filled with given parameter `nan`.

        missing_mask : array,
            The mask indicates all missing values in X.
            In it, 1 indicates observed values, and 0 indicates missing values.

        indicating_mask : array,
            The mask indicates the artificially-missing values in X, namely missing parts different from X_intact.
            In it, 1 indicates artificially missing values,
            and the other values (including originally observed/missing values) are indicated as 0.

    If return_masks is False:

        X : array-like
            Original X with artificial missing values.
            Both originally-missing and artificially-missing values are left as NaN.
    """
    if isinstance(X, list):
        X = np.asarray(X)

    if isinstance(X, np.ndarray):
        results = _mnar_t_numpy(X, cycle, pos, scale, return_masks, nan)
    elif isinstance(X, torch.Tensor):
        results = _mnar_t_torch(X, cycle, pos, scale, return_masks, nan)
    else:
        raise TypeError(
            "X must be type of list/numpy.ndarray/torch.Tensor, " f"but got {type(X)}"
        )

    if not return_masks:
        X = results
        return X

    X_intact, X, missing_mask, indicating_mask = results
    return X_intact, X, missing_mask, indicating_mask


def _mnar_t_numpy(
    X: np.ndarray,
    cycle: float = 20,
    pos: float = 10,
    scale: float = 3,
    return_masks: bool = True,
    nan: Union[float, int] = 0,
) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    # clone X to ensure values of X out of this function not being affected
    X = np.copy(X)

    X_intact = np.copy(X)  # keep a copy of originally observed values in X_intact

    n_s, n_l, n_c = X.shape

    ori_mask = (~np.isnan(X)).astype(np.float32)
    X = np.nan_to_num(X, nan=nan)

    ts = np.linspace(0, 1, n_l).reshape(1, n_l, 1)
    ts = np.repeat(ts, n_s, axis=0)
    ts = np.repeat(ts, n_c, axis=2)
    intensity = np.exp(3 * np.sin(cycle * ts + pos))
    mnar_missing_mask = (np.random.rand(n_s, n_l, n_c) * scale) < intensity

    missing_mask = ori_mask * mnar_missing_mask

    if not return_masks:
        X[missing_mask == 0] = np.nan
        return X

    indicating_mask = ori_mask - missing_mask
    X_intact = np.nan_to_num(X_intact, nan=nan)
    X[missing_mask == 0] = nan
    return tuple((X_intact, X, missing_mask, indicating_mask))


def _mnar_t_torch(
    X: torch.Tensor,
    cycle: float = 20,
    pos: float = 10,
    scale: float = 3,
    return_masks: bool = True,
    nan: Union[float, int] = 0,
) -> Union[Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor]:
    # clone X to ensure values of X out of this function not being affected
    X = torch.clone(X)

    X_intact = torch.clone(X)  # keep a copy of originally observed values in X_intact
    n_s, n_l, n_c = X.shape

    ori_mask = (~torch.isnan(X)).type(torch.float32)
    X = torch.nan_to_num(X, nan=nan)

    ts = torch.linspace(0, 1, n_l).reshape(1, n_l, 1).repeat(n_s, 1, n_c)
    intensity = torch.exp(3 * torch.sin(cycle * ts + pos))
    mnar_missing_mask = (torch.randn(X.size()).uniform_(0, 1) * scale) < intensity

    missing_mask = ori_mask * mnar_missing_mask

    if not return_masks:
        X[missing_mask == 0] = np.nan
        return X

    indicating_mask = ori_mask - missing_mask
    X_intact = torch.nan_to_num(X_intact, nan=nan)
    X[missing_mask == 0] = nan
    return tuple((X_intact, X, missing_mask, indicating_mask))
