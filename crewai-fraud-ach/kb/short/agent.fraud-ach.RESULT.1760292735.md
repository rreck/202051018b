```json
{
  "id": "aa75bdf9f72b4157",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292735,
  "host_pid": "9e6742732c60:1",
  "hash": "ae692d7f1288add16db01978c44645fc8709f941a2429e10f4ce7e5a65adf526",
  "cid": "QmV1ae692d7f1288add16db01978c44645fc8709f941",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292735,
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
      "evaluated_at": 1760292735
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
  "sig": "a47e5b32b29dc2c4503cd820a9fb1fdaabc8f92487838384fe884c3f45761029"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466383232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 40748796, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '37ada470abbef201'}}}