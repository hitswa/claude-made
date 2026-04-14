# anatomy.md

> Auto-maintained by OpenWolf. Last scanned: 2026-04-14T20:06:55.581Z
> Files: 509 tracked | Anatomy hits: 0 | Misses: 0

## ./

- `.gitignore` — Git ignore rules (~102 tok)
- `AGENTS.md` — Multi-Agent Workflow Boundaries (~739 tok)
- `Claude Multi-Agent System Template.md` — **Architecting High-Efficiency Multi-Agent Systems Using the Claude Framework** (~11971 tok)
- `CLAUDE.md` — CLAUDE.md (~991 tok)
- `README.md` — Project documentation (~343 tok)
- `requirements.txt` — Python dependencies (~160 tok)

## .claude/

- `config.json` (~0 tok)
- `settings.json` (~441 tok)

## .claude/agents/

- `architect.md` — Rules (~280 tok)
- `builder.md` — Rules (~275 tok)
- `reviewer.md` — Rules (~281 tok)

## .claude/commands/

- `new-task.md` (~179 tok)

## .claude/memory/

- `.gitkeep` (~0 tok)

## .claude/rules/

- `openwolf.md` (~313 tok)

## .claude/skills/strict-review/

- `SKILL.md` (~189 tok)

## .venv/

- `.gitignore` — Git ignore rules (~19 tok)
- `pyvenv.cfg` (~88 tok)

## .venv/bin/

- `activate` — This file must be used with "source bin/activate" *from bash* (~596 tok)
- `activate.csh` — This file must be used with "source bin/activate.csh" *from csh*. (~254 tok)
- `activate.fish` — This file must be used with "source <venv>/bin/activate.fish" *from fish* (~593 tok)
- `Activate.ps1` — Declares from (~2409 tok)
- `dmypy` (~65 tok)
- `dotenv` — -*- coding: utf-8 -*- (~73 tok)
- `httpx` — -*- coding: utf-8 -*- (~71 tok)
- `jsonschema` — -*- coding: utf-8 -*- (~73 tok)
- `mcp` — -*- coding: utf-8 -*- (~71 tok)
- `mypy` (~64 tok)
- `mypyc` (~59 tok)
- `pip` — -*- coding: utf-8 -*- (~75 tok)
- `pip3` — -*- coding: utf-8 -*- (~75 tok)
- `pip3.13` — -*- coding: utf-8 -*- (~75 tok)
- `stubgen` (~59 tok)
- `stubtest` (~59 tok)
- `uvicorn` — -*- coding: utf-8 -*- (~72 tok)

## .venv/lib/python3.13/site-packages/

- `mypy_extensions.py` — Defines experimental extensions to the standard "typing" module that are (~2216 tok)
- `typing_extensions.py` — _Sentinel: final, done, done, disjoint_base + 1 more (~45837 tok)

## .venv/lib/python3.13/site-packages/annotated_types-0.7.0.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares MyClass (~4013 tok)
- `RECORD` (~214 tok)
- `WHEEL` (~24 tok)

## .venv/lib/python3.13/site-packages/annotated_types-0.7.0.dist-info/licenses/

- `LICENSE` — Project license (~289 tok)

## .venv/lib/python3.13/site-packages/annotated_types/

- `__init__.py` — Declares from (~3949 tok)
- `py.typed` (~0 tok)
- `test_cases.py` — Test file (~1834 tok)

## .venv/lib/python3.13/site-packages/anyio-4.13.0.dist-info/

- `entry_points.txt` (~10 tok)
- `INSTALLER` (~2 tok)
- `METADATA` (~1203 tok)
- `RECORD` (~1669 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## .venv/lib/python3.13/site-packages/anyio-4.13.0.dist-info/licenses/

- `LICENSE` — Project license (~288 tok)

## .venv/lib/python3.13/site-packages/anyio/

- `__init__.py` — Declares as (~1763 tok)
- `from_thread.py` — _BlockingAsyncContextManager: run, run_sync, run_async_cm, started + 9 more (~5469 tok)
- `functools.py` — _InitialMissingType: cache_info, cache_parameters, cache_clear, cache_info + 12 more (~3451 tok)
- `lowlevel.py` — View: get, get, get (~1474 tok)
- `py.typed` (~0 tok)
- `pytest_plugin.py` — FreePortFactory: extract_backend_and_options, get_runner, pytest_addoption, pytest_configure + 10 more (~3650 tok)
- `to_interpreter.py` — _Worker: destroy, call, destroy, call + 4 more (~2029 tok)
- `to_process.py` — from: run_sync, send_raw_command, current_default_process_limiter, process_worker (~2800 tok)
- `to_thread.py` — run_sync, current_default_thread_limiter (~770 tok)

## .venv/lib/python3.13/site-packages/anyio/_backends/

- `__init__.py` (~0 tok)
- `_asyncio.py` — _State: close, get_loop, run, find_root_task + 2 more (~28422 tok)
- `_trio.py` — from: cancel, deadline, deadline, cancel_called + 25 more (~11819 tok)

## .venv/lib/python3.13/site-packages/anyio/_core/

- `__init__.py` (~0 tok)
- `_asyncio_selector_thread.py` — Selector: start, add_reader, add_writer, remove_reader + 3 more (~1608 tok)
- `_contextmanagers.py` — Declares _SupportsCtxMgr (~2062 tok)
- `_eventloop.py` — because: run, sleep, sleep_forever, sleep_until + 9 more (~1842 tok)
- `_exceptions.py` — BrokenResourceError: iterate_exceptions (~1260 tok)
- `_fileio.py` — from: wrapped, aclose, read, read1 + 35 more (~7333 tok)
- `_resources.py` — aclose_forcefully (~125 tok)
- `_signals.py` — open_signal_receiver (~291 tok)
- `_sockets.py` — URL configuration (~9992 tok)
- `_streams.py` — Declares create_memory_object_stream (~516 tok)
- `_subprocesses.py` — run_process, drain_stream, open_process (~2262 tok)
- `_synchronization.py` — from: set, is_set, wait, statistics + 29 more (~6018 tok)
- `_tasks.py` — _IgnoredTaskStatus: started, cancel, deadline, deadline + 8 more (~1553 tok)
- `_tempfile.py` — TemporaryFile: aclose, rollover, closed, read + 6 more (~5607 tok)
- `_testing.py` — TaskInfo: has_pending_cancellation, get_current_task, get_running_tasks, wait_all_tasks_blocked (~669 tok)
- `_typedattr.py` — TypedAttributeSet: typed_attribute, extra_attributes, extra, extra + 1 more (~717 tok)

## .venv/lib/python3.13/site-packages/anyio/abc/

- `__init__.py` (~820 tok)
- `_eventloop.py` — AsyncBackend: run, current_token, current_time, cancelled_exception_class + 43 more (~3037 tok)
- `_resources.py` — AsyncResource: aclose (~224 tok)
- `_sockets.py` — SocketAttribute: extra_attributes, from_socket, from_socket, send_fds + 9 more (~3750 tok)
- `_streams.py` — UnreliableObjectReceiveStream: receive, send, send_eof, receive + 5 more (~2138 tok)
- `_subprocesses.py` — Process: wait, terminate, kill, send_signal + 5 more (~591 tok)
- `_tasks.py` — TaskStatus: started, started, started, start_soon + 1 more (~1064 tok)
- `_testing.py` — TestRunner: run_asyncgen_fixture, run_fixture, run_test (~521 tok)

## .venv/lib/python3.13/site-packages/anyio/streams/

- `__init__.py` (~0 tok)
- `buffered.py` — BufferedByteReceiveStream: aclose, buffer, extra_attributes, feed_data + 6 more (~1790 tok)
- `file.py` — URL configuration (~1266 tok)
- `memory.py` — MemoryObjectStreamStatistics: statistics, receive_nowait, receive, clone + 9 more (~3069 tok)
- `stapled.py` — from: receive, send, send_eof, aclose + 9 more (~1255 tok)
- `text.py` — TextReceiveStream: receive, aclose, extra_attributes, send + 8 more (~1648 tok)
- `tls.py` — from: wrap, unwrap, aclose, receive + 4 more (~4373 tok)

## .venv/lib/python3.13/site-packages/attr/

- `__init__.py` — SPDX-License-Identifier: MIT (~588 tok)
- `__init__.pyi` — Declares import (~3020 tok)
- `_cmp.py` — SPDX-License-Identifier: MIT (~1177 tok)
- `_cmp.pyi` (~99 tok)
- `_compat.py` — SPDX-License-Identifier: MIT (~809 tok)
- `_config.py` — SPDX-License-Identifier: MIT (~241 tok)
- `_funcs.py` — SPDX-License-Identifier: MIT (~4709 tok)
- `_make.py` — SPDX-License-Identifier: MIT (~30323 tok)
- `_next_gen.py` — SPDX-License-Identifier: MIT (~7507 tok)
- `_typing_compat.pyi` — MYPY is a special constant in mypy which works the same way as `TYPE_CHECKING`. (~126 tok)
- `_version_info.py` — SPDX-License-Identifier: MIT (~635 tok)
- `_version_info.pyi` — Declares VersionInfo (~56 tok)
- `converters.py` — SPDX-License-Identifier: MIT (~1104 tok)
- `converters.pyi` (~172 tok)
- `exceptions.py` — SPDX-License-Identifier: MIT (~569 tok)
- `exceptions.pyi` — Declares FrozenError (~144 tok)
- `filters.py` — SPDX-License-Identifier: MIT (~513 tok)
- `filters.pyi` (~56 tok)
- `py.typed` (~0 tok)
- `setters.py` — SPDX-License-Identifier: MIT (~462 tok)
- `setters.pyi` (~156 tok)
- `validators.py` — SPDX-License-Identifier: MIT (~6158 tok)
- `validators.pyi` (~1090 tok)

## .venv/lib/python3.13/site-packages/attrs-26.1.0.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares Classifier (~2334 tok)
- `RECORD` (~949 tok)
- `WHEEL` (~24 tok)

## .venv/lib/python3.13/site-packages/attrs-26.1.0.dist-info/licenses/

- `LICENSE` — Project license (~296 tok)

## .venv/lib/python3.13/site-packages/attrs/

- `__init__.py` — SPDX-License-Identifier: MIT (~338 tok)
- `__init__.pyi` — Declares our (~2511 tok)
- `converters.py` — SPDX-License-Identifier: MIT (~22 tok)
- `exceptions.py` — SPDX-License-Identifier: MIT (~22 tok)
- `filters.py` — SPDX-License-Identifier: MIT (~21 tok)
- `py.typed` (~0 tok)
- `setters.py` — SPDX-License-Identifier: MIT (~21 tok)
- `validators.py` — SPDX-License-Identifier: MIT (~22 tok)

## .venv/lib/python3.13/site-packages/certifi-2026.2.25.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` (~660 tok)
- `RECORD` (~273 tok)
- `top_level.txt` (~2 tok)
- `WHEEL` (~25 tok)

## .venv/lib/python3.13/site-packages/certifi-2026.2.25.dist-info/licenses/

- `LICENSE` — Project license (~264 tok)

## .venv/lib/python3.13/site-packages/certifi/

- `__init__.py` (~27 tok)
- `__main__.py` (~70 tok)
- `cacert.pem` — Issuer: CN=QuoVadis Root CA 2 O=QuoVadis Limited (~72651 tok)
- `core.py` — URL patterns: 3 routes (~970 tok)
- `py.typed` (~0 tok)

## .venv/lib/python3.13/site-packages/cffi-2.0.0.dist-info/

- `entry_points.txt` (~19 tok)
- `INSTALLER` (~2 tok)
- `METADATA` (~683 tok)
- `RECORD` (~873 tok)
- `top_level.txt` (~5 tok)
- `WHEEL` (~37 tok)

## .venv/lib/python3.13/site-packages/cffi-2.0.0.dist-info/licenses/

- `AUTHORS` (~56 tok)
- `LICENSE` — Project license (~300 tok)

## .venv/lib/python3.13/site-packages/cffi/

- `__init__.py` (~146 tok)
- `_cffi_errors.h` — ifndef CFFI_MESSAGEBOX (~1117 tok)
- `_cffi_include.h` — *******  CPython-specific section  ********* (~4302 tok)
- `_embedding.h` — ** Support code for embedding **** (~5368 tok)
- `_imp_emulation.py` — get_suffixes, find_module, load_dynamic (~846 tok)
- `_shimmed_dist_utils.py` (~638 tok)
- `api.py` — FFI: cdef, are, embedding_api, dlopen + 8 more (~12049 tok)
- `backend_ctypes.py` — CTypesType: cmp, set_ffi, load_library, new_void_type + 1 more (~12130 tok)
- `cffi_opcode.py` — CffiOp: as_c_expr, as_python_bytes, format_four_bytes (~1638 tok)
- `commontypes.py` — resolve_common_type, win_common_types (~802 tok)
- `cparser.py` — specifier: source, replace, replace, replace_keeping_newlines + 2 more (~12798 tok)
- `error.py` — Declares FFIError (~251 tok)
- `ffiplatform.py` — URL configuration (~1024 tok)
- `lock.py` — allocate_lock: acquire (~214 tok)
- `model.py` — type qualifiers (~6228 tok)
- `parse_c_type.h` — Declares char (~1708 tok)
- `pkgconfig.py` — pkg-config, https://www.freedesktop.org/wiki/Software/pkg-config/ integration for cffi (~1250 tok)
- `recompiler.py` — GlobalExpr: as_c_expr, as_python_expr, as_c_expr, as_python_expr + 12 more (~18717 tok)
- `setuptools_ext.py` — URL configuration (~2689 tok)
- `vengine_cpy.py` — DEPRECATED: implementation for ffi.verify() (~12538 tok)
- `vengine_gen.py` — DEPRECATED: implementation for ffi.verify() (~7697 tok)
- `verifier.py` — DEPRECATED: implementation for ffi.verify() (~3195 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk-0.1.59.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares for (~3537 tok)
- `RECORD` (~849 tok)
- `REQUESTED` (~0 tok)
- `WHEEL` (~28 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk-0.1.59.dist-info/licenses/

- `LICENSE` — Project license (~286 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk/

- `__init__.py` — Claude SDK for Python. (~5752 tok)
- `_cli_version.py` — Bundled Claude Code CLI version. (~20 tok)
- `_errors.py` — Error types for Claude SDK. (~452 tok)
- `_version.py` — Version information for claude-agent-sdk. (~21 tok)
- `client.py` — Claude SDK Client for interacting with Claude Code. (~6753 tok)
- `py.typed` (~0 tok)
- `query.py` — Query function for one-shot interactions with Claude Code. (~1332 tok)
- `types.py` — Type definitions for Claude SDK. (~11648 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk/_bundled/

- `.gitignore` — Git ignore rules (~20 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk/_internal/

- `__init__.py` — Internal implementation details. (~12 tok)
- `client.py` — Internal client implementation. (~1904 tok)
- `message_parser.py` — Message parser for Claude Code SDK responses. (~3035 tok)
- `query.py` — Query class for handling bidirectional control protocol. (~8827 tok)
- `session_mutations.py` — Portable session mutation functions for the Agent SDK. (~6549 tok)
- `sessions.py` — Session listing implementation. (~10348 tok)

## .venv/lib/python3.13/site-packages/claude_agent_sdk/_internal/transport/

- `__init__.py` — Transport implementations for Claude SDK. (~566 tok)
- `subprocess_cli.py` — Subprocess transport implementation using Claude Code CLI. (~7757 tok)

## .venv/lib/python3.13/site-packages/click-8.3.2.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares toolkit (~699 tok)
- `RECORD` (~675 tok)
- `WHEEL` (~22 tok)

## .venv/lib/python3.13/site-packages/click-8.3.2.dist-info/licenses/

- `LICENSE.txt` (~369 tok)

## .venv/lib/python3.13/site-packages/click/

- `__init__.py` (~1278 tok)
- `_compat.py` — URL configuration (~5341 tok)
- `_termui_impl.py` — ProgressBar: render_finish, pct, time_per_iteration, eta + 11 more (~7741 tok)
- `_textwrap.py` — TextWrapper: extra_indent, indent_only (~400 tok)
- `_utils.py` — Declares import (~270 tok)
- `_winconsole.py` — This module is based on the excellent work by Adam Bartoš who (~2419 tok)
- `core.py` — ParameterSource: batch, augment_usage_errors, iter_params_for_processing, sort_key (~37973 tok)
- `decorators.py` — to: pass_context, new_func, pass_obj, new_func + 24 more (~5275 tok)
- `exceptions.py` — ClickException: format_message, show, show, format_message + 4 more (~2844 tok)
- `formatting.py` — Can force a width.  This is used by the test system (~2780 tok)
- `globals.py` — get_current_context, get_current_context, get_current_context, push_context + 2 more (~550 tok)
- `parser.py` — _Option: takes_value, process, process, add_option + 2 more (~5432 tok)
- `py.typed` (~0 tok)
- `shell_completion.py` — CompletionItem: shell_complete, func_name, source_vars, source + 9 more (~5999 tok)
- `termui.py` — hidden_prompt_func, prompt, prompt_func, confirm + 4 more (~8868 tok)
- `testing.py` — EchoingStdin: read, read1, readline, readlines + 15 more (~5423 tok)
- `types.py` — ParamType: to_info_dict, get_metavar, get_missing_message, convert + 14 more (~11408 tok)
- `utils.py` — URL configuration (~5788 tok)

## .venv/lib/python3.13/site-packages/cryptography-46.0.7.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` (~1533 tok)
- `RECORD` (~4287 tok)
- `WHEEL` (~29 tok)

## .venv/lib/python3.13/site-packages/cryptography-46.0.7.dist-info/licenses/

- `LICENSE` — Project license (~53 tok)
- `LICENSE.APACHE` — Declares name (~3030 tok)
- `LICENSE.BSD` (~409 tok)

## .venv/lib/python3.13/site-packages/cryptography/

- `__about__.py` — This file is dual licensed under the terms of the Apache License, Version (~128 tok)
- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~104 tok)
- `exceptions.py` — This file is dual licensed under the terms of the Apache License, Version (~311 tok)
- `fernet.py` — This file is dual licensed under the terms of the Apache License, Version (~1990 tok)
- `py.typed` (~0 tok)
- `utils.py` — This file is dual licensed under the terms of the Apache License, Version (~1243 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~130 tok)
- `_oid.py` — This file is dual licensed under the terms of the Apache License, Version (~4926 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/asn1/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~84 tok)
- `asn1.py` — This file is dual licensed under the terms of the Apache License, Version (~1103 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/backends/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~104 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/backends/openssl/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~88 tok)
- `backend.py` — This file is dual licensed under the terms of the Apache License, Version (~2919 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/bindings/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~52 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/bindings/_rust/

- `__init__.pyi` — This file is dual licensed under the terms of the Apache License, Version (~336 tok)
- `_openssl.pyi` — This file is dual licensed under the terms of the Apache License, Version (~62 tok)
- `asn1.pyi` — This file is dual licensed under the terms of the Apache License, Version (~95 tok)
- `declarative_asn1.pyi` — This file is dual licensed under the terms of the Apache License, Version (~238 tok)
- `exceptions.pyi` — This file is dual licensed under the terms of the Apache License, Version (~171 tok)
- `ocsp.pyi` — This file is dual licensed under the terms of the Apache License, Version (~1072 tok)
- `pkcs12.pyi` — This file is dual licensed under the terms of the Apache License, Version (~428 tok)
- `pkcs7.pyi` — This file is dual licensed under the terms of the Apache License, Version (~427 tok)
- `test_support.pyi` — This file is dual licensed under the terms of the Apache License, Version (~202 tok)
- `x509.pyi` — This file is dual licensed under the terms of the Apache License, Version (~2610 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/bindings/_rust/openssl/

- `__init__.pyi` — This file is dual licensed under the terms of the Apache License, Version (~406 tok)
- `aead.pyi` — This file is dual licensed under the terms of the Apache License, Version (~717 tok)
- `ciphers.pyi` — This file is dual licensed under the terms of the Apache License, Version (~351 tok)
- `cmac.pyi` — This file is dual licensed under the terms of the Apache License, Version (~151 tok)
- `dh.pyi` — This file is dual licensed under the terms of the Apache License, Version (~418 tok)
- `dsa.pyi` — This file is dual licensed under the terms of the Apache License, Version (~347 tok)
- `ec.pyi` — This file is dual licensed under the terms of the Apache License, Version (~451 tok)
- `ed25519.pyi` — This file is dual licensed under the terms of the Apache License, Version (~142 tok)
- `ed448.pyi` — This file is dual licensed under the terms of the Apache License, Version (~138 tok)
- `hashes.pyi` — This file is dual licensed under the terms of the Apache License, Version (~263 tok)
- `hmac.pyi` — This file is dual licensed under the terms of the Apache License, Version (~188 tok)
- `kdf.pyi` — This file is dual licensed under the terms of the Apache License, Version (~542 tok)
- `keys.pyi` — This file is dual licensed under the terms of the Apache License, Version (~244 tok)
- `poly1305.pyi` — This file is dual licensed under the terms of the Apache License, Version (~156 tok)
- `rsa.pyi` — This file is dual licensed under the terms of the Apache License, Version (~364 tok)
- `x25519.pyi` — This file is dual licensed under the terms of the Apache License, Version (~140 tok)
- `x448.pyi` — This file is dual licensed under the terms of the Apache License, Version (~135 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/bindings/openssl/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~52 tok)
- `_conditional.py` — This file is dual licensed under the terms of the Apache License, Version (~1655 tok)
- `binding.py` — This file is dual licensed under the terms of the Apache License, Version (~1318 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/decrepit/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~62 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/decrepit/ciphers/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~62 tok)
- `algorithms.py` — This file is dual licensed under the terms of the Apache License, Version (~742 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~52 tok)
- `_asymmetric.py` — This file is dual licensed under the terms of the Apache License, Version (~152 tok)
- `_cipheralgorithm.py` — This file is dual licensed under the terms of the Apache License, Version (~435 tok)
- `_serialization.py` — This file is dual licensed under the terms of the Apache License, Version (~1464 tok)
- `cmac.py` — This file is dual licensed under the terms of the Apache License, Version (~97 tok)
- `constant_time.py` — This file is dual licensed under the terms of the Apache License, Version (~121 tok)
- `hashes.py` — This file is dual licensed under the terms of the Apache License, Version (~1482 tok)
- `hmac.py` — This file is dual licensed under the terms of the Apache License, Version (~121 tok)
- `keywrap.py` — This file is dual licensed under the terms of the Apache License, Version (~1615 tok)
- `padding.py` — This file is dual licensed under the terms of the Apache License, Version (~533 tok)
- `poly1305.py` — This file is dual licensed under the terms of the Apache License, Version (~102 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/asymmetric/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~52 tok)
- `dh.py` — This file is dual licensed under the terms of the Apache License, Version (~1042 tok)
- `dsa.py` — This file is dual licensed under the terms of the Apache License, Version (~1204 tok)
- `ec.py` — This file is dual licensed under the terms of the Apache License, Version (~3840 tok)
- `ed25519.py` — This file is dual licensed under the terms of the Apache License, Version (~1058 tok)
- `ed448.py` — This file is dual licensed under the terms of the Apache License, Version (~1066 tok)
- `padding.py` — This file is dual licensed under the terms of the Apache License, Version (~816 tok)
- `rsa.py` — This file is dual licensed under the terms of the Apache License, Version (~2373 tok)
- `types.py` — This file is dual licensed under the terms of the Apache License, Version (~856 tok)
- `utils.py` — This file is dual licensed under the terms of the Apache License, Version (~226 tok)
- `x25519.py` — This file is dual licensed under the terms of the Apache License, Version (~1033 tok)
- `x448.py` — This file is dual licensed under the terms of the Apache License, Version (~1041 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/ciphers/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~195 tok)
- `aead.py` — This file is dual licensed under the terms of the Apache License, Version (~182 tok)
- `algorithms.py` — This file is dual licensed under the terms of the Apache License, Version (~974 tok)
- `base.py` — This file is dual licensed under the terms of the Apache License, Version (~1216 tok)
- `modes.py` — This file is dual licensed under the terms of the Apache License, Version (~2377 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/kdf/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~215 tok)
- `argon2.py` — This file is dual licensed under the terms of the Apache License, Version (~132 tok)
- `concatkdf.py` — This file is dual licensed under the terms of the Apache License, Version (~1068 tok)
- `hkdf.py` — This file is dual licensed under the terms of the Apache License, Version (~156 tok)
- `kbkdf.py` — This file is dual licensed under the terms of the Apache License, Version (~2619 tok)
- `pbkdf2.py` — This file is dual licensed under the terms of the Apache License, Version (~560 tok)
- `scrypt.py` — This file is dual licensed under the terms of the Apache License, Version (~169 tok)
- `x963kdf.py` — This file is dual licensed under the terms of the Apache License, Version (~572 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/serialization/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~488 tok)
- `base.py` — This file is dual licensed under the terms of the Apache License, Version (~176 tok)
- `pkcs12.py` — This file is dual licensed under the terms of the Apache License, Version (~1459 tok)
- `pkcs7.py` — This file is dual licensed under the terms of the Apache License, Version (~3984 tok)
- `ssh.py` — This file is dual licensed under the terms of the Apache License, Version (~15343 tok)

## .venv/lib/python3.13/site-packages/cryptography/hazmat/primitives/twofactor/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~74 tok)
- `hotp.py` — This file is dual licensed under the terms of the Apache License, Version (~931 tok)
- `totp.py` — This file is dual licensed under the terms of the Apache License, Version (~472 tok)

## .venv/lib/python3.13/site-packages/cryptography/x509/

- `__init__.py` — This file is dual licensed under the terms of the Apache License, Version (~2360 tok)
- `base.py` — This file is dual licensed under the terms of the Apache License, Version (~7999 tok)
- `certificate_transparency.py` — This file is dual licensed under the terms of the Apache License, Version (~228 tok)
- `extensions.py` — This file is dual licensed under the terms of the Apache License, Version (~22207 tok)
- `general_name.py` — This file is dual licensed under the terms of the Apache License, Version (~2239 tok)
- `name.py` — This file is dual licensed under the terms of the Apache License, Version (~4315 tok)
- `ocsp.py` — This file is dual licensed under the terms of the Apache License, Version (~3629 tok)
- `oid.py` — This file is dual licensed under the terms of the Apache License, Version (~266 tok)
- `verification.py` — This file is dual licensed under the terms of the Apache License, Version (~274 tok)

## .venv/lib/python3.13/site-packages/dotenv/

- `__init__.py` — load_ipython_extension, get_cli_string (~352 tok)
- `__main__.py` — Entry point for cli, enables execution with `python -m dotenv` (~37 tok)
- `cli.py` — enumerate_env, cli, stream_file, list_values + 5 more (~1870 tok)
- `ipython.py` — class: dotenv, load_ipython_extension (~379 tok)
- `main.py` — A type alias for a string path to be used for the paths in this file. (~4196 tok)
- `parser.py` — Original: make_regex, start, set, advance + 13 more (~1480 tok)
- `py.typed` — Marker file for PEP 561 (~7 tok)
- `variables.py` — Atom: resolve, resolve, resolve, parse_variables (~671 tok)
- `version.py` (~7 tok)

## .venv/lib/python3.13/site-packages/h11-0.16.0.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` (~2227 tok)
- `RECORD` (~488 tok)
- `top_level.txt` (~1 tok)
- `WHEEL` (~25 tok)

## .venv/lib/python3.13/site-packages/h11-0.16.0.dist-info/licenses/

- `LICENSE.txt` (~281 tok)

## .venv/lib/python3.13/site-packages/h11/

- `__init__.py` — A highish-level implementation of the HTTP/1.1 wire protocol (RFC 7230), (~431 tok)
- `_abnf.py` — We use native strings for all the re patterns, to take advantage of string (~1376 tok)
- `_connection.py` — This contains the main Connection class. Everything in h11 revolves around (~7676 tok)
- `_events.py` — High level events that make up HTTP/1.1 conversations. Loosely inspired by (~3370 tok)
- `_headers.py` — Headers: raw_items, normalize_and_validate, normalize_and_validate, normalize_and_validate + 4 more (~2975 tok)
- `_readers.py` — Code to read HTTP data (~2455 tok)
- `_receivebuffer.py` — ReceiveBuffer: maybe_extract_at_most, maybe_extract_next_line, maybe_extract_lines, is_next_line_obviously_invalid_request_line (~1501 tok)
- `_state.py` — ############################################################### (~3781 tok)
- `_util.py` — ProtocolError: validate, bytesify (~1397 tok)
- `_version.py` — This file must be kept very simple, because it is consumed from several (~196 tok)
- `_writers.py` — Code to read HTTP data (~1452 tok)
- `py.typed` (~2 tok)

## .venv/lib/python3.13/site-packages/httpcore-1.0.9.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares html (~5741 tok)
- `RECORD` (~1270 tok)
- `WHEEL` (~24 tok)

## .venv/lib/python3.13/site-packages/httpcore-1.0.9.dist-info/licenses/

- `LICENSE.md` (~380 tok)

## .venv/lib/python3.13/site-packages/httpcore/

- `__init__.py` — Declares is (~985 tok)
- `_api.py` — request, stream (~899 tok)
- `_exceptions.py` — ConnectionNotAvailable: map_exceptions (~339 tok)
- `_models.py` — Functions for typechecking... (~5036 tok)
- `_ssl.py` — default_ssl_context (~54 tok)
- `_synchronization.py` — Our async synchronization primatives use either 'anyio' or 'trio' depending (~2696 tok)
- `_trace.py` — Trace: trace, atrace (~1130 tok)
- `_utils.py` — is_socket_readable (~440 tok)
- `py.typed` (~0 tok)

## .venv/lib/python3.13/site-packages/httpcore/_async/

- `__init__.py` — Declares AsyncHTTP2Connection (~349 tok)
- `connection_pool.py` — AsyncPoolRequest: assign_to_connection, clear_connection, wait_for_connection, is_queued + 3 more (~4945 tok)
- `connection.py` — AsyncHTTPConnection: exponential_backoff, handle_async_request, can_handle_request, aclose + 5 more (~2414 tok)
- `http_proxy.py` — AsyncHTTPProxy: merge_headers, create_connection, handle_async_request, can_handle_request + 7 more (~4201 tok)
- `http11.py` — HTTPConnectionState: handle_async_request, aclose, can_handle_request, is_available + 4 more (~3966 tok)
- `http2.py` — HTTPConnectionState: has_body_headers, handle_async_request (~6839 tok)
- `interfaces.py` — AsyncRequestInterface: request, stream, handle_async_request, aclose + 6 more (~1273 tok)
- `socks_proxy.py` — AsyncSOCKSProxy: create_connection, handle_async_request, can_handle_request (~3955 tok)

## .venv/lib/python3.13/site-packages/httpcore/_backends/

- `__init__.py` (~0 tok)
- `anyio.py` — AnyIOStream: read, write, aclose, start_tls + 4 more (~1501 tok)
- `auto.py` — AutoBackend: connect_tcp, connect_unix_socket, sleep (~475 tok)
- `base.py` — NetworkStream: read, write, close, start_tls + 12 more (~870 tok)
- `mock.py` — MockSSLObject: selected_alpn_protocol, read, write, close + 13 more (~1165 tok)
- `sync.py` — TLSinTLSStream: read, write, close, start_tls + 8 more (~2280 tok)
- `trio.py` — TrioStream: read, write, aclose, start_tls + 4 more (~1714 tok)

## .venv/lib/python3.13/site-packages/httpcore/_sync/

- `__init__.py` — Declares HTTP2Connection (~326 tok)
- `connection_pool.py` — PoolRequest: assign_to_connection, clear_connection, wait_for_connection, is_queued + 3 more (~4845 tok)
- `connection.py` — HTTPConnection: exponential_backoff, handle_request, can_handle_request, close + 5 more (~2354 tok)
- `http_proxy.py` — HTTPProxy: merge_headers, create_connection, handle_request, can_handle_request + 7 more (~4133 tok)
- `http11.py` — HTTPConnectionState: handle_request, close, can_handle_request, is_available + 5 more (~3851 tok)
- `http2.py` — HTTPConnectionState: has_body_headers, handle_request (~6686 tok)
- `interfaces.py` — RequestInterface: request, stream, handle_request, close + 6 more (~1242 tok)
- `socks_proxy.py` — SOCKSProxy: create_connection, handle_request, can_handle_request, close + 1 more (~3890 tok)

## .venv/lib/python3.13/site-packages/httpx-0.28.1.dist-info/

- `entry_points.txt` (~10 tok)
- `INSTALLER` (~2 tok)
- `METADATA` — Declares html (~1880 tok)
- `RECORD` (~940 tok)
- `WHEEL` (~24 tok)

## .venv/lib/python3.13/site-packages/httpx-0.28.1.dist-info/licenses/

- `LICENSE.md` (~377 tok)

## .venv/lib/python3.13/site-packages/httpx/

- `__init__.py` — main (~621 tok)
- `__version__.py` (~31 tok)
- `_api.py` — to: request, stream, get, options + 5 more (~3356 tok)
- `_auth.py` — Auth: auth_flow, sync_auth_flow, async_auth_flow, auth_flow + 4 more (~3398 tok)
- `_client.py` — UseClientDefault: close, aclose, is_closed, trust_env + 15 more (~18776 tok)
- `_config.py` — UnsetType: create_ssl_context, as_dict, raw_auth (~2442 tok)
- `_content.py` — ByteStream: encode_content, encode_urlencoded_data, encode_multipart_data, encode_text + 4 more (~2332 tok)
- `_decoders.py` — ContentDecoder: decode, flush, decode, flush + 18 more (~3441 tok)
- `_exceptions.py` — HTTPError: request, request, request_context (~2434 tok)
- `_main.py` — SQLAlchemy model (~4465 tok)
- `_models.py` — View: get, update (~12772 tok)
- `_multipart.py` — DataField: replacer, get_multipart_boundary_from_content_type, render_headers, render_data + 9 more (~2813 tok)
- `_status_codes.py` — codes: get_reason_phrase, is_informational, is_success, is_redirect + 3 more (~1612 tok)
- `_types.py` — SyncByteStream: close, aclose (~848 tok)
- `_urlparse.py` — URL configuration (~5299 tok)
- `_urls.py` — URL configuration (~6148 tok)
- `_utils.py` — URLPattern: primitive_value_to_str, get_environment_proxies, to_bytes, to_str + 7 more (~2368 tok)
- `py.typed` (~0 tok)

## .venv/lib/python3.13/site-packages/httpx/_transports/

- `__init__.py` (~79 tok)
- `asgi.py` — ASGIResponseStream: is_running_trio, create_event, handle_async_request, receive + 1 more (~1572 tok)
- `base.py` — BaseTransport: handle_request, close, handle_async_request, aclose (~721 tok)
- `default.py` — ResponseStream: map_httpcore_exceptions, close, handle_request, close + 1 more (~3996 tok)
- `mock.py` — MockTransport: handle_request, handle_async_request (~352 tok)
- `wsgi.py` — WSGIByteStream: close, handle_request, start_response (~1379 tok)

## .venv/lib/python3.13/site-packages/httpx_sse-0.4.3.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares is (~2579 tok)
- `RECORD` (~324 tok)
- `top_level.txt` (~3 tok)
- `WHEEL` (~25 tok)

## .venv/lib/python3.13/site-packages/httpx_sse-0.4.3.dist-info/licenses/

- `LICENSE` — Project license (~286 tok)

## .venv/lib/python3.13/site-packages/httpx_sse/

- `__init__.py` (~81 tok)
- `_api.py` — EventSource: response, iter_sse, aiter_sse, connect_sse + 1 more (~834 tok)
- `_decoders.py` — SSELineDecoder: decode, flush, decode (~1145 tok)
- `_exceptions.py` — Declares SSEError (~18 tok)
- `_models.py` — ServerSentEvent: event, data, id, retry + 1 more (~349 tok)
- `py.typed` (~0 tok)

## .venv/lib/python3.13/site-packages/idna-3.11.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` — Declares issue (~2212 tok)
- `RECORD` (~372 tok)
- `WHEEL` (~22 tok)

## .venv/lib/python3.13/site-packages/idna-3.11.dist-info/licenses/

- `LICENSE.md` (~386 tok)

## .venv/lib/python3.13/site-packages/idna/

- `__init__.py` (~248 tok)
- `codec.py` — Codec: encode, decode, search_function (~983 tok)
- `compat.py` — ToASCII, ToUnicode, nameprep (~91 tok)
- `core.py` — IDNAError: valid_label_length, valid_string_length, check_bidi, check_initial_combiner + 9 more (~3785 tok)
- `idnadata.py` — This file is automatically generated by tools/idna-data (~22750 tok)
- `intranges.py` — intranges_from_list, intranges_contain (~543 tok)
- `package_data.py` (~6 tok)
- `py.typed` (~0 tok)
- `uts46data.py` — This file is automatically generated by tools/idna-data (~67061 tok)

## .venv/lib/python3.13/site-packages/jsonschema/

- `__init__.py` (~1126 tok)
- `__main__.py` (~33 tok)
- `_format.py` — FormatChecker: checks, cls_checks, check, conforms + 19 more (~4448 tok)
- `_keywords.py` — patternProperties, propertyNames, additionalProperties, items + 28 more (~4272 tok)
- `_legacy_keywords.py` — ignore_ref_siblings, dependencies_draft3, dependencies_draft4_draft6_draft7, disallow_draft3 + 13 more (~4341 tok)
- `_types.py` — TypeChecker: is_array, is_bool, is_integer, is_null + 8 more (~1559 tok)
- `_typing.py` — Declares SchemaKeywordValidator (~177 tok)
- `_utils.py` — URIDict: normalize, format_as_index, find_additional_properties, extras_msg + 7 more (~3046 tok)
- `cli.py` — _CannotLoadFile: from_arguments, load, filenotfound_error, parsing_error + 14 more (~2413 tok)
- `exceptions.py` — URL configuration (~4359 tok)
- `protocols.py` — Validator: check_schema, is_type, is_valid, iter_errors + 2 more (~2057 tok)
- `validators.py` — decorator: validates, create, evolve, check_schema + 3 more (~13474 tok)

## .venv/lib/python3.13/site-packages/jsonschema/benchmarks/

- `__init__.py` (~20 tok)
- `const_vs_enum.py` — Declares valid (~238 tok)
- `contains.py` (~225 tok)
- `import_benchmark.py` — import_time (~223 tok)
- `issue232.py` (~149 tok)
- `json_schema_test_suite.py` (~92 tok)
- `nested_schemas.py` — nested_schema (~541 tok)
- `subcomponents.py` — registry_data_structures, registry_add (~318 tok)
- `unused_registry.py` (~269 tok)
- `useless_applicator_schemas.py` (~955 tok)
- `useless_keywords.py` (~248 tok)
- `validator_creation.py` (~82 tok)

## .venv/lib/python3.13/site-packages/jsonschema/benchmarks/issue232/

- `issue.json` — Declares of (~33459 tok)

## .venv/lib/python3.13/site-packages/jsonschema/tests/

- `__init__.py` (~0 tok)
- `_suite.py` — Suite: benchmark, version, benchmark, cases + 12 more (~2393 tok)
- `fuzz_validate.py` — test_schemas, main (~319 tok)
- `test_cli.py` — Tests: invalid_instance, invalid_instance_pretty_output, invalid_instance_explicit_plain_output, invalid_instance_multiple_errors + 10 more (~8156 tok)
- `test_deprecations.py` — Tests: version, validators_ErrorTree, import_ErrorTree, ErrorTree_setitem + 16 more (~4502 tok)
- `test_exceptions.py` — Tests: shallower_errors_are_better_matches, oneOf_and_anyOf_are_weak_matches, if_the_most_relevant_error_is_anyOf_it_is_traversed, no_anyOf_travers... (~6944 tok)
- `test_format.py` — Tests: it_can_validate_no_formats, it_raises_a_key_error_for_unknown_formats, it_can_register_cls_checkers, it_can_register_checkers + 4 more (~911 tok)
- `test_jsonschema_test_suite.py` — Test file (~2418 tok)
- `test_types.py` — Tests: is_type, is_unknown_type, checks_can_be_added_at_init, redefine_existing_type + 11 more (~1994 tok)
- `test_utils.py` — Tests: none, nan, equal_dictionaries, equal_dictionaries_with_nan + 22 more (~1190 tok)
- `test_validators.py` — Tests: attrs, init, iter_errors_successful, iter_errors_one_error + 23 more (~25129 tok)

## .venv/lib/python3.13/site-packages/jsonschema/tests/typing/

- `__init__.py` (~0 tok)
- `test_all_concrete_validators_match_protocol.py` — Test file (~354 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications-2025.9.1.dist-info/

- `INSTALLER` (~2 tok)
- `METADATA` (~776 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications-2025.9.1.dist-info/licenses/

- `COPYING` (~282 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/

- `__init__.py` (~111 tok)
- `_core.py` — URL patterns: 1 routes (~326 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft201909/

- `metaschema.json` (~510 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft201909/vocabularies/

- `applicator` (~496 tok)
- `content` (~138 tok)
- `core` (~409 tok)
- `format` (~108 tok)
- `meta-data` (~238 tok)
- `validation` (~756 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft202012/

- `metaschema.json` (~701 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft202012/vocabularies/

- `applicator` (~443 tok)
- `content` (~139 tok)
- `core` (~418 tok)
- `format-annotation` (~120 tok)
- `format-assertion` (~119 tok)
- `meta-data` (~238 tok)
- `unevaluated` (~135 tok)
- `validation` (~756 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft3/

- `metaschema.json` (~743 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft4/

- `metaschema.json` (~1245 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft6/

- `metaschema.json` (~1268 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/schemas/draft7/

- `metaschema.json` (~1377 tok)

## .venv/lib/python3.13/site-packages/jsonschema_specifications/tests/

- `__init__.py` (~0 tok)
- `test_jsonschema_specifications.py` — Tests: it_contains_metaschemas, it_is_crawled, it_copes_with_dotfiles (~316 tok)
