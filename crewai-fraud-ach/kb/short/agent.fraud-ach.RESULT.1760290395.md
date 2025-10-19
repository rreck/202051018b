```json
{
  "id": "e4f4f66354f6b8d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290395,
  "host_pid": "9e6742732c60:1",
  "hash": "93c90679bfcde61633c73b675f3f49fb307b5ef1fd327c38efc093f395945064",
  "cid": "QmV193c90679bfcde61633c73b675f3f49fb307b5ef1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290395,
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
      "evaluated_at": 1760290395
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
  "sig": "8a1f8ab3878be7cd1149b505e625378003b683bac5d04baefef60eebd325c173"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594873577
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 90641475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760284979, 'matching_hash': '5add1f4a09a12b51'}}}