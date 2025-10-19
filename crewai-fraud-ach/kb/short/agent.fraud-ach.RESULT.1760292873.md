```json
{
  "id": "38ff3f670650dbd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292873,
  "host_pid": "9e6742732c60:1",
  "hash": "9ca999c7b6f89c06ad6aa4d3aee6be7e2dd4a7dc7c1a2a33899a6926fba94603",
  "cid": "QmV19ca999c7b6f89c06ad6aa4d3aee6be7e2dd4a7dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292873,
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
      "evaluated_at": 1760292873
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
  "sig": "fae22a3ea29947fa646142797e8cf7a7f0c808be62964dbf3fd4254ee1df0e5a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278260639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 73407582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'cac17e8b7d36ee50'}}}maly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}