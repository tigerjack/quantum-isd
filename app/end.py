import logging
from app.session import Session
from isdquantum.utils import misc

logger = logging.getLogger(__name__)


def go():
    ses = Session()
    logger.info("H was\n{0}".format(ses.h))
    logger.info("Syndrome was\n{0}".format(ses.syndrome))
    logger.info("With {} accuracy error is \n{}".format(
        ses.accuracy, ses.error))
    if ses.args.export_qasm_file is not None:
        misc.export_circuit_to_qasm(ses.qc, ses.args.export_qasm_file)
    if ses.args.draw_circuit:
        misc.draw_circuit(ses.qc, ses.args.img_dir)
    if ses.args.draw_dag:
        misc.draw_dag(ses.qc, ses.args.img_dir)
