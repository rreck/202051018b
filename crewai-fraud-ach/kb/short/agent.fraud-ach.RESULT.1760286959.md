```json
{
  "id": "20af0b647d8fe96e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286959,
  "host_pid": "9e6742732c60:1",
  "hash": "1c574048292377790472c83737118617f7ae8035b820b69ce2b50bb73d9e1b86",
  "cid": "QmV11c574048292377790472c83737118617f7ae8035",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286959,
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
      "evaluated_at": 1760286959
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
  "sig": "8f73fa221a731c0aa5fe2ca0cc02eab396feb413bd12fcd13bc1d2b8405fa839"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025207502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18888696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285765, 'matching_hash': 'b87463fc74d5c9ed'}}}