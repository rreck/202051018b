```json
{
  "id": "2f9c4f809c511829",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286997,
  "host_pid": "9e6742732c60:1",
  "hash": "0ffb0f8ee0f0d70138ed5cbcde4c3951c3d0cb3e81b86a76f787940e04db8bc9",
  "cid": "QmV10ffb0f8ee0f0d70138ed5cbcde4c3951c3d0cb3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286997,
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
      "evaluated_at": 1760286997
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "557e2e6d5e446d2ed02d941ec77b998c416908da71ee2cfeaccd24b8cbbfe5de"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14002912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}