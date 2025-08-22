import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      light: '#1d5300',
      main: '#476072',
      dark: '#334257',
      contrastText: '#fff',
    },
    secondary: {
      light: '#fafafa',
      main: '#EEEEEE',
      dark: '#E5E5E5',
      contrastText: '#000',
    },
    teritary: {
      light: '#ffff',
      main: '#f9f9f9',
      dark: '#E5E5E5',
      contrastText: '#334257',
    },
  },
});

export default theme;
