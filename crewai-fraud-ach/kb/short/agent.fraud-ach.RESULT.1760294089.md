```json
{
  "id": "762b86c332eed80c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294089,
  "host_pid": "9e6742732c60:1",
  "hash": "747992a19b7419d20992119e6948b0f0b342fd56d1946ec64405c7786a3b03e8",
  "cid": "QmV1747992a19b7419d20992119e6948b0f0b342fd56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294089,
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
      "evaluated_at": 1760294089
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
  "sig": "d72bf80bd323e0ac347cd8e98527685ced1a4726d1021642287c98a6aebc7eb5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 53591769, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}