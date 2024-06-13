import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  logo: {
    width: '6rem',
    height: '6rem',
  },
  logoContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    textAlign: 'center',
  },
  loading: {
    position: 'absolute',
    left: '50%',
    top: '115%',
    transform: 'translate(-50%, -50%)',
  },
  container: {
    position: 'absolute',
    left: '50%',
    top: '40%',
    transform: 'translate(-50%, -50%)',
  },
  mainContainer: {
    backgroundColor: theme.palette.secondary.dark,
    position: 'relative',
    width: '100vw',
    height: '100vh',
  },
});
export default style;
