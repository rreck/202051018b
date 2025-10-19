```json
{
  "id": "aada48f6aaee0a5a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290499,
  "host_pid": "9e6742732c60:1",
  "hash": "a898fad5b39a9ff6717ea54d2b2fc7243d8fdcff4c90fdbc6a809dbef9f4383f",
  "cid": "QmV1a898fad5b39a9ff6717ea54d2b2fc7243d8fdcff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290499,
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
      "evaluated_at": 1760290499
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
  "sig": "e676ff0c43e9263dcf17c034b2503f235e54f87eba829a76b73523c2e34bd300"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247916716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 14287392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '297f10dabf118171'}}}