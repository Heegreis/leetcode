int distanceBetweenBusStops(int* distance, int distanceSize, int start, int destination){
    int minDis = 0;
    int clockwise = 0;
    int counterclockwise = 0;
    
    int s;
    int d;
    if (start < destination){
        s = start;
        d = destination;
    }
    else{
        s = destination;
        d = start;   
    }
    
    printf("clockwise: ");
    int i = 0;
    for(i = s; i < d; i++){
        printf("[%d] %d ", i, distance[i]);
        clockwise = clockwise + distance[i];
        printf("%d ", clockwise);
    }
    printf("%d ", clockwise);
    
    printf("counterclockwise: ");
    for(i = d; i < distanceSize; i++){
        counterclockwise = counterclockwise + distance[i];
    }
    for(i = 0; i < s; i++){
        counterclockwise = counterclockwise + distance[i];
    }
    
    if (clockwise < counterclockwise)
        minDis = clockwise;
    else
        minDis = counterclockwise;
    
    return minDis;
}