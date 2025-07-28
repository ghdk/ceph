User
~~~~

:cli:

    `</ceph/src/ceph.in>`_

:cluster map:

    `<https://docs.ceph.com/en/latest/architecture/#cluster-map>`_

:compiler:

    `</ceph/src/crush/CrushCompiler.h>`_  FIXME

:crush:

    `</ceph/src/crush/crush.h>`_
    `</ceph/src/crush/CrushWrapper.h>`_

..  tree size n^CRUSH_MAX_DEPTH == n^10?

..  /ceph/src/crush/crush::crush_get_bucket_item_weight  FIXME what is?
..  /ceph/src/crush/builder::set_optimal_crush_map  **creation**
..  /ceph/src/crush/builder::crush_bucket_add_item  **reallocs**
....  bucket size unbounded?
....  rule size unbounded?
..  /ceph/src/crush/mapper::crush_do_rule
....  recursive calls

:fsid:

    The fsid is a unique identifier for the cluster, and stands for
    File System ID from the days when the Ceph Storage Cluster was principally
    for the Ceph File System.

    `<https://docs.ceph.com/en/latest/install/manual-deployment/#monitor-bootstrapping>`_

:hello:

    `</ceph/src/pybind/mgr/hello/module.py>`_

:main:

    OSD - `</ceph/src/ceph_osd::main>`_
    MDS - `</ceph/src/ceph_mds::main>`_
    MGR - `</ceph/src/ceph_mgr::main>`_
    MON - `</ceph/src/ceph_mon::main>`_
    RGW (S3) - ?

:pybind:

    Py API: `<https://docs.python.org/3/extending/index.html>`_
    ex `</ceph/src/mgr/ActivePyModule.cc>`_

    GIL: `</ceph/src/mgr/Gil.h>`_

:test:

    `</ceph/src/test/crush/CMakeLists.txt>`_

Kernel
~~~~~~

:cephFS:

    `</linux/include/linux/ceph/>`_
    `</linux/drivers/fs/ceph/>`_
    
:ioctl:  `</linux/fs/ceph/ioctl::ceph_ioctl>`_

Doc
~~~

:bluestore: OSD - data is written directly to the disk device, while a separate
    RocksDB key-value store contains all the metadata. BlueFS provides a
    virtual filesystem layer to support RocksDB.
..  layout: block, block.db, block.wal
:build:  `<https://docs.ceph.com/en/latest/install/build-ceph/>`_
         `<https://docs.ceph.com/en/latest/dev/quick_guide/>`_
         `<https://docs.ceph.com/en/latest/dev/macos/>`_
:ci:     `<https://github.com/ceph/teuthology>`_
:contrib:  `<https://docs.ceph.com/en/latest/dev/developer_guide/basic-workflow/#basic-workflow-dev-guide>`_
           `<https://docs.ceph.com/en/latest/start/documenting-ceph/#documenting-ceph>`_
:test:  `<https://docs.ceph.com/en/latest/dev/developer_guide/tests-unit-tests/>`_
:cephFS:  `<https://www.kernel.org/doc/html/latest/filesystems/ceph.html>`_
:crush:  `<https://ceph.io/assets/pdfs/weil-crush-sc06.pdf>`_

..  "CRUSH meets these challenges by casting data placement as a pseudo-random
    mapping function, eliminating the conventional need for allocation metadata
    and instead distributing data based on a weighted hierarchy describing
    available storage."

..  workload vs utilisation

    "Although a large system will likely contain devices with a variety of
    capacity and performance characteristics, randomized data distributions
    statistically correlate device utilization with workload, such that device
    load is on average proportional to the amount of data stored. This results
    in a one-dimensional placement metric, weight, which should be derived from
    the device's capabilities. Bucket weights are defined as the sum of the
    weights of the items they contain."

..  reshuffling

    "In contrast to conventional hashing techniques, in which any change in the
    number of target bins (devices) results in a massive reshuffling of bin
    contents, CRUSH is based on four different bucket types, each with a
    different selection algorithm to address data movement resulting from the
    addition or removal of devices and overall computational complexity."

..  SELECT algorithm

    algorithm 1 - SELECT - tree traversal (secs 3.2.1, 3.2.2)
    
..  weights (sec 3.3),

    m_optimal = Dw/W where 
    Dw is the combined weight of the storage devices added or removed, and
    W is the total weight of the system.

..  buckets: uniform, list, tree, straw

..  overload protection (sec 4.1.1)

..  load balancing (sec 4.1.2)

..  hashing function (sec 4.3, 5)

..  quantified overall system reliability, MTTDL (sec 4.4, 5)

:glossary:  `<https://docs.ceph.com/en/latest/glossary/#term-Object-Storage-Device>`_
:ibm:  `<https://www.ibm.com/docs/en/storage-ceph>`_
       `<https://www.redbooks.ibm.com/abstracts/redp5721.html>`_
:S3 lifetime management: tiering system
:paxos:  `<https://en.wikipedia.org/wiki/Paxos_(computer_science)>`_
:rados:  `<https://ceph.io/assets/pdfs/weil-rados-pdsw07.pdf>`_

..  FIXME MGR::balancer?
..  FIXME MGR::auto-scaler?
..  FIXME MGR::prometheus?
    
:www:  `<https://docs.ceph.com/en/latest/start/get-involved/>`_

Contrib
~~~~~~~

:gdb:
    gdb --batch -ex "source ../extensions/pygdb.py" -p `cat ./out/mon.a.pid`
:health:
    ./bin/ceph health detail
:intro:
    export DOCKER_DEFAULT_PLATFORM=linux/amd64
    docker run -it --stop-signal SIGQUIT --privileged --cap-add=SYS_PTRACE --security-opt seccomp=unconfined  --name ceph -v ~/Documents/gitspace:/mnt/macos --net=host  debian:testing
    ./install-deps.sh
    git submodule deinit --force --all
    git submodule update --init --recursive --progress  --jobs 1
    ./do_cmake.sh -DWITH_MANPAGE=OFF -DWITH_BABELTRACE=OFF -DWITH_MGR_DASHBOARD_FRONTEND=OFF -DWITH_RBD=OFF -DWITH_KRBD=OFF -DWITH_RADOSGW=OFF -DWITH_TESTS=OFF -DWITH_SYSTEM_BOOST=ON  (cmake -LH)
    ./run-make-check.sh
    cd build; ninja -t targets all
    env MON=1 MDS=1 OSD=1 ../src/vstart.sh --new -x --localhost --bluestore  --debug --trace
                          ../src/stop.sh  &&  rm -rf out dev
:ctest:
    ninja -t targets all (check,test)
    ninja unittest_crush && ./bin/unittest_crush --gtest_filter="CRUSHTest.indep_basic"  (--gtest_list_tests)

FIXME: `<https://docs.ceph.com/en/latest/dev/developer_guide/basic-workflow/#amending-your-pr>`_ inconsistent
       with `<https://github.com/ceph/ceph/blob/main/SubmittingPatches.rst>`_
FIXME: `<https://docs.ceph.com/en/latest/dev/developer_guide/basic-workflow/#miscellaneous>`_
