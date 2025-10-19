```json
{
  "id": "3911f2c4d8c45adf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293469,
  "host_pid": "9e6742732c60:1",
  "hash": "03c85b98e1a3f2beea2c37ff16ca6c1d850c754f177d2a4c647c85259a67d657",
  "cid": "QmV103c85b98e1a3f2beea2c37ff16ca6c1d850c754f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293469,
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
      "evaluated_at": 1760293469
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
  "sig": "1d92bf0ff3ba2488efc06ffd490d84043be5bd06eb9132420f9307b52434536d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157518284
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 63942306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '79d45ba49f6b4a46'}}}