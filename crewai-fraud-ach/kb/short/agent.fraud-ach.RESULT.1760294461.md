```json
{
  "id": "ee466b68c5432af0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294461,
  "host_pid": "9e6742732c60:1",
  "hash": "42cc6eccf58d97fc47ebfd4cb8fc1a8a8e80f20686f3895f28c7ada30ee005f8",
  "cid": "QmV142cc6eccf58d97fc47ebfd4cb8fc1a8a8e80f206",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294461,
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
      "evaluated_at": 1760294461
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
  "sig": "8a77c20a3fbd74fd5b0e0a85b4d1f9fd3fd8c725836497c52f191aaa3644a3a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 40367418, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}