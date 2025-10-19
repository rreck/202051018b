```json
{
  "id": "84ff2758aadabcf4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293214,
  "host_pid": "9e6742732c60:1",
  "hash": "944a4541a19385f30617aebae75dfec80a0ed10d3bdfa161bb6fb3cee2f61f7d",
  "cid": "QmV1944a4541a19385f30617aebae75dfec80a0ed10d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293214,
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
      "evaluated_at": 1760293214
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
  "sig": "4c79446fc8358bdfe1a731d89193e11b7b1cad4f464766f325deeb8aabedaf65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024343993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 61821604, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '423e45fba5759e5c'}}}