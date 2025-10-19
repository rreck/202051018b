```json
{
  "id": "3a560e175226f1cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289681,
  "host_pid": "9e6742732c60:1",
  "hash": "a1df69832a555a0967092689c73dad224e220ee1cbeec7da310ee3f283302255",
  "cid": "QmV1a1df69832a555a0967092689c73dad224e220ee1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289681,
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
      "evaluated_at": 1760289681
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
  "sig": "8b8b80923867c59197e69d1ba1b482e995b2051dfca383aa78cc39e9e37a23ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 26781560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}