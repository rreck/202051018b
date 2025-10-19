```json
{
  "id": "1b63e37488154f53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288434,
  "host_pid": "9e6742732c60:1",
  "hash": "6935fbef6117c1761434f21ccfeeca111361f77255e1e4e4046fa178d63b5c6c",
  "cid": "QmV16935fbef6117c1761434f21ccfeeca111361f772",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288434,
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
      "evaluated_at": 1760288434
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
  "sig": "b72b1172e2cd45f1ad40a918116897a40fa7e77cff6e3a45eff7fb288e6abcf7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270534223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 16662624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': '6dd341e8ae885101'}}}