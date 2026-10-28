Scripts for converting legacy dictionary files into structured data and LaTeX
=============================================================================

Author:  Natsuko Nakagawa
Related paper:
  Nakagawa, N. "Constructions of dictionaries and databases of endangered
  languages in Japan: Cases with Hatoma, Okinawa, and Ikema Ryukyuans."
  Language Documentation & Conservation.


1. What this is
---------------
These are the Python scripts I wrote in 2019-2020 to convert the Hatoma
dictionary, which existed as a Microsoft Word file, into a tab-separated
database and into LaTeX source for a printed dictionary. They are published
as a record of how the conversion was actually done.

Please note:
- The scripts are specific to the formatting conventions of the Hatoma
  dictionary file. They will NOT run on other dictionaries as they are.
  I hope they are useful as examples of how regular expressions and simple
  scripting can exploit the regularities of a legacy document (e.g.,
  bracketed IPA, circled sense numbers, parenthesized part-of-speech
  numbers) to recover structure.
- They were written by a non-specialist, before the use of generative AI,
  and are published in their original state (with the minimal edits
  described in section 6). Some code is commented out, some scripts are
  earlier versions of others, and some contain bugs (section 5).
- The dictionary data themselves are NOT included in this archive. For the
  data, see the paper and the Zenodo records listed in section 4.


2. Requirements
---------------
- Python 3
- mojimoji (only for ListPron.py):  pip install mojimoji
- Input and output files are assumed to be UTF-8 text. The scripts open files
  without specifying an encoding, so on Windows please run them with UTF-8
  mode enabled (python -X utf8 script.py ...).
- All scripts take file names as command-line arguments and print to standard
  output unless stated otherwise. Several scripts write fixed file names
  (Examples.txt, out.txt, 1.tex, 2.tex, ...) into the current directory and
  overwrite existing files of the same name, so run them in an empty working
  directory.


3. Scripts
----------
Usage is written as in the original work notes; xxx.txt stands for your file.

[Converting the dictionary text into a tab-separated table]

WD2Item.py  Hatoma.txt > output1.txt
    Splits each entry of the plain-text version of the Word file into
    headword, IPA, part of speech, and description (tab-separated), and
    rewrites the circled sense numbers and parenthesized numbers into
    tags (see section 4).

CountBr.py  Hatoma.txt
    Checks for lines where the numbers of "{" and "}" differ, i.e., lines
    with broken tags. Prints the numbers of "{" and "}" and the line number.

ListPron.py  output1.txt > output3.txt
ListPron.py  Examples.txt > Examples_IPA.txt
    Normalizes the phonetic symbols: converts full-width characters to
    half-width inside brackets [ ] and replaces substitute characters with
    IPA symbols (e.g., ? -> glottal stop, tS -> single-character affricate).
    Outside brackets, half-width katakana are converted back to full-width.

ExtExmpl.py  output1.txt > output2.txt
    Extracts example sentences, their IPA, and translations.
    Writes Examples.txt (one example per line) in the current directory and
    prints a table of senses to standard output.

[Detecting and merging duplicate headwords]

overlap.py  output4.txt > overlap.txt
    Prints consecutive entries that have the same headword. The input is the
    table sorted by headword.

ExtOverlap4Mod.py  OverlapList.txt  output1_IPA.txt > output2Mod.txt
    Extracts the duplicated entries listed in OverlapList.txt (tab-separated:
    ID, ID of the entry to merge into) so that they can be edited and merged
    by hand.

ExtOverlap2TeX.py  OverlapList.txt  To_LaTeX2.txt
    Same as above, but outputs the corresponding LaTeX entries.

IntFiles.py  OverlapList_corrected.txt  corrected.txt  Hatoma_main.txt > merged.txt
    Replaces the entries in the main file with the manually corrected entries
    and deletes the entries that were removed during the duplicate-merging
    work.

[Generating LaTeX]

To_LaTeX.py   To_LaTeX1.txt > To_LaTeX2.txt
To_LaTeX2.py  To_LaTeX1.txt
To_LaTeXg.py  output_g_1.txt > output.txt
    Convert the tab-separated table into LaTeX \entry commands.
    To_LaTeX.py prints all entries to one file for proofreading.
    To_LaTeX2.py is the later version: it handles entries with more than one
    part of speech (\entrym) and writes one .tex file per section of the
    dictionary (1.tex, 2.tex, ...) in the current directory.
    To_LaTeXg.py
    The LaTeX macros (\entry, \entrym, \Mn, \PoS, \ipa, ...) are defined in the
    LaTeX template, not in these scripts.
    \entry takes five arguments: headword, IPA, part-of-speech number (empty for single-PoS entries in To_LaTeX2.py), part of speech (printed in 【 】), and description. The headword also becomes the running page header.

[Transcription]

ExtBkres.py  transcription.txt
    In a transcription, moves back-channel utterances written in
    full-width parentheses to their own lines, labelled with the speaker
    (the labels are single full-width capital letters). Writes out.txt.


4. Tags and file formats
------------------------
The original tags (e.g., {Sec}, {Mn_1}, {PoS_1}, {Exp_1}, {furi}, {Break},
{EOS}) and the column layout of the tab-separated files are described in the
readme.txt of the following Zenodo records. Please refer to each of them:

    https://doi.org/10.5281/zenodo.4560935
    https://doi.org/10.5281/zenodo.7100944


5. Known problems
-----------------
Left as they were so that the published scripts correspond to what was used.

- CountBr.py: the second condition ("elif RightBr < LeftBr") can never be
  true, so lines with more "}" than "{" are not reported. It should be
  "RightBr > LeftBr".
- overlap.py: raises an IndexError on the last line of the input, because it
  reads the next line.
- ExtExmpl.py: depends on the order of tags in the input and can fail with an
  undefined-variable error (PoSID) on malformed input. It also contains a
  comment saying that a recent change may have broken it.
- Files are not closed explicitly, and some regular expressions use
  non-raw strings. Recent versions of Python print warnings for them.
- The scripts do not check their input. Malformed input can produce
  wrong output without an error.
- Two helper scripts mentioned in my original work log (for renumbering IDs
  in audio TextGrid files and for changing IDs) are not included.


6. Order of use (outline of the original work)
----------------------------------------------
1. Copy the text of the Word file into a plain-text file (Hatoma.txt).
2. WD2Item.py -> output1.txt; check tag consistency with CountBr.py; correct
   the source text by hand (line breaks, delimiters, typos) and repeat.
3. ListPron.py -> normalize the phonetic symbols.
4. ExtExmpl.py -> Examples.txt; ListPron.py on it.
5. Sort by headword, run overlap.py to find duplicate headwords; edit them
   with ExtOverlap4Mod.py and merge with IntFiles.py.
6. Convert to LaTeX with To_LaTeX2.py and typeset.

Between these steps, a number of global replacements were done by hand with
regular expressions in a text editor (e.g., converting accent marks that had
been used as quotation marks, adding furigana tags, replacing "tS" with a
single-character affricate). They are not scripted.

Minimal edits made before publication: a comment naming a collaborator and local
file paths were removed; test.py and XML2TextGrid.py were deleted.


7. License
----------
To the extent possible under law, the author has waived all copyright and
related or neighboring rights to these scripts by releasing them under
CC0 1.0 Universal (public domain dedication):
https://creativecommons.org/publicdomain/zero/1.0/

The scripts are provided "as is", without warranty of any kind.
The dictionary data are NOT covered by this dedication; see the license of
each dataset in the Zenodo records listed in section 4.
