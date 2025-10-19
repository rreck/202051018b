```json
{
  "id": "1aff92e48f2c7e61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289863,
  "host_pid": "9e6742732c60:1",
  "hash": "2037957fdef5dab22718deb41e972fbc59afef3f7f0dadefa638d5115796a803",
  "cid": "QmV12037957fdef5dab22718deb41e972fbc59afef3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289863,
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
      "evaluated_at": 1760289863
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
  "sig": "0ce1e85c3e6b6e97fca264bf47010b0d2ef1cff0a18e5ec7249767d9a9124674"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151200756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 21953565, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': 'e0249734267f8906'}}}