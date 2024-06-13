import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  mainContainer: {
    padding: '0 1rem',
  },
  documentsContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    overflow: 'hidden',
    justifyContent: 'space-around',
    alignItems: 'center',
  },
  documentContainer: {
    margin: '1rem 0',
  },
});
export default style;
