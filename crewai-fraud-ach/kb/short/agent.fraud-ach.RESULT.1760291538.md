```json
{
  "id": "c2e3556abf226016",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291538,
  "host_pid": "9e6742732c60:1",
  "hash": "ffd35f467b9e31eace66d227e16e7c544913a9ce35777a76f746699618bdfce2",
  "cid": "QmV1ffd35f467b9e31eace66d227e16e7c544913a9ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291538,
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
      "evaluated_at": 1760291538
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
  "sig": "506a537777871863e2fd5c7fbcde2c29038c8d6888926be9947633156dd7b6e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464550835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 33140064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '50cb0ee46794e046'}}}