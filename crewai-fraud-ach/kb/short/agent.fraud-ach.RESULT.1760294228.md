```json
{
  "id": "ef68a2571e7283d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294228,
  "host_pid": "9e6742732c60:1",
  "hash": "884e240c371e728bcfd17ebb3460132fc7a75f92eb8977441ef53d4e3aa3f903",
  "cid": "QmV1884e240c371e728bcfd17ebb3460132fc7a75f92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294228,
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
      "evaluated_at": 1760294228
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
  "sig": "2c9eede47461b1634a066fdee2088b796aa314249add9e4c84bcb07176f446e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 80226666, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}