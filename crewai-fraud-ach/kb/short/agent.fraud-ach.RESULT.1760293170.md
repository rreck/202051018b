```json
{
  "id": "76693054b8d442a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293170,
  "host_pid": "9e6742732c60:1",
  "hash": "5329160d30d9f9f5a43e82c2ec97b3bb5fcb9c0330de55b908529a224942a1bd",
  "cid": "QmV15329160d30d9f9f5a43e82c2ec97b3bb5fcb9c03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293170,
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
      "evaluated_at": 1760293170
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
  "sig": "4a4df4b9fd69abb2aaeace17d10c9e5264ef3522a2068d5522eaef14a51ec829"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036907843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 65657676, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '5c57e03938e1b0ed'}}}