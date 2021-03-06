# -*- coding: utf-8 -*-

def mne_data(what="raw", path=None):
    """Utility function to easily access MNE datasets

    Parameters
    -----------
    what : str
        Can be 'raw' or 'filt-0-40_raw' (a filtered version).
    path : str
        Defaults to None, assuming that the MNE data folder already exists. If not,
        specify the directory to download the folder.

    Returns
    -------
    object
        The raw mne object.

    Examples
    ---------
    >>> import neurokit2 as nk
    >>>
    >>> raw = nk.mne_data(what="raw")

    """
    # Try loading mne
    try:
        import mne
    except ImportError:
        raise ImportError(
            "NeuroKit error: mne_data(): the 'mne' module is required for this function to run. ",
            "Please install it first (`pip install mne`).",
        )

    old_verbosity_level = mne.set_log_level(verbose="WARNING", return_old_level=True)

    if what in ["raw", "filt-0-40_raw"]:
        if path is None:
            try:
                path = mne.datasets.sample.data_path()
            except ValueError:
                raise ValueError("NeuroKit error: the mne sample data folder does not exist. ",
                                 "Please specify a path to download the mne datasets.")
        path += '/MEG/sample/sample_audvis_' + what + '.fif'
        data = mne.io.read_raw_fif(path, preload=True)
        data = data.pick_types(meg=False, eeg=True)

    mne.set_log_level(old_verbosity_level)
    return data
