#!/usr/bin/env python

"""
rna_transcription

Python script for the Python "Rna Transcription", 'exercism' exercise.
Implementation of a program that, given a DNA strand, returns its RNA complement (per RNA transcription).

Created by: shamdela
Date:       19/09/2016
"""

strands = {'G':'C', 'C':'G', 'T':'A', 'A':'U'};


def to_rna(dna):
    rna = [strands[nucleotide] for nucleotide in dna]
    return "".join(str(nucleotide) for nucleotide in rna)
