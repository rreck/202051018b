```json
{
  "id": "cd76b664a4281a80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287974,
  "host_pid": "9e6742732c60:1",
  "hash": "9d8a0f24323742e0ebaa32150098873f933d305666f17a9a4aa9a6404d4370da",
  "cid": "QmV19d8a0f24323742e0ebaa32150098873f933d3056",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287974,
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
      "evaluated_at": 1760287974
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
  "sig": "9a6ffe32bf5ec6c66cdc035b74172469256f23a4dd68bbf3a876ed08add9872c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276764543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 25584156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': '861ebf9054cc2433'}}}