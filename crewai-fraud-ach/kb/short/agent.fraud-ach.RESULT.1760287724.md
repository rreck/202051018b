```json
{
  "id": "4fe17f3ba1b14cd5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287724,
  "host_pid": "9e6742732c60:1",
  "hash": "9b5e6d4d3518ea2ee79891708e61f9edb8a3b45b85cd7d2c200c87e1a50453bc",
  "cid": "QmV19b5e6d4d3518ea2ee79891708e61f9edb8a3b45b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287724,
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
      "evaluated_at": 1760287724
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
  "sig": "08471b1164db18c003ab0e572b52b672842d2a8fcb3775c7ccde7db40bbc19a3"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 111000023553215
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 27411930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': '85da211728f5a38f'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}