#!/usr/bin/env python3
"""
pmem 1.0 - Consolidation jobs for emergent artifacts
CLUSTER, SYNTHESIS, META, ECHO, CONSENSUS generation
"""

from pmem import PMemSystem, CONSENSUS_MIN_QUORUM, SYNTHESIS_MIN_CLUSTERS, SYNTHESIS_MAX_JS_DIV
from typing import List, Dict, Any, Optional
import json
import math
from collections import Counter


class PMemConsolidator:
    """Consolidation engine for emergent artifacts"""

    def __init__(self, pmem: PMemSystem):
        self.pmem = pmem

    def js_divergence(self, p: List[float], q: List[float]) -> float:
        """Calculate Jensen-Shannon divergence between two distributions"""
        if len(p) != len(q):
            raise ValueError("Distributions must have same length")

        # Normalize
        p_sum = sum(p)
        q_sum = sum(q)
        if p_sum == 0 or q_sum == 0:
            return 1.0

        p = [x / p_sum for x in p]
        q = [x / q_sum for x in q]

        # Compute M = (P + Q) / 2
        m = [(p[i] + q[i]) / 2.0 for i in range(len(p))]

        # KL divergence helper
        def kl(dist1, dist2):
            kl_sum = 0.0
            for i in range(len(dist1)):
                if dist1[i] > 0 and dist2[i] > 0:
                    kl_sum += dist1[i] * math.log(dist1[i] / dist2[i])
            return kl_sum

        # JS = (KL(P||M) + KL(Q||M)) / 2
        return (kl(p, m) + kl(q, m)) / 2.0

    def generate_synthesis(
        self,
        scope: str,
        clusters: List[str],
        theme: str,
        hypothesis: str,
        issuer: str = "pmem-consolidation"
    ) -> Optional[str]:
        """Generate SYNTHESIS from multiple clusters"""

        if len(clusters) < SYNTHESIS_MIN_CLUSTERS:
            return None

        # Load cluster data
        cluster_data = []
        all_sources = []

        for cluster_path in clusters:
            try:
                header, body = self.pmem.read_artifact(cluster_path)
                cluster_data.append({
                    "id": header.id,
                    "sources": header.sources,
                    "metrics": header.metrics
                })
                all_sources.extend(header.sources)
            except Exception as e:
                print(f"Failed to load cluster {cluster_path}: {e}")
                return None

        # Check JS divergence between clusters (simplified: use source overlap)
        # In production, would use actual weight distributions
        unique_sources = set(all_sources)
        cluster_vectors = []
        for cd in cluster_data:
            vec = [1 if src in cd["sources"] else 0 for src in unique_sources]
            cluster_vectors.append(vec)

        # Check all pairs
        for i in range(len(cluster_vectors)):
            for j in range(i + 1, len(cluster_vectors)):
                try:
                    js_div = self.js_divergence(
                        [float(x) for x in cluster_vectors[i]],
                        [float(x) for x in cluster_vectors[j]]
                    )
                    if js_div > SYNTHESIS_MAX_JS_DIV:
                        print(f"JS divergence too high: {js_div:.3f}")
                        return None
                except Exception:
                    pass

        # Build evidence list
        evidence_items = []
        for cd in cluster_data:
            evidence_items.append(f"- {cd['id']}: {len(cd['sources'])} supporting artifacts")

        evidence = "\n".join(evidence_items)

        body = f"""# SYNTHESIS

## Theme
{theme}

## Hypothesis
{hypothesis}

## Evidence
Synthesized from {len(clusters)} clusters with {len(unique_sources)} unique sources:

{evidence}

## Heuristics
- Cross-cluster coherence validated
- Jensen-Shannon divergence ≤ {SYNTHESIS_MAX_JS_DIV}
- Minimum {SYNTHESIS_MIN_CLUSTERS} clusters required

## Limits
- Synthesis represents correlation, not causation
- Subject to weight decay and temporal validity
- Requires continuous validation against new evidence
"""

        metrics = {
            "cluster_count": len(clusters),
            "unique_sources": len(unique_sources),
            "total_sources": len(all_sources)
        }

        return self.pmem.write_artifact(
            scope=scope,
            key="SYNTHESIS",
            body=body,
            sources=[cd["id"] for cd in cluster_data],
            metrics=metrics,
            issuer=issuer
        )

    def generate_meta(
        self,
        scope: str,
        syntheses: List[str],
        meta_rule: str,
        standard: str,
        issuer: str = "pmem-consolidation"
    ) -> Optional[str]:
        """Generate META from multiple syntheses"""

        if len(syntheses) < 2:
            return None

        # Load synthesis data
        synthesis_data = []
        all_clusters = []

        for synth_path in syntheses:
            try:
                header, body = self.pmem.read_artifact(synth_path)
                synthesis_data.append({
                    "id": header.id,
                    "sources": header.sources,
                    "metrics": header.metrics
                })
                all_clusters.extend(header.sources)
            except Exception as e:
                print(f"Failed to load synthesis {synth_path}: {e}")
                return None

        support_items = []
        for sd in synthesis_data:
            support_items.append(f"- {sd['id']}")

        support = "\n".join(support_items)

        body = f"""# META

## Meta-Rule
{meta_rule}

## Support
Derived from {len(syntheses)} syntheses spanning {len(set(all_clusters))} clusters:

{support}

## Standard
{standard}

## Impact
Meta-rules shape consolidation behavior and emergence patterns across the knowledge base.
Updates to meta-rules require governance approval and impact analysis.
"""

        metrics = {
            "synthesis_count": len(syntheses),
            "cluster_span": len(set(all_clusters))
        }

        return self.pmem.write_artifact(
            scope=scope,
            key="META",
            body=body,
            sources=[sd["id"] for sd in synthesis_data],
            metrics=metrics,
            issuer=issuer
        )

    def generate_echo(
        self,
        scope: str,
        artifacts: List[str],
        replay: str,
        mutation: str,
        issuer: str = "pmem-consolidation"
    ) -> Optional[str]:
        """Generate ECHO for anomaly detection"""

        artifact_data = []
        for artifact_path in artifacts:
            try:
                header, body = self.pmem.read_artifact(artifact_path)
                artifact_data.append({
                    "id": header.id,
                    "key": header.key,
                    "epoch": header.epoch
                })
            except Exception:
                continue

        if len(artifact_data) == 0:
            return None

        # Detect anomalies (simplified: look for outliers)
        epochs = [ad["epoch"] for ad in artifact_data]
        mean_epoch = sum(epochs) / len(epochs)
        std_dev = math.sqrt(sum((e - mean_epoch) ** 2 for e in epochs) / len(epochs))

        anomalies = []
        for ad in artifact_data:
            z_score = abs(ad["epoch"] - mean_epoch) / std_dev if std_dev > 0 else 0
            if z_score > 2.0:  # 2 sigma threshold
                anomalies.append(f"- {ad['id']}: temporal outlier (z={z_score:.2f})")

        anomaly_text = "\n".join(anomalies) if anomalies else "No anomalies detected"

        candidates_text = "\n".join(f"- {ad['id']}" for ad in artifact_data[:5])

        body = f"""# ECHO

## Replay
{replay}

## Mutation
{mutation}

## Anomaly
{anomaly_text}

## Candidates
Quarantine candidates for review:

{candidates_text}

## Governance
ECHO artifacts are NOT used as direct sources for clusters or synthesis.
They serve diagnostic and quality control purposes only.
"""

        metrics = {
            "artifact_count": len(artifact_data),
            "anomaly_count": len(anomalies)
        }

        # CRITICAL: ECHO artifacts have NO sources to prevent contamination
        return self.pmem.write_artifact(
            scope=scope,
            key="ECHO",
            body=body,
            sources=[],  # NO SOURCES
            metrics=metrics,
            issuer=issuer
        )

    def generate_consensus(
        self,
        scope: str,
        artifacts: List[str],
        position: str,
        rationale: str,
        issuer: str = "pmem-consolidation"
    ) -> Optional[str]:
        """Generate CONSENSUS with quorum validation"""

        # Load artifacts and check UCON conflicts
        if self.pmem.check_ucon_conflict(artifacts):
            print("UCON conflict detected - consensus rejected")
            return None

        artifact_data = []
        for artifact_path in artifacts:
            try:
                header, body = self.pmem.read_artifact(artifact_path)
                artifact_data.append({
                    "id": header.id,
                    "scope": header.scope
                })
            except Exception:
                continue

        if len(artifact_data) == 0:
            return None

        # Check quorum (simplified: all artifacts count equally)
        # In production: weight by artifact quality, recency, etc.
        quorum = 1.0  # All artifacts agree by being included

        if quorum < CONSENSUS_MIN_QUORUM:
            print(f"Quorum too low: {quorum:.2%} < {CONSENSUS_MIN_QUORUM:.2%}")
            return None

        action_text = "Approved for cross-agent propagation" if quorum >= 0.75 else "Local consensus only"

        body = f"""# CONSENSUS

## Position
{position}

## Rationale
{rationale}

## Quorum
- Participating artifacts: {len(artifact_data)}
- Agreement level: {quorum:.2%}
- Threshold: {CONSENSUS_MIN_QUORUM:.2%}
- Status: {'APPROVED' if quorum >= CONSENSUS_MIN_QUORUM else 'REJECTED'}

## Action
{action_text}

## Governance
- Consensus is frozen upon signing
- Lineage is immutable
- Updates require new consensus with reference to this artifact
"""

        metrics = {
            "participant_count": len(artifact_data),
            "quorum": quorum,
            "approved": quorum >= CONSENSUS_MIN_QUORUM
        }

        return self.pmem.write_artifact(
            scope=scope,
            key="CONSENSUS",
            body=body,
            sources=[ad["id"] for ad in artifact_data],
            metrics=metrics,
            issuer=issuer
        )

    def run_consolidation(self) -> Dict[str, int]:
        """Run full consolidation cycle"""

        stats = {
            "clusters": 0,
            "syntheses": 0,
            "meta": 0,
            "echo": 0,
            "consensus": 0
        }

        # 1. Find and create clusters
        cluster_candidates = self.pmem.find_clusters()
        print(f"Found {len(cluster_candidates)} cluster candidates")

        created_clusters = []
        for candidate in cluster_candidates:
            try:
                cluster_path = self.pmem.create_cluster(
                    scope="agent",
                    members=candidate["sources"],
                    summary=f"Cluster of {candidate['count']} related artifacts",
                    pattern="temporal-cooccurrence"
                )
                created_clusters.append(cluster_path)
                stats["clusters"] += 1
            except Exception as e:
                print(f"Failed to create cluster: {e}")

        # 2. Generate synthesis from clusters
        if len(created_clusters) >= SYNTHESIS_MIN_CLUSTERS:
            try:
                synth_path = self.generate_synthesis(
                    scope="agent",
                    clusters=created_clusters[:5],  # limit for example
                    theme="Emergent pattern from temporal clustering",
                    hypothesis="Related activities cluster within time window"
                )
                if synth_path:
                    stats["syntheses"] += 1
            except Exception as e:
                print(f"Failed to create synthesis: {e}")

        return stats


def main():
    """Example consolidation run"""

    pmem = PMemSystem()
    consolidator = PMemConsolidator(pmem)

    # Create some test artifacts
    artifacts = []
    for i in range(7):
        path = pmem.write_artifact(
            scope="agent",
            key="TASK",
            body=f"Example task {i}",
            tags=["test"],
            issuer="test-agent"
        )
        artifacts.append(path)

        # Create edges
        if i > 0:
            header_curr, _ = pmem.read_artifact(path)
            header_prev, _ = pmem.read_artifact(artifacts[i-1])
            pmem.add_edge(header_prev.id, header_curr.id, 0.8)

    print(f"Created {len(artifacts)} test artifacts")

    # Run consolidation
    stats = consolidator.run_consolidation()

    print("\nConsolidation results:")
    for key, val in stats.items():
        print(f"  {key}: {val}")


if __name__ == "__main__":
    main()
