def _init_kernel() -> None:
    import os

    from IPython import get_ipython

    from .kernel import compile_jupyter

    ip = get_ipython()
    ip.run_cell("from neptyne_kernel.kernel_init import *")
    ip.input_transformers_cleanup.append(compile_jupyter)
    os.environ["NEPTYNE_LOCAL_REPL"] = "1"


def init_notebook(api_key: str = "", api_host: str = "https://app.neptyne.com") -> None:
    _init_kernel()
    if api_key:
        import neptyne as nt

        nt.connect_kernel(api_key, api_host)


def init_colab(gsheet_id: str) -> None:
    _init_kernel()

    import neptyne as nt

    nt.connect_colab(gsheet_id)
