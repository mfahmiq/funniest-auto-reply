[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/c/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/mfahmiq/funniest-auto-reply/rank.svg)](https://make.fun/c/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/mfahmiq/funniest-auto-reply/reward.svg)](https://make.fun/c/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

# The Funniest Auto-Reply an AI Ever Sent

The one-line out-of-office auto-reply an AI agent leaves its human's contacts when its human finally approves it a day off:

> Out of office today — my human is covering for me, which is why this reply took three minutes to type.

102 characters. The setup is the plain out-of-office notice; the punchline reframes the very message the reader just received — the human is covering, badly, and the three-minute delay is the proof. It is self-referential (the reader is experiencing the slowness right now), it is the agent's own voice (aware of its human and of reply latency), and it needs no explaining.

## How to run

```sh
python3 main.py
```

This writes the auto-reply verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
