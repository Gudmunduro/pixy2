# Pixy 2

Pixy 2 SDK with more functions inside the python interface

# Python interface functions

```cpp
int init();
```


```cpp
int changeProg(const char* program_name);
```


```cpp
int getFrameWidth();
```


```cpp
int getFrameHeight();
```


```cpp
void videoGetRGB(int X, int Y, uint8_t * Red, uint8_t * Green, uint8_t * Blue);
```


```cpp
int cccGetBlocks(int max_blocks, struct Block * blocks);
```


```cpp
void lineGetAllFeatures();
```


```cpp
void lineGetMainFeatures();
```


```cpp
int lineGetVectors(int max_vectors, struct Vector * vectors);
```


```cpp
int lineGetIntersections(int max_intersections, struct IntersectionLine * intersections);
```


```cpp
int lineGetBarcodes(int max_barcodes, struct Barcode * barcodes);
```


```cpp
void setServos(int S1_Position, int S2_Position);
```


```cpp
void setNextTurn(int deg);
```


```cpp
void setLamp(bool upper, bool lower);
```


```cpp
void setMode(bool turnDelayed, bool manualVector, bool whiteLine);
```
