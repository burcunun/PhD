import React from 'react';
import { Box } from '@mui/material';
import Document from './Document';

export default function DocumentContainer(props) {
  return (
    <Box>
      <Document
        title={props.title}
        summary={props.summary}
        source={props.source}
        exists={props.exists}
      />
    </Box>
  );
}
