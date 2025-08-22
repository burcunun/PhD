import { React, useEffect } from 'react';
import { Box, ThemeProvider } from '@mui/material';
import HomeContainer from './pages/Home/HomeContainer';
import theme from './theme';
import useMediaQuery from '@mui/material/useMediaQuery';
import { mobileMedia } from './redux/actions/index';
import { useDispatch } from 'react-redux';

function App() {
  const mobile = useMediaQuery('(min-width: 600px)');
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(mobileMedia());
  }, [mobile]);

  return (
    <ThemeProvider theme={theme}>
      <Box className="App">
        <HomeContainer />
      </Box>
    </ThemeProvider>
  );
}

export default App;
