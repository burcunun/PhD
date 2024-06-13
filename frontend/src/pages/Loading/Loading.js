import React from 'react';
import { Box, Typography } from '@mui/material';
import style from './style';
import PropagateLoader from 'react-spinners/PropagateLoader';
import Logo from '../../assets/logo_v2.png';
import theme from '../../theme';

export default function Loading({ loading }) {
  const classes = style();

  return (
    <Box className={classes.mainContainer}>
      <Box className={classes.container}>
        <Box className={classes.logoContainer}>
          <img className={classes.logo} src={Logo} alt="logo" />
          <Typography variant="h5" color="primary">
            Innovation Sustainability Search Engine
          </Typography>
        </Box>
        <Box className={classes.loading}>
          <PropagateLoader
            color={theme.palette.primary.main}
            loading={loading}
            size={7}
          />
        </Box>
      </Box>
    </Box>
  );
}
