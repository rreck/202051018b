```json
{
  "id": "27695606b9e3ab9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291057,
  "host_pid": "9e6742732c60:1",
  "hash": "0fd8e082771355b1e93c1e29567851e75717ec42481bda143d5353274bb947a6",
  "cid": "QmV10fd8e082771355b1e93c1e29567851e75717ec42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291057,
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
      "evaluated_at": 1760291057
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
  "sig": "c7861018acfb9b0a9bc0637f8632d6aba90f87df1f30dfcec7cf93444ffcd3cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466383232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 33158334, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '37ada470abbef201'}}}