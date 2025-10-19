```json
{
  "id": "ab106b55dfc4c44f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293267,
  "host_pid": "9e6742732c60:1",
  "hash": "fad9c5efc0f2f581e6379e547b37c4445d2077f8eaa9026d372835479a08c19c",
  "cid": "QmV1fad9c5efc0f2f581e6379e547b37c4445d2077f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293267,
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
      "evaluated_at": 1760293267
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
  "sig": "6b396f70aded42262535db627add38b887fd07eb9c5a690eca8e2e3bdb35f063"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030505524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 96636265, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': '58071665864a5dbb'}}}