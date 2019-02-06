#include <string.h>
#include "libpixyusb2.h"

Pixy2  pixy_instance;

int init()
{
  return  pixy_instance.init();
}

int changeProg (const char *  program_name)
{
  return pixy_instance.changeProg (program_name);
}

int getFrameWidth ()
{
  return pixy_instance.frameWidth;
}

int getFrameHeight ()
{
  return pixy_instance.frameHeight;
}

void videoGetRGB (int  X, int  Y, uint8_t *  Red, uint8_t *  Green, uint8_t *  Blue)
{
  pixy_instance.video.getRGB (X, Y, Red, Green, Blue);
}

int cccGetBlocks (int  max_blocks, struct Block *  blocks)
{
  int  number_of_blocks_copied;
  int  blocks_available;
  int  index;
  
  // Get number of blocks detected //
  pixy_instance.ccc.getBlocks();
  blocks_available = pixy_instance.ccc.numBlocks;

  // Copy the maximum amount of blocks that can be copied //
  number_of_blocks_copied = (max_blocks >= blocks_available ? blocks_available : max_blocks);   

  // Copy blocks //
  for (index = 0; index != number_of_blocks_copied; ++index)  {
    memcpy (&blocks[index], &pixy_instance.ccc.blocks[index], sizeof (Block));
  }

  return number_of_blocks_copied;
}

void lineGetAllFeatures ()
{
  pixy_instance.line.getAllFeatures();
}

void lineGetMainFeatures ()
{
  pixy_instance.line.getMainFeatures();
}

int lineGetVectors (int  max_vectors, struct Vector *  vectors)
{
  int  number_of_vectors_copied;
  int  vectors_available;
  int  index;

  vectors_available        = pixy_instance.line.numVectors;
  number_of_vectors_copied = (max_vectors >= vectors_available ? vectors_available : max_vectors);

  // Copy vectors //
  for (index = 0; index != number_of_vectors_copied; ++index)  {
    memcpy (&vectors[index], &pixy_instance.line.vectors[index], sizeof (Vector));
  }

  return number_of_vectors_copied;
}

int lineGetIntersections (int  max_intersections, struct IntersectionLine *  intersections)
{
  int  number_of_intersections_copied;
  int  intersections_available;
  int  index;

  intersections_available        = pixy_instance.line.numIntersections;
  number_of_intersections_copied = (max_intersections >= intersections_available ? intersections_available : max_intersections);

  // Copy intersections //
  for (index = 0; index != number_of_intersections_copied; ++index)  {
    memcpy (&intersections[index], &pixy_instance.line.intersections[index], sizeof (Intersection));
  }

  return number_of_intersections_copied;
}

int lineGetBarcodes (int  max_barcodes, struct Barcode *  barcodes)
{
  int  number_of_barcodes_copied;
  int  barcodes_available;
  int  index;

  barcodes_available        = pixy_instance.line.numBarcodes;
  number_of_barcodes_copied = (max_barcodes >= barcodes_available ? barcodes_available : max_barcodes);

  // Copy barcodes //
  for (index = 0; index != number_of_barcodes_copied; ++index) {
    memcpy (&barcodes[index], &pixy_instance.line.barcodes[index], sizeof (Barcode));
  }

  return number_of_barcodes_copied;
}

void setServos (int  S1_Position, int  S2_Position)
{
  pixy_instance.setServos (S1_Position, S2_Position);
}

void setNextTurn(int deg)
{
  pixy_instance.line.setNextTurn(deg); 
}

void setDefaultTurn(int deg)
{
  pixy_instance.line.setDefaultTurn(deg); 
}

int setLamp(int upper, int lower)
{
  return pixy_instance.setLamp(upper, lower);
}

void setMode(bool turnDelayed, bool manualVector, bool whiteLine)
{
  uint8_t mode = 0;
  if (turnDelayed) {
    mode = LINE_MODE_TURN_DELAYED; 
  }
  if (manualVector) {
    mode = mode | LINE_MODE_MANUAL_SELECT_VECTOR;
  }
  if (whiteLine) {
   mode = mode | LINE_MODE_WHITE_LINE; 
  }
  pixy_instance.line.setMode(mode);
}


void setModeWhiteLine()
{
  pixy_instance.line.setMode(LINE_MODE_WHITE_LINE);
}
