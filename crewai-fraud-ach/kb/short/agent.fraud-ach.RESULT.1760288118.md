```json
{
  "id": "b7652ed6ce3c02f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288118,
  "host_pid": "9e6742732c60:1",
  "hash": "7799b205aea9d183070124b0e984b54e0ae3501dd276914b634364ec55c379e5",
  "cid": "QmV17799b205aea9d183070124b0e984b54e0ae3501d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288118,
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
      "evaluated_at": 1760288118
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
  "sig": "6d7362fdfa4a5f2b71c707189eb59d9b474cc26f962e7dcbe501c689c48b12d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462119178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 35148757, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': '2f807700ebd65d7c'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}