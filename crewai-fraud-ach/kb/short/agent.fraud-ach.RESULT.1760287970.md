```json
{
  "id": "a27ee0d7bdf3679a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287970,
  "host_pid": "9e6742732c60:1",
  "hash": "f91c8130898ffce736c078d740dc2486bbe12b5ffbd69aabeb926440f73505e3",
  "cid": "QmV1f91c8130898ffce736c078d740dc2486bbe12b5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287970,
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
      "evaluated_at": 1760287970
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
  "sig": "b65f2d8bd8db6feca1edf18786a4dcef7a02a771eeb88832d635da276b7c7341"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 30591600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}