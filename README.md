# podcast-feed-agent

Convert RSS feeds into a podcast using podcastfy library.

## installation

create the venv environment
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

copy .env.template to .env file 

```
cp .env.template .env
```
and set the api key:
```
OPENAI_API_KEY=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
```
(check https://github.com/souzatharsis/podcastfy for other configuration.)


run run.py:
```
python3 run.py
```


podcast audio saved in data/audio

