#!/bin/bash
# Script to make a request that causes the server to respond with "You got me!"
curl -sLX PUT "0.0.0.0:5000/catch_me" -H "Origin:You got me!"
