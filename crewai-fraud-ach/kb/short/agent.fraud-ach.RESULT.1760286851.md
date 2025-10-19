```json
{
  "id": "e9afb014d81cdc4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286851,
  "host_pid": "9e6742732c60:1",
  "hash": "a936152348dce646132ebd4cf605948c09fb88a3a8d1c73d58ad500efa28fa35",
  "cid": "QmV1a936152348dce646132ebd4cf605948c09fb88a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286851,
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
      "evaluated_at": 1760286851
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
  "sig": "f64bc6200300fee79c1e5b9a2a39316b9f10c0c0536bf6976f396bd3dffd1ee0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14353716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}