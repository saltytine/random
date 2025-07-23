#!/bin/bash
du -sh "${1:-.}"/* 2>/dev/null | sort -hr | head -n 15
