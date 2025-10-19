#!/usr/bin/env python3
"""
pmem 1.0 - Demo script showing complete workflow
Demonstrates IDEA → TASK → RESULT → CLUSTER → SYNTHESIS → CONSENSUS
"""

from pmem import PMemSystem
from pmem_consolidate import PMemConsolidator
import time


def demo_workflow():
    """Run complete pmem 1.0 demonstration"""

    print("=" * 60)
    print("pmem 1.0 - Biomimicry Persistent Memory Demo")
    print("=" * 60)

    pmem = PMemSystem()
    consolidator = PMemConsolidator(pmem)

    # Phase 1: Create atomic artifacts (IDEAS)
    print("\n[Phase 1] Creating atomic artifacts...")

    ideas = [
        "Implement weight decay on temporal edges",
        "Add cryptographic signing to all artifacts",
        "Build cross-agent consensus protocol",
        "Design quarantine system for anomalies",
        "Create UCON constraint validator"
    ]

    idea_paths = []
    for i, idea_text in enumerate(ideas):
        path = pmem.write_artifact(
            scope="agent",
            key="IDEA",
            body=idea_text,
            tags=["architecture", "pmem"],
            metrics={"priority": 0.7 + i * 0.05},
            issuer="demo-agent"
        )
        idea_paths.append(path)
        print(f"  ✓ {path}")

    # Phase 2: Create tasks from ideas
    print("\n[Phase 2] Creating tasks from ideas...")

    task_paths = []
    for i, idea_path in enumerate(idea_paths):
        header, body = pmem.read_artifact(idea_path)

        task_path = pmem.write_artifact(
            scope="agent",
            key="TASK",
            body=f"Implement: {body}",
            sources=[header.id],
            tags=["implementation"],
            issuer="demo-agent"
        )
        task_paths.append(task_path)

        # Create edge from idea to task
        task_header, _ = pmem.read_artifact(task_path)
        pmem.add_edge(header.id, task_header.id, 0.9)

        print(f"  ✓ {task_path}")

    # Phase 3: Create results from tasks
    print("\n[Phase 3] Creating results from tasks...")

    result_paths = []
    for i, task_path in enumerate(task_paths):
        header, body = pmem.read_artifact(task_path)

        result_path = pmem.write_artifact(
            scope="agent",
            key="RESULT",
            body=f"Completed: {body}\n\nStatus: Success\nTests: Passed",
            sources=[header.id],
            tags=["completed"],
            metrics={"success": True},
            issuer="demo-agent"
        )
        result_paths.append(result_path)

        # Create edges
        result_header, _ = pmem.read_artifact(result_path)
        pmem.add_edge(header.id, result_header.id, 0.95)

        print(f"  ✓ {result_path}")

    # Phase 4: Create cross-connections (reinforcement)
    print("\n[Phase 4] Creating reinforcement edges...")

    # Connect related results
    for i in range(len(result_paths) - 1):
        h1, _ = pmem.read_artifact(result_paths[i])
        h2, _ = pmem.read_artifact(result_paths[i + 1])
        pmem.add_edge(h1.id, h2.id, 0.75)
        print(f"  ✓ {h1.id} → {h2.id} (w=0.75)")

    # Phase 5: Find clusters
    print("\n[Phase 5] Finding clusters...")

    clusters = pmem.find_clusters()
    print(f"  Found {len(clusters)} cluster candidates")

    for cluster in clusters:
        print(f"    - Target: {cluster['target']}")
        print(f"      Sources: {cluster['count']}")
        print(f"      Avg weight: {cluster['avg_weight']:.3f}")

    # Phase 6: Create CLUSTER artifacts
    print("\n[Phase 6] Creating CLUSTER artifacts...")

    cluster_paths = []
    for cluster in clusters:
        cluster_path = pmem.create_cluster(
            scope="agent",
            members=cluster["sources"],
            summary=f"Cluster of {cluster['count']} related pmem implementation artifacts",
            pattern="temporal-cooccurrence"
        )
        cluster_paths.append(cluster_path)
        print(f"  ✓ {cluster_path}")

    # Phase 7: Create SYNTHESIS
    print("\n[Phase 7] Creating SYNTHESIS...")

    if len(cluster_paths) >= 2:
        synth_path = consolidator.generate_synthesis(
            scope="agent",
            clusters=cluster_paths[:2],
            theme="pmem 1.0 implementation patterns",
            hypothesis="Temporal clustering reveals implementation dependencies"
        )

        if synth_path:
            print(f"  ✓ {synth_path}")

            # Read and display
            header, body = pmem.read_artifact(synth_path)
            print(f"\n  Synthesis ID: {header.id}")
            print(f"  Sources: {len(header.sources)} clusters")
            print(f"  Unique sources: {header.metrics.get('unique_sources', 0)}")
        else:
            print("  ✗ Synthesis rejected (JS divergence too high)")
    else:
        print("  ⊘ Not enough clusters for synthesis")

    # Phase 8: Create CONSENSUS
    print("\n[Phase 8] Creating CONSENSUS...")

    consensus_path = consolidator.generate_consensus(
        scope="crew",  # crew-level consensus
        artifacts=result_paths[:3],
        position="pmem 1.0 core implementation complete",
        rationale="All core components tested and verified"
    )

    if consensus_path:
        print(f"  ✓ {consensus_path}")

        header, body = pmem.read_artifact(consensus_path)
        print(f"\n  Consensus ID: {header.id}")
        print(f"  Quorum: {header.metrics.get('quorum', 0):.2%}")
        print(f"  Approved: {header.metrics.get('approved', False)}")
    else:
        print("  ✗ Consensus rejected (quorum or UCON failure)")

    # Phase 9: Verify provenance
    print("\n[Phase 9] Verifying provenance...")

    all_artifacts = idea_paths + task_paths + result_paths + cluster_paths
    if consensus_path:
        all_artifacts.append(consensus_path)

    verified = 0
    for artifact_path in all_artifacts:
        if pmem.verify_provenance(artifact_path):
            verified += 1

    print(f"  Verified: {verified}/{len(all_artifacts)} artifacts")

    # Phase 10: Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    all_artifacts_final = pmem.list_artifacts()
    print(f"Total artifacts: {len(all_artifacts_final)}")

    for key in ["IDEA", "TASK", "RESULT", "CLUSTER", "SYNTHESIS", "CONSENSUS"]:
        count = len(pmem.list_artifacts(key))
        if count > 0:
            print(f"  {key}: {count}")

    print(f"\nEdges: {len(pmem.edges)}")
    print(f"Storage: kb/short={len(list(pmem.kb_short.glob('*.md')))}, kb/long={len(list(pmem.kb_long.glob('*.md')))}")

    print("\n✓ pmem 1.0 demo complete")


if __name__ == "__main__":
    demo_workflow()
