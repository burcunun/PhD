import React from 'react';
import { Box, Typography, Button } from '@mui/material';
import style from './style';
import DocumentsGridContainer from '../DocumentsGrid/DocumentsGridContainer';
import PuffLoader from 'react-spinners/PuffLoader';
import theme from '../../theme';
import { motion } from 'framer-motion';

export default function ResultsBox(props) {
  const classes = style();

  const variants = {
    before: {
      height: '75vh',
      display: 'flex',
    },
    after: {
      height: '100%',
      display: 'inline-block',
      transition: {
        duration: 2,
      },
    },
  };

  return (
    <motion.div
      variants={variants}
      animate={props.showResults ? 'after' : 'before'}
      className={classes.mainContainer}
    >
      {props.showResults && (
        <Box className={classes.infoContainer}>
          <Typography variant="caption" color="primary.dark">
            Info: The <strong>Highlighted</strong> documents do not contain the
            query words in their title.
          </Typography>
          <Typography variant="caption" color="primary.dark">
            You can click "<em>Table Search</em>" in the navbar to view a more
            detailed result.
          </Typography>
        </Box>
      )}

      <Box className={classes.loaderContainer}>
        <PuffLoader
          color={theme.palette.primary.main}
          loading={props.resultsLoading}
          size={50}
        />
      </Box>

      {props.showResults && (
        <Box className={classes.documentsContainer}>
          <DocumentsGridContainer />
        </Box>
      )}
    </motion.div>
  );
}
