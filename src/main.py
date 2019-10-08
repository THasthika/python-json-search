#!/usr/bin/env python3

import prompt
import search


def main():
    search.SearchManager.getInstance()
    prompt.SearchAppPrompt().loop()


if __name__ == "__main__":
    main()
