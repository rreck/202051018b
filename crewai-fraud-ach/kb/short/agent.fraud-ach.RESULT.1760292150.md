```json
{
  "id": "12ab0fd1654aa5d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292150,
  "host_pid": "9e6742732c60:1",
  "hash": "de825e15919454fc57bf9adce1e311ae89dcd2d3b6183d24ee0ee103eaa5c58c",
  "cid": "QmV1de825e15919454fc57bf9adce1e311ae89dcd2d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292150,
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
      "evaluated_at": 1760292150
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
  "sig": "1ed9cf5ad63721f60186250810ebd631b66c02c129419769d6d5b204b6d1cd14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031032710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 45305391, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'e5dc8a38744b9e1c'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}