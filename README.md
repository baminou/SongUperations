[![Build Status](https://travis-ci.org/baminou/Uperations.svg?branch=master)](https://travis-ci.org/baminou/Uperations)

## Sing Uperations

This python client tools is used to work with a [https://github.com/overture-stack/SONG](Song server)


* Operations: An action that has to be executed.
* Library: A group of operations
* A command to execute in the terminal to run the Operation

## Installation
This project uses python3 and was built using python 3.7.0.
Start by cloning this repository to your local
```bash
pip3 install -r requirements.txt
```

## All available operations in 'sing' library
```bash
./uperation base list:operations | grep sing

sing       upload               Upload              Upload json payload to song
sing       save                 Save                Save a SONG upload ID.
sing       manifest             Manifest            Generate manifest file for upload
sing       publish              Publish             Publish an analysis
sing       status               Status              Retrieve an upload status
```

## Operations
In order to keep the access token hidden, store your token into an environment global variable, and pass the name
of the this variable to the cli if needed.

In a bash terminal
```bash
export ICGC_ACCESS_TOKEN=`My Token`
./uperation sing upload {song_server} ICGC_ACCESS_TOKEN ...
```

### upload

Upload a payload to a SONG server

```python
./uperation sing upload -h
--song-url          song_url        URL of the SONG server
--access-token      access_token    Access token global variable name
--study             study           ICGC study ID
-p/--payload        payload         Path to {payload}.json
```

### save

Save a payload on a SONG server

```python
./uperation sing save -h
--song-url          song_url        URL of the SONG server
--access-token      access_token    Access token global variable name
--study             study           ICGC study ID
-u/--upload-id      upload_id       Upload ID from SONG
```

### manifest

Generate a manifest file from analysis ID

```python
./uperation sing manifest -h
--song-url          song_url       URL of the SONG server
--study             study          ICGC study ID
-a/--analysis-id    analysis_id    Analysis ID
-d/--files-dir      files_dir      Directory where files are located
-m/--manifest       manifest_file  Output manifest path
```

### publish

Publish an existing analysis

```python
./uperation sing publish -h
--song-url          song_url        URL of the SONG server
--study             study           ICGC study ID
--access-token      access_token    Access token global variable name
-a/--analysis-id    analysis_id     Analysis ID
```

### status

Show the status of an existing upload

```python
./uperation sing status -h
--song-url          song_url     URL of the SONG server
--study             study        ICGC study ID
-u/--upload-id      upload_id    Upload ID from SONG
```

### search

Retrieve an analysis ID

```python
./uperation sing search -h
--song-url          song_url     URL of the SONG server
--study             study        ICGC study ID
-a/--analysis-id    analysis_id  Analysis ID to retrieve
```

### validate

Check if a payload is valid

```python
./uperation sing validate -h
payload     Path to JSON payload
```
