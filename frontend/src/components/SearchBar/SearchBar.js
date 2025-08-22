import React from 'react';
import { Box, TextField, IconButton, InputAdornment } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import style from './style';

export default function SearchBar({ handleOnChange, handleOnClick, handleOnEnter }) {
  const classes = style();

  return (
    <Box className={classes.container}>
      <TextField
        label="Search..."
        className={classes.textField}
        onChange={handleOnChange}
        onKeyPress={handleOnEnter}
        InputProps={{
          endAdornment: (
            <InputAdornment position="start">
              <IconButton
                onClick={() => {
                  handleOnClick();
                }}
              >
                <SearchIcon />
              </IconButton>
            </InputAdornment>
          ),
        }}
      />
    </Box>
  );
}
