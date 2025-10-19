```json
{
  "id": "16fac632ab422eab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292186,
  "host_pid": "9e6742732c60:1",
  "hash": "5c2fa29f23511b02ffb547424db0eca8ef021bea1fd4ced807a116a2644d4cd2",
  "cid": "QmV15c2fa29f23511b02ffb547424db0eca8ef021bea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292186,
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
      "evaluated_at": 1760292186
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
  "sig": "f5120e36485862b6de2475d5bea975332adcf66bcbe37f2dc733c47643e004d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 84420480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}