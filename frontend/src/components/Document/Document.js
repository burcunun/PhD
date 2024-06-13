import React from 'react';
import { Box, Card, Typography, CardContent, Link } from '@mui/material';
import style from './style';

export default function Document(props) {
  const classes = style(props);
  return (
    <Link
      href={props.source}
      target="_blank"
      rel="noreferrer"
      className={classes.link}
    >
      <Box>
        <Card className={classes.container}>
          <CardContent className={classes.cardContent}>
            <Typography className={classes.title} color="primary.dark">
              {props.title}
            </Typography>
            <Box className={classes.border} />
            <Typography className={classes.summary} color="primary.dark">
              {props.summary}
            </Typography>
          </CardContent>
        </Card>
      </Box>
    </Link>
  );
}
