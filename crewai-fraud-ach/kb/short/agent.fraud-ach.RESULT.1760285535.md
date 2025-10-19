```json
{
  "id": "b531c0cbe3a495ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285535,
  "host_pid": "9e6742732c60:1",
  "hash": "b556f935b69c0270b1e25e6f8bcd25e5b8be45c664821698bbac054b6104398c",
  "cid": "QmV1b556f935b69c0270b1e25e6f8bcd25e5b8be45c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285535,
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
      "evaluated_at": 1760285535
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
  "sig": "437d745d293412c819232fc5dc02a29f0354a4f951c2fd880698752a450e2ea9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246900677
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 23893210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760284979, 'matching_hash': '3c9e668125e5b467'}}}