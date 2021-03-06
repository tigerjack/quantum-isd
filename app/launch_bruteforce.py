import logging
from isdquantum.methods.algorithms.bruteforce_alg import BruteforceAlg
from isdquantum.utils import misc
from app.session import Session
from app import end
logger = logging.getLogger(__name__)


def go():
    ses = Session()
    bru = BruteforceAlg(ses.h, ses.syndrome, ses.args.w, ses.need_measures,
                        ses.args.mct_mode, ses.args.nwr_mode)
    ses.qc, ses.backend = bru.prepare_circuit_for_backend(
        ses.args.provider, ses.args.backend)
    if ses.args.infos:
        infos = misc.get_compiled_circuit_infos(ses.qc, ses.backend)
        for k, v in infos.items():
            print("{} --> {}".format(k, v))
    if ses.args.export_qasm_file is not None:
        misc.export_circuit_to_qasm(ses.qc, ses.args.export_qasm_file)

    if (ses.args.not_execute):
        logger.debug("Not execute set to true, exiting.")
        end.go()
    ses.result, ses.error, ses.accuracy = bru.run_circuit_on_backend(
        ses.qc, ses.backend)
    end.go()
