```json
{
  "id": "184e6d6672e4005f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287324,
  "host_pid": "9e6742732c60:1",
  "hash": "dcc0461c7d38dfb90491f5e18cba046a61de6524edec5d0962df72bf99d15e80",
  "cid": "QmV1dcc0461c7d38dfb90491f5e18cba046a61de6524",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287324,
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
      "evaluated_at": 1760287324
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
  "sig": "48c94eee1420eb352e9a54f9abe0da70d97f9811ad6a47ee0b35195c28a54835"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030330812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 11351312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285763, 'matching_hash': '72f4f50a1c3c0bfc'}}}