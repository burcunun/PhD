import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  mainContainer: {
    borderRadius: '15px',
    background: theme.palette.teritary.main,
    boxShadow: ' 0px 1px 5px rgba(0, 0, 0, 0.15)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  infoContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    padding: '1.5rem',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  pagesInfoContainer: {
    display: 'flex',
    padding: '1.5rem',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  documentsContainer: {},
  loaderContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
});
export default style;
