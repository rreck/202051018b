```json
{
  "id": "02acf62ec127bad0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288627,
  "host_pid": "9e6742732c60:1",
  "hash": "d919db775f0de2192d1e41d33dc52e3d22e82ddfbc79d8a1dbf812106c145502",
  "cid": "QmV1d919db775f0de2192d1e41d33dc52e3d22e82ddf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288627,
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
      "evaluated_at": 1760288627
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
  "sig": "e254fbd33de32d2da5b4c4ad6e8eb7c052d59a96e4257b3e435bd9ea6ebbffb6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468078455
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 44446347, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285764, 'matching_hash': '379f6acb9d31a698'}}}