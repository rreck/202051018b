```json
{
  "id": "d46069374309c5ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290787,
  "host_pid": "9e6742732c60:1",
  "hash": "cbcd5dba5a6f99a820446c69ede01d862bcb15ba062852cef1832f0638ff237b",
  "cid": "QmV1cbcd5dba5a6f99a820446c69ede01d862bcb15ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290787,
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
      "evaluated_at": 1760290787
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
  "sig": "2d49a8ed7cb8d16e29055a6d420a770162ff1aa63ad7cb675ef4bdba4bdb7b26"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 77992044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}