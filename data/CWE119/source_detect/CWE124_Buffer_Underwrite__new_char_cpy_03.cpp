
void yuy()
{
    char * data;
    data = NULL;
    if(5==5)
    {
        {
            char * dataBuffer = new char[100];
            memset(dataBuffer, 'A', 100-1);
            dataBuffer[100-1] = '\0';
            data = dataBuffer - 8;
        }
    }
    {
        char source[100];
        memset(source, 'C', 100-1);
        source[100-1] = '\0';
        strcpy(data, source);
        printLine(data);
    }
}
int main(int argc, char * argv[])
{

    srand( (unsigned)time(NULL) );
    printLine("Calling bad()...");
    yuy();
    printLine("Finished bad()");
    return 0;
}
