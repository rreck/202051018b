```json
{
  "id": "20777585755aa662",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294650,
  "host_pid": "9e6742732c60:1",
  "hash": "49c6c2d33865bb49a8184d1ba1eb55c36a1e48898962d551681e0dadf2ffa80f",
  "cid": "QmV149c6c2d33865bb49a8184d1ba1eb55c36a1e4889",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294650,
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
      "evaluated_at": 1760294650
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
  "sig": "f79cea085ab79a1f067877799a9c2c7bf8c4c1588984b50baadeb8b8ef2bca8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 39134304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}