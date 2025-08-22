import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  mainContainer: {
    backgroundColor: theme.palette.secondary.main,
    display: 'flex',
    position: 'relative',
  },
  navbarContainer: {},
  searchResultContainer: {
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    padding: '0 2rem',
    overflow: 'auto',
    height: '100vh',
  },
  searchbarContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    alignItems: 'center',
    justifyContent: 'space-between',
    margin: '2.3rem 0',
  },

  switch: {
    margin: '0.2rem 0',
    borderRadius: '15px',
    background: theme.palette.teritary.main,
    padding: '0.5rem 1rem',
    boxShadow: '0px 1px 5px rgb(0 0 0 / 15%)',
  },
});
export default style;
