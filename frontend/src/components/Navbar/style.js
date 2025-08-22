import { makeStyles } from '@mui/styles';
import theme from '../../theme';

const style = makeStyles({
  mainContainer: {
    backgroundColor: '#ffffff',//theme.palette.primary.light,
    width: '12.5rem',
    height: '100vh',
    borderTopRightRadius: '15px',
    borderBottomRightRadius: '15px',
    filter: 'drop-shadow(1px 0px 5px rgba(0, 0, 0, 0.25))',
  },
  menuContainer: {
    backgroundColor: '#ffffff',//theme.palette.primary.light,
    width: '12.5rem',
    borderRadius: '15px',
    borderBottomRightRadius: '15px',
    filter: 'drop-shadow(1px 0px 5px rgba(0, 0, 0, 0.25))',
  },
  logo: {
    height: '5rem',
    widht: '5rem',
    filter: 'drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25))',
    paddingRight: '0.5rem',
  },
  title: {
    color: '#1d5300',    
    fontWeight: '500',
    lineHeight: '1.1rem',
    filter: 'drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25))',
  },
  logoContainer: {    
color: '#1d5300', 
    display: 'flex',
    alignItems: 'center',
    padding: '1.5rem 1rem',
  },
  lineBreak: {
    borderBottom: `1px solid ${theme.palette.secondary.dark}`,
    height: '1px',
  },
  navLinksContainer: {
    color: '#1d5300', 
    padding: '1rem',
    display: 'flex',
    flexDirection: 'column',
  },
  link: {
    color: '#1d5300', 
fontWeight:'500',
    margin: '0.5rem',
    textDecoration: 'none',
    cursor: 'pointer',
  },
  linkContainer: {    
    color: '#1d5300 !important', 
    display: 'flex',
    alignItems: 'center',
    margin: '0.2rem 0',
  },
  menuMainContainer: {
    position: 'absolute',
    left: '0.5rem',
    zIndex: '5',
  },
  navSmallContainer: {
    position: 'absolute',
  },
});
export default style;
