```json
{
  "id": "63d77dfc9d4b78b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289734,
  "host_pid": "9e6742732c60:1",
  "hash": "7bcc90b91257f7df4496879ddc491aee89990581bdebf10d513479adbb45dbb8",
  "cid": "QmV17bcc90b91257f7df4496879ddc491aee89990581",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289734,
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
      "evaluated_at": 1760289734
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
  "sig": "778d106e3ef079616c8a781d119050d72e3b8b2fd20acf8652410df7d227c9d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 41690488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}