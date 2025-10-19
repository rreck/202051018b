```json
{
  "id": "89aa0565f4dbb2d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291073,
  "host_pid": "9e6742732c60:1",
  "hash": "7f684206478016cdcdabd00becbf7fcf670b3a7db1a73db55a79b56bde6cb866",
  "cid": "QmV17f684206478016cdcdabd00becbf7fcf670b3a7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291073,
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
      "evaluated_at": 1760291073
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
  "sig": "4a027fc7850c02bd3eb3c89da7b17a40749535d7f15510a8e8362020bd68ec41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 49455218, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}