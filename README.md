# Quack

Local push-to-talk dictation for macOS.

Hold a key, talk, let go, and the text is pasted into whatever app you were in. Everything runs on the Mac, your audio & text never leave the machine. Currently running [Phonon-2](https://huggingface.co/FermionResearch/Phonon-2-CoreML) on the Neural Engine. No account, no API key, and it works offline.

[Download](https://updates.tired.dev/quack). Apple silicon, macOS 15 or later. The app is 5 MB and downloads a 215 MB speech model on first launch.

## Dictating

Hold `fn` and talk. The words appear in a pill at the bottom of the screen while you speak. Release the key and the text is pasted into the focused app in one edit, then your clipboard is restored. Settings has a press-to-start, press-to-stop mode. Esc cancels.

A toggleable cleanup feature removes filler words and stutters, and spoken corrections are applied. "Let's meet Monday, sorry, Thursday" types as "Let's meet Thursday". "Push the beta, actually make that the final build" types as "push the final build". "Scratch that" drops the sentence before it. The pill shows the removed words struck through.

Ending with "send it" types the text and presses Return. "Trash what I said" discards the dictation. The phrases are long so that ordinary speech does not trigger them.

When enabled, a "use words on screen" feature allows Quack to read the text of the window it is about to type into. Such as the open file or the email you are replying to, and uses the names, identifiers, and acronyms it finds there to guide recognition for that dictation. Saying "fetch user profile" with `fetchUserProfile` on screen types `fetchUserProfile`. The text is read on the Mac and not saved.

Speakers that are playing are muted while you talk and restored afterwards. Headphones are left alone.

The menu bar shows your recent dictations. Click one to copy it.

## Dictionary

The words a speech model gets wrong are usually the ones specific to you: product names, people, the libraries in your codebase. Quack has a dictionary for these. Each word can have "heard as" forms, so `kubectl` is typed when the model hears "cube control".

Quack comes with a command line tool, `quackctl`, so the dictionary can be filled by a script or a coding agent instead of by hand. An agent can read through a project and add the names Quack is likely to mishear:

```sh
quackctl add Tauri Bun
quackctl add kubectl --heard-as "cube control"
jq -r '.dependencies | keys[]' package.json | quackctl add
```

Every dictionary change is recorded with who made it and can be undone, in Settings or with `quackctl undo`. `quackctl usage` shows how often each word fired, so misfiring words can be found. `quackctl dictate --audio file.aiff` dictates a recording instead of the microphone, which lets an agent check a word without using your microphone or typing into your apps.

Other apps can use the same local API to start and stop dictation, or to receive the text instead of having it typed. Each app asks for permission the first time. See the [control API docs](https://updates.tired.dev/quack/control-api).

## Privacy

Audio and text are processed on the Mac. Quack makes two kinds of network request: the speech model download, and a daily check for signed updates. Recent dictations are stored encrypted on disk, and Clear History in the menu bar deletes them.

## This repository

This repository holds Quack's signed downloads, update feed, and website. Phonon-2 weights are distributed under CC-BY-4.0 by Fermion Research, derived from NVIDIA Parakeet TDT 0.6B v3. The NOTICE and license ship inside the app. Publishing notes are in [PUBLISHING.md](PUBLISHING.md).
