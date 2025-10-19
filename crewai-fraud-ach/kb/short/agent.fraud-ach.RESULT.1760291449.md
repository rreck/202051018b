```json
{
  "id": "01dbee3de367d990",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291449,
  "host_pid": "9e6742732c60:1",
  "hash": "88f68139a5b713aaa136d075bf6246dd20a09351fe2a52cefacdc0144d2730f3",
  "cid": "QmV188f68139a5b713aaa136d075bf6246dd20a09351",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291449,
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
      "evaluated_at": 1760291450
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
  "sig": "fb31e3b13f4c2b53a7be98d08dbd0fbdeb004330e2c7474862319de90d1e15d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272268645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 77054425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '088fbc730f5432fe'}}}