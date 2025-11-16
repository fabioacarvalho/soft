import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

export default function CircularProgress() {
    const percentage = 66;
    const primaryColor = '#15A25E';

    return (
        <CircularProgressbar className='text-primary size-52 my-10' value={percentage} text={`${percentage}%`} styles={{ 
            path: { stroke: primaryColor, strokeLinecap: 'round', transition: 'stroke-dashoffset 0.5s ease 0s' },  
            text: { fill: primaryColor, fontSize: '16px', fontWeight: 'bold'},
            trail: { stroke: '#e2e8f0'},
         }} />
    );
}