```json
{
  "id": "9a11dccc638db5c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287497,
  "host_pid": "9e6742732c60:1",
  "hash": "05925f4973fb93a7ec8d1cf2664fa9a8025e5909f520041f7eb1ec0a81bee1bd",
  "cid": "QmV105925f4973fb93a7ec8d1cf2664fa9a8025e5909",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287497,
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
      "evaluated_at": 1760287497
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "3c1addfca66df1a2b9e1939cf72763442233bacf41cdf58f66d7bdf2fa57dc8a"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 122105159548599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285764, 'matching_hash': '3450667ce2814f1a'}}}