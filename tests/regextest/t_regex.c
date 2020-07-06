#include "regex.h"
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

int main(int argc, char *argv[])
{

  regex_t    re;
  char *fname = NULL;
  FILE *fin;
  char *line = NULL;
  size_t len;
  int exitcode = 0;
  
  if (argc != 2) {
    fprintf(stderr, "t_regex fname\n");
    exit(1);
  }
      
  fname = argv[1];
  fin = fopen(fname, "r");

  while(getline(&line, &len, fin) != -1) {
    char * pattern = line;
    if (rcsb_regcomp(&re, pattern, REG_EXTENDED|REG_NOSUB) != 0) {
      fprintf(stderr, "Could not compile pattern %s\n", line);
      exitcode = 1;
    }
  }
  

  fclose(fin);
  free(line);
  exit(exitcode);
   
}
