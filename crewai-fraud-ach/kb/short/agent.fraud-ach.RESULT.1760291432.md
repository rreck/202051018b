```json
{
  "id": "52599a0a108d544e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291432,
  "host_pid": "9e6742732c60:1",
  "hash": "7b5d97c3b86c5a588d56b82edeb999de688ffe6cc1d247dd12bf4cf3ac1a4ee5",
  "cid": "QmV17b5d97c3b86c5a588d56b82edeb999de688ffe6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291432,
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
      "evaluated_at": 1760291432
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
  "sig": "dd5e53efdf836424530a5c400bfefa3a5d237facb4dfd1e495c9580fc02b3489"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 62974275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}