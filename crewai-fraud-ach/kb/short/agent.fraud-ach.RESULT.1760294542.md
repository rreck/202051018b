```json
{
  "id": "05558869feddaadc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294542,
  "host_pid": "9e6742732c60:1",
  "hash": "8db5ec1e4524c56cfaa80a3f72e453c7db171ae0954c16422638ad5b303caa09",
  "cid": "QmV18db5ec1e4524c56cfaa80a3f72e453c7db171ae0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294542,
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
      "evaluated_at": 1760294542
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
  "sig": "3aa87ea8d06844014562fbca4b15c4ed76432f00edd2fa1871e7de4975186aec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024298856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 81909600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}