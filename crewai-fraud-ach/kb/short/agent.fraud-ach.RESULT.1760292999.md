```json
{
  "id": "49518a77eb8c881d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292999,
  "host_pid": "9e6742732c60:1",
  "hash": "27127ac50d1fdd76d3f44daf420ab121bb2cef6e0c502376a5273471e53df268",
  "cid": "QmV127127ac50d1fdd76d3f44daf420ab121bb2cef6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292999,
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
      "evaluated_at": 1760292999
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
  "sig": "41bfb2c35a8c7a0384cffce99b62953ea7d9785c8f70ff603a7f3317f2e56533"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243684464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 37677893, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': '4ae1f96c7cecc03b'}}}