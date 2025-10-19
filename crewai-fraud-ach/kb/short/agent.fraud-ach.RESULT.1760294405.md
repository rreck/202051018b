```json
{
  "id": "ddf756a84a75945b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294405,
  "host_pid": "9e6742732c60:1",
  "hash": "d5623c9cbe6bfd01867cf7687b96511bc950bb49c7f8a34d1940b2e21f17ff94",
  "cid": "QmV1d5623c9cbe6bfd01867cf7687b96511bc950bb49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294405,
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
      "evaluated_at": 1760294405
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
  "sig": "c4bf0c963fcb4f11cc068db9b98aeba99a02159e9d68536a850aba3c485face4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 15323946, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}