```json
{
  "id": "b11d35f10861e99e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292524,
  "host_pid": "9e6742732c60:1",
  "hash": "1edd83a281817229029d6ad15859a4a456fc342ca2fee7da24e42f04376c136f",
  "cid": "QmV11edd83a281817229029d6ad15859a4a456fc342c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292524,
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
      "evaluated_at": 1760292524
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
  "sig": "0a764db571e3dfd395bc4b184f1d99830d25fd271c393cd9ad6db1c5a31cb008"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 18865001, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}