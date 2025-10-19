```json
{
  "id": "e727508381e39eda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294789,
  "host_pid": "9e6742732c60:1",
  "hash": "f64dc5854f60e0d8f5bc1a19f3d233d9f9cc04b128b02eb5e77d1718c506c48f",
  "cid": "QmV1f64dc5854f60e0d8f5bc1a19f3d233d9f9cc04b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294789,
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
      "evaluated_at": 1760294789
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
  "sig": "16736c1b04028cdb8fc470969b15760288f9f824edd4a5c7741aadf7ab83ff5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 21609616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}