#include "regex.h"
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


char *ConvertSpecial(const char *line) {
  /* Walk through line converting special characters */
  /* Overallocate output */
  char *out = malloc(strlen(line) + 1);

  size_t outpos = 0;  
  size_t pos = 0;

  while(pos < strlen(line)) {
    if (line[pos] == '\\') {
      if (line[pos+1] == '\\') {
	out[outpos] = '\\';
	pos += 2;
	outpos++;
      } else if (line[pos+1] == '\t') {
	out[outpos] = '\t';
	pos += 2;
	outpos++;
      } else if (line[pos+1] == '\n') {
	out[outpos] = '\n';
	pos += 2;
	outpos++;
      } else {
	out[outpos] = line[pos];
	pos++;
	outpos++;
      }
    } else {
      out[outpos] = line[pos];
      pos++;
      outpos++;
    }
  }
  /* fprintf(stderr, "CKP1: %s\n", out); */
  out[outpos] = '\0';
  return out;
}

int main(int argc, char *argv[])
{

  regex_t preg;
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
    /* remove newline */
    size_t len = strlen(line);
    if( line[len-1] == '\n' )
      line[len-1] = 0;

    char * pattern = ConvertSpecial(line);
    /* printf("%s\n", line); */
    if (rcsb_regcomp(&preg, pattern, REG_EXTENDED|REG_NOSUB) != 0) {
      fprintf(stderr, "Could not compile pattern %s\n", line);
      exitcode = 1;
    }
    rcsb_regfree(&preg);
    free(pattern);
  }

  fclose(fin);
  free(line);
  exit(exitcode);
   
}
