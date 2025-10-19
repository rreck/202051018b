```json
{
  "id": "4071f30216655a9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288402,
  "host_pid": "9e6742732c60:1",
  "hash": "3778d734adb66a146e3e8c910c8738c3b092e69bdd5cf30529b03fffdfcb081f",
  "cid": "QmV13778d734adb66a146e3e8c910c8738c3b092e69b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288402,
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
      "evaluated_at": 1760288402
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
  "sig": "04af865e3e3dca0e091eb19843707ce2f04c18b327d0f1f37cbb81887b5c29af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 27304220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}