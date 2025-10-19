```json
{
  "id": "e1d27a74bb041323",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293763,
  "host_pid": "9e6742732c60:1",
  "hash": "cdfde0e9099573e02d06f02bd1bb47f5b46cfae063c00cc93a1db2209c3c0c62",
  "cid": "QmV1cdfde0e9099573e02d06f02bd1bb47f5b46cfae0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293763,
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
      "evaluated_at": 1760293763
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
  "sig": "99b8cea974f8c3c7cc8374e53c9e91a2fad74ddf2a907e430295e128800ed9cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 102308175, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}