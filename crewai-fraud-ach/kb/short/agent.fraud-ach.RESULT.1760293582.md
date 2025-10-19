```json
{
  "id": "6b9eb9f1b204ccfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293582,
  "host_pid": "9e6742732c60:1",
  "hash": "eccf62e9829c30b6f7e5335a81a179222c3a08e0731c497ec30802bf37a131ab",
  "cid": "QmV1eccf62e9829c30b6f7e5335a81a179222c3a08e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293582,
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
      "evaluated_at": 1760293582
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
  "sig": "e1d6dd8c2250bd4cd22b9f06472626fe3e41494b7ed6fa4d2a0e7b4abff8fe0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592552790
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 72497945, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285764, 'matching_hash': 'c5daecdc9bc16873'}}}