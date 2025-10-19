```json
{
  "id": "5ae5993055692485",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289062,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b656f31ae198ed22762cf6829cc36df31d205ce0b0cef8a40c1c6a126b86f9",
  "cid": "QmV1e4b656f31ae198ed22762cf6829cc36df31d205c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289062,
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
      "evaluated_at": 1760289062
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
  "sig": "c35b9c456f8a54663fdcc74b3bc9a6bec61275b03d70a74713e443e42c58db62"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 17799712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}