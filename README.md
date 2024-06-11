# API Framework Comparison

This repository gives a small overview and comparison for both [Flask](https://flask.palletsprojects.com/en/3.0.x/) and [FastAPI](https://fastapi.tiangolo.com/).

**Table of Content:**
<!-- vscode-markdown-toc -->
* [Install](#Install)
* [Run Python APIs](#RunPythonAPIs)
	* [FastAPI](#FastAPI)
	* [Flask](#Flask)
* [Comparison Table](#ComparisonTable)
* [Discussions](#Discussions)
	* [Performance](#Performance)
	* [FastAPI - When to use `async`](#FastAPI-Whentouseasync)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Install'></a>Install

```shell
poetry install
```

## <a name='RunPythonAPIs'></a>Run Python APIs

### <a name='FastAPI'></a>FastAPI

After the installation, you can start the FastAPI backend via:

```shell
poe start-fastapi
```

You can open the OpenAPI definition in <http://127.0.0.1:8000/docs>.

### <a name='Flask'></a>Flask

After the installation, you can start the Flask backend via:

```shell
poe start-flask
```

## <a name='ComparisonTable'></a>Comparison Table

| Flask  | FastAPI |
| --- | ----|
| 2010 | 2019 |
| Micro framework| Full-Stack framwork |
| Async support from > v2.0 | Async first |
| License: BSD-3 Clause | License: MIT |
| No built-in data validation | Built-in data validation with pydantic |
| | Out-of-the-box OpenAPI documentation |

## <a name='Discussions'></a>Discussions
### <a name='Performance'></a>Performance

Apparently, there are a few discussions online regarding the speed of both frameworks. Initially, FastAPI
was supposed to be the faster framework due to the async-first implementation. However, with version [2.0](https://flask.palletsprojects.com/en/2.3.x/async-await/),
Flask also added async support:

- <https://www.reddit.com/r/flask/comments/xvw1vi/misunderstandings_about_how_async_works_with/>
- <https://www.reddit.com/r/flask/comments/13pyxie/flask_vs_fastapi/>
- <https://stackoverflow.com/questions/76297879/benchmarks-of-fastapi-vs-async-flask>
- <https://flask.palletsprojects.com/en/2.3.x/async-await/>
- <https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one>
- <https://www.geeksforgeeks.org/flask-vs-fastapi/>

### <a name='FastAPI-Whentouseasync'></a>FastAPI - When to use `async`

Similarly, there are also some open discussions whether one should always define routes in FastAPI with `async`
or not:

- <https://www.reddit.com/r/FastAPI/comments/18c66xt/how_do_you_decide_which_functionsroutes_should_be/>
- <https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-9-asynchronous-performance-basics/>
- <https://rishibajargan.medium.com/do-not-over-use-async-with-fastapi-fa70bed14d9c>
- <https://github.com/tiangolo/fastapi/discussions/10771>
- <https://superfastpython.com/asyncio-vs-threading/>
- <https://www.geeksforgeeks.org/blocking-and-nonblocking-io-in-operating-system/>

For normal path operation functions (without `async`), the function is run in an external threadpool that is then
awaited, instead of being called directly (See: [documentation](https://fastapi.tiangolo.com/async/#path-operation-functions)).

The only official answer ([discussion 10771](https://github.com/tiangolo/fastapi/discussions/10771)) states:
> FastAPI is an async framework, and async should the be the default choice.

and that the "threadpool def endpoints" are merely an escape hatch.
