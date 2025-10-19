```json
{
  "id": "abd039260d838fa8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291754,
  "host_pid": "9e6742732c60:1",
  "hash": "f46573452a96112743592b88f044e92db763f8aabe4f88834f2121f89c6015aa",
  "cid": "QmV1f46573452a96112743592b88f044e92db763f8aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291754,
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
      "evaluated_at": 1760291754
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
  "sig": "61638994d3b1f82c7da2d7b65b28daa844b2e45ebfbbf8a522ca12b0cf3298ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034053694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': 'f3f5d61420936f73'}}}een': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}