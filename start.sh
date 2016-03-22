#!/bin/bash

uwsgi -s /home/bug/uwsgi.sock --module run --callable app
