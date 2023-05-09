static int staticReturnsTrue() {
	Return 1;
}
static int staticReturnsFalse() {
	Return 0;
}
void CWE145_Double_Free_malloc_long() {
	Long *data;
	data = NULL;
	if(staticReturnsTrue()) {
		data = (long *)malloc(100 * sizeof(long));
		if (data == NULL) { exit(-1); }
		free(data);
	}
	if(staticReturnsTrue()) {
		free(data);
	}
}
