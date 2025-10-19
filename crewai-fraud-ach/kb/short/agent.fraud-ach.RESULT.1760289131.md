```json
{
  "id": "dc697b9720b7fefa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289131,
  "host_pid": "9e6742732c60:1",
  "hash": "4cf757829128f4d8877fd1966ca692e1e14cf3000d0e0c2e5787a8453950e810",
  "cid": "QmV14cf757829128f4d8877fd1966ca692e1e14cf300",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289131,
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
      "evaluated_at": 1760289131
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
  "sig": "f3666daadf1a3df94263c784e307b19ae8d0f26a2461ce65b226963f424619dd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 50563446, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}