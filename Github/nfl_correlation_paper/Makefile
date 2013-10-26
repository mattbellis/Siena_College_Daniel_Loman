# Makefile for latex sources.
# attention: 

PROJECT   = paper

TEX_FILES = $(shell ls *.tex)
EPS_FILES = $(shell ls figures/*.*pdf >& /dev/null)

all:  $(PROJECT)

$(PROJECT).dvi : $(TEX_FILES) $(EPS_FILES) # make the dvi file
	pdflatex  $(PROJECT) 
	bibtex  $(PROJECT) 
	pdflatex  $(PROJECT) 

$(PROJECT) : $(PROJECT).dvi

clean:
	rm -rf $(PROJECT).log
	rm -rf $(PROJECT).aux
	rm -rf $(PROJECT).pdf
	rm -rf $(PROJECT).lot
	rm -rf $(PROJECT).aux
	rm -rf $(PROJECT).blg
	rm -rf $(PROJECT).bbl
	rm -rf paperNotes.bib
	rm -rf texput.log

