```json
{
  "id": "6e17e4b0ca6428f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289732,
  "host_pid": "9e6742732c60:1",
  "hash": "0d9a894a5ab2b2c2b3f3290c1018a4bb15aa6ce531f56ed82d230b03cc234985",
  "cid": "QmV10d9a894a5ab2b2c2b3f3290c1018a4bb15aa6ce5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289732,
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
      "evaluated_at": 1760289732
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
  "sig": "8f18aaf321604c65ced2660fdfaeb774e736409b15d4a398a6670f4a1f057638"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460708628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}