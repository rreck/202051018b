```json
{
  "id": "def06475551e3d9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287552,
  "host_pid": "9e6742732c60:1",
  "hash": "646594950f1ef7869db22704d875ed37a1470e20ce0b11abf2ab4fbba500d611",
  "cid": "QmV1646594950f1ef7869db22704d875ed37a1470e20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287552,
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
      "evaluated_at": 1760287552
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
  "sig": "6b9917a8c197dfcd8fc7fc4513a2e43bbfe7d050debb1ac0f59007a5dc6fb591"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000245329334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 23602048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}