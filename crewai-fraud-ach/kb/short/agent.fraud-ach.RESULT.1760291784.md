```json
{
  "id": "7628d413cb2d5690",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291784,
  "host_pid": "9e6742732c60:1",
  "hash": "cc86596d87fef1f12e2d010da649d74afd309fa9dde82252f606dcbebf0dc48c",
  "cid": "QmV1cc86596d87fef1f12e2d010da649d74afd309fa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291784,
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
      "evaluated_at": 1760291784
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
  "sig": "c43a9a2e45b582a827c6ab51d730ab2842fdfca0794e0d46faccea0a1fb2c745"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463060709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 86875773, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285764, 'matching_hash': '9043a83188003850'}}}