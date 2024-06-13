import { makeStyles } from '@mui/styles';

const style = makeStyles({
  container: {
    width: '18rem',
    height: '22rem',
    '&:hover': {
      cursor: 'pointer',
    },
    border: (props) => (props.exists ? 'none' : '2px solid grey'),
  },
  title: {
    fontSize: '0.8rem',
    margin: '0.4rem 0 ',
    fontWeight: 'bold',
  },
  border: {
    borderTop: '1px solid black',
  },
  summary: {
    fontSize: '0.7rem ',
    margin: '0.8rem 0.3rem',
    overflow: 'hidden',
    height: '20rem',
  },
  cardContent: {
    height: '20rem',
  },
  link: {
    textDecoration: 'none',
  },
});
export default style;
