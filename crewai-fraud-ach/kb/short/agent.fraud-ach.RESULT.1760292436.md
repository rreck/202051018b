```json
{
  "id": "365e5ba694181e0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292436,
  "host_pid": "9e6742732c60:1",
  "hash": "37004a636b2d22aecd27ec9f3360394feaf9089f865906572c740b0264c3b449",
  "cid": "QmV137004a636b2d22aecd27ec9f3360394feaf9089f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292436,
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
      "evaluated_at": 1760292436
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
  "sig": "467ae30de11b38f97290d09eaf730173e28e25433e0639fbffe7b66d69e48e7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 21825827, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}