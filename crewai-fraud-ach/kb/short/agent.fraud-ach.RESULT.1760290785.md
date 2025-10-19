```json
{
  "id": "9daa8c63a33089ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290785,
  "host_pid": "9e6742732c60:1",
  "hash": "0d8b644265cc3357f4e9f3bd28033a2946cea40f60ecfd96c100f03789898da3",
  "cid": "QmV10d8b644265cc3357f4e9f3bd28033a2946cea40f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290785,
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
      "evaluated_at": 1760290785
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
  "sig": "2149345d02ce9966ef0105e5a4f5354315726ec91888f9f572da0f598a82a139"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242027891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 22189245, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}