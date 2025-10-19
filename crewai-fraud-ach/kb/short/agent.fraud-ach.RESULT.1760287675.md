```json
{
  "id": "2e36575d41afccba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287675,
  "host_pid": "9e6742732c60:1",
  "hash": "bcd4265924d8d6d11273d6be2fde40a3db5eaa5e0a51da4cd3c1938e7918d540",
  "cid": "QmV1bcd4265924d8d6d11273d6be2fde40a3db5eaa5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287675,
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
      "evaluated_at": 1760287675
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
  "sig": "fce1230defc1c67ad1b590970e87e67c86b4fa9532c219706bf325e997727521"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462224628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 15843320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '4ca3be34af08dccb'}}}