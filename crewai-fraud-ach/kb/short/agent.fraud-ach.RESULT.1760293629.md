```json
{
  "id": "66863979004cd873",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293629,
  "host_pid": "9e6742732c60:1",
  "hash": "dcaf9c4ce9f14c8ecdde43afc71ce134534918f8a02e36c3ac86b14f3473c606",
  "cid": "QmV1dcaf9c4ce9f14c8ecdde43afc71ce134534918f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293629,
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
      "evaluated_at": 1760293629
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
  "sig": "f97e344e2a1e2b62676aaadfd6cdbf4094c94c0b5a17d6f7366eeebdb1c6a5ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028777791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 14095668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'd241f2dd5b1f162a'}}}