```json
{
  "id": "b21e1d25882b235f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289376,
  "host_pid": "9e6742732c60:1",
  "hash": "54f401006533e7cc874a56f093114815ae25f980d818a0093594ebe9e76137d6",
  "cid": "QmV154f401006533e7cc874a56f093114815ae25f980",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289376,
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
      "evaluated_at": 1760289376
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
  "sig": "7a362228c1be39970ddeae1e444c887e3cfd4e9587fea4b930929e221c2bdded"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 29607490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}