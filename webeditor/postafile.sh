#!/bin/bash

curl --data-urlencode "`cat %1`" http://127.0.0.1:5000/go

