```json
{
  "id": "19e830080982392a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294774,
  "host_pid": "9e6742732c60:1",
  "hash": "478cc6746ac55b22397c7d16a4b67eb7c06fbb032a96f372601be0c52b0721d5",
  "cid": "QmV1478cc6746ac55b22397c7d16a4b67eb7c06fbb03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294774,
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
      "evaluated_at": 1760294775
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
  "sig": "43b840a5d78917ca5e5cbd9e7c397ad39e30577931aff63ec9190461b7ba6b7f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026494478
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 46242148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'bca1271a1f86b87c'}}}