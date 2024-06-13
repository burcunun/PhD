import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  container: {
    borderRadius: '15px',
    boxShadow: ' 0px 1px 5px rgba(0, 0, 0, 0.15)',
    width: '100%',
    //maxWidth: '35rem',
    background: theme.palette.teritary.main,
  },
  textField: {
    width: '100%',
    //maxWidth: '35rem',
    borderRadius: '15px',
    '& > div': { borderRadius: '15px' },
  },
  button: {
    border: 'none',
    height: '3.2rem',
    borderRadius: '5px',
    margin: '0 0.5rem',
    backgroundColor: theme.palette.secondary.main,
  },
  buttonIcon: {
    color: 'white',
    width: '2rem',
    '&:hover': {
      color: 'black',
    },
  },
});
export default style;
