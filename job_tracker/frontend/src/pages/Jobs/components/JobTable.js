import * as React from "react";
import styled from '@emotion/styled'
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";


function JobsTableHeaderRow(){
  return (
    <TableRow>
      <TableCell align="center">Company</TableCell>
      <TableCell align="center">Title</TableCell>
      <TableCell align="center">Compensation</TableCell>
      <TableCell align="center">Work Model</TableCell>
      <TableCell align="center">Location</TableCell>
      <TableCell align="center">Source</TableCell>
      <TableCell align="center">Application Status</TableCell>
      <TableCell align="center">Resume</TableCell>
      <TableCell align="center">Cover Letter</TableCell>
    </TableRow>
  );
}

function JobsTableRow({job}) {
  const tableCells = Object.values(job).map(value => { return <TableCell align="right">{value}</TableCell>})
  return (
    <TableRow>
      <TableCell align="right">{job.company_name}</TableCell>
      <TableCell align="right">{job.title}</TableCell>
      <TableCell align="right">{`$${job.compensation_low} - $${job.compensation_high}`}</TableCell>
      <TableCell align="right">{job.work_model}</TableCell>
      <TableCell align="right">{job.location}</TableCell>
      <TableCell align="right">{job.posting_source}</TableCell>
      <TableCell align="right">{job.application_status}</TableCell>
      <TableCell align="right"></TableCell>
      <TableCell align="right"></TableCell>
    </TableRow>
  );

}
function JobsTable({jobs}) {
  return (
    <TableContainer component={Paper} sx={{ maxWidth: '100%'}}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <JobsTableHeaderRow />
        </TableHead>
        <TableBody>
          {jobs.map((jobStr) => {
            const job = JSON.parse(jobStr); // safely parse here
            return <JobsTableRow job={job} key={job.id} />;
          })}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

export default JobsTable