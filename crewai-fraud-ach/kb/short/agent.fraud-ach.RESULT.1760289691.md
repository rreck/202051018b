```json
{
  "id": "949d0643c122a56a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289691,
  "host_pid": "9e6742732c60:1",
  "hash": "f56a081849f49da859bd86af24016409a2628f6ac522be725d6f108925ea08b2",
  "cid": "QmV1f56a081849f49da859bd86af24016409a2628f6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289691,
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
      "evaluated_at": 1760289691
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
  "sig": "ef4d1bc8f5a211be7401c14282393dc1305d866d67b8d4788388662119a6b591"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 29953560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}