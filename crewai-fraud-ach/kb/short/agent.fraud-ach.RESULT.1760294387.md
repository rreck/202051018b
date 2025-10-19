```json
{
  "id": "7151e883a57af65c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294387,
  "host_pid": "9e6742732c60:1",
  "hash": "3474d7561c1471bb606a9ffadf5eb0ca8f359dabc87125e813b66a08573384d1",
  "cid": "QmV13474d7561c1471bb606a9ffadf5eb0ca8f359dab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294387,
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
      "evaluated_at": 1760294387
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
  "sig": "14387d6883e6be6d5c70f8e696b482995413dcb69ecce550419c356aeefff5f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024349722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 15411399, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}