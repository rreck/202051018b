```json
{
  "id": "067c8d97a42014d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291149,
  "host_pid": "9e6742732c60:1",
  "hash": "5720e9dec64f8138fe4cc4baaab1bd46d78693175d25b3b56a1874211ffea4c0",
  "cid": "QmV15720e9dec64f8138fe4cc4baaab1bd46d7869317",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291149,
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
      "evaluated_at": 1760291149
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
  "sig": "c74538fdcbac79bdce284bc2a506882db15783bc7ed97c6c1388ecd9c162eaf0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 56477400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}