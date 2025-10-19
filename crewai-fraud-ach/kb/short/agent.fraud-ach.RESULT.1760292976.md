```json
{
  "id": "276f63ff6280d3d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292976,
  "host_pid": "9e6742732c60:1",
  "hash": "2e43df49e2d2ead46e0a55b8fdd21b2508f0753e79716a4eb811b90964d65472",
  "cid": "QmV12e43df49e2d2ead46e0a55b8fdd21b2508f0753e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292976,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760292976
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "6f9bb130dcb5a7d0e44f41c16109b4a31616b782503a3f6e18d0d160daaa6e88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020626056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 20900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'ca4ea9492786d8a3'}}}maly': {'fraud_detected': True, 'risk_score': 74, 'details': {'zscore': 3.49, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6849877}}}