```json
{
  "id": "8049724929be8678",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291017,
  "host_pid": "9e6742732c60:1",
  "hash": "abcec8f5c207d6cf4b85e137ef63340cedc88bb718969bb85058bc21d784f2a7",
  "cid": "QmV1abcec8f5c207d6cf4b85e137ef63340cedc88bb7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291017,
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
      "evaluated_at": 1760291017
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
  "sig": "b5f9129472e04f31d56c1b3cbb908ce875d9d1df066fc9149d4be6ed3bc141bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 30844275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}