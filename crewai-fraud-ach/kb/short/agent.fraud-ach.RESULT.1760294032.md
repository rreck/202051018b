```json
{
  "id": "2a300303f3f4cb41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294032,
  "host_pid": "9e6742732c60:1",
  "hash": "a630c741720d44fd7e106faa4702ef09978a5942fdda9199aa934b1c183e5c4f",
  "cid": "QmV1a630c741720d44fd7e106faa4702ef09978a5942",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294032,
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
      "evaluated_at": 1760294032
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
  "sig": "13be28249446a926bfa7830563db05ae1e1627e0dbcd1d7bd0c3cc5ad6e38d7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028775289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 306, 'threshold': 50, 'total_amount': 113982858, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 305, 'first_seen': 1760284979, 'matching_hash': 'c3a7255fa6117479'}}}