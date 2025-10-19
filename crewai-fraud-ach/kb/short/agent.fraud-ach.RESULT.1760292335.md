```json
{
  "id": "89bdb65510bdbfe1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292335,
  "host_pid": "9e6742732c60:1",
  "hash": "75038c7fd981b08c2b51bf20b2de38018e3f58d17852727daf66d0a6644ccd75",
  "cid": "QmV175038c7fd981b08c2b51bf20b2de38018e3f58d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292335,
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
      "evaluated_at": 1760292335
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
  "sig": "0443654863452a13e63b6e508b1fd114643394d19fef29a9b131147ffb0ab7bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243649474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 68803800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '901672e1b111b3e4'}}}