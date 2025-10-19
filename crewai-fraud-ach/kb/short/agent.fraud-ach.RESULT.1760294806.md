```json
{
  "id": "721be3a8822d0932",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294806,
  "host_pid": "9e6742732c60:1",
  "hash": "b1cf500069a7ee96f49c6eb3a3dab1808efa6797b8c0f04c06ed351340fea64a",
  "cid": "QmV1b1cf500069a7ee96f49c6eb3a3dab1808efa6797",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294806,
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
      "evaluated_at": 1760294806
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
  "sig": "7bf1728f2f09d96d52925687c5d6c030718bf6f1b2de21045d051f9d010f3de2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 63636545, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}