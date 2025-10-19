```json
{
  "id": "0478597498a7f67a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294075,
  "host_pid": "9e6742732c60:1",
  "hash": "bcc97bfc1b54b6308b956a3ee72f2a7b1b44c0ac01e9eff8f54ae3639a7c2821",
  "cid": "QmV1bcc97bfc1b54b6308b956a3ee72f2a7b1b44c0ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294075,
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
      "evaluated_at": 1760294075
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
  "sig": "a329089a106dccd857636452b6268013592bfa92f51b1e1495e44ad2b4ce2015"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030199431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 111366948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '86eebb6c1a57e398'}}}