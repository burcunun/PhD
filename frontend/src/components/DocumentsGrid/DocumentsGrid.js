import React from 'react';
import { Box, Grid } from '@mui/material';
import style from './style';
import DocumentContainer from '../Document/DocumentContainer';
import { motion, AnimateSharedLayout } from 'framer-motion';

export default function DocumentsGrid({ results }) {
  const classes = style();

  const item = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
    },
    exit: {
      opacity: 0,
    },
  };

  return (
    <Box className={classes.mainContainer}>
      <Box>
        <Box className={classes.documentsContainer}>
          <AnimateSharedLayout>
            {results.results.map((doc, index) => {
              return (
                <Box key={index} className={classes.documentContainer}>
                  <motion.div
                    layout
                    whileHover={{
                      scale: 1.05,
                    }}
                    whileTap={{ scale: 0.999 }}
                    variants={item}
                  >
                    <DocumentContainer
                      title={doc['_source'].title}
                      summary={doc['_source'].summary}
                      source={doc['_source'].source}
                      exists={doc['_source'].query_term_exists}
                    />
                  </motion.div>
                </Box>
              );
            })}
          </AnimateSharedLayout>
        </Box>
      </Box>
    </Box>
  );
}
