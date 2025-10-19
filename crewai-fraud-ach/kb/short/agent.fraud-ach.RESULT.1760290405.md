```json
{
  "id": "2d88d93b44f7cfbd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290405,
  "host_pid": "9e6742732c60:1",
  "hash": "4444a108dfab320d49471be3d5a981286779e798fbda326ac3be6a2474fc74a2",
  "cid": "QmV14444a108dfab320d49471be3d5a981286779e798",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290405,
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
      "evaluated_at": 1760290405
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
  "sig": "83a4b120af27580b90210784d6ffbb6fbac66e9fae72409068e590d7f8765d1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 62126593, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}