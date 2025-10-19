```json
{
  "id": "e732ad4803067738",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292206,
  "host_pid": "9e6742732c60:1",
  "hash": "4889cae73fb7f000be6e3ff3ff0fbeadaac2f733ad5d469f0d2735d3df481279",
  "cid": "QmV14889cae73fb7f000be6e3ff3ff0fbeadaac2f733",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292206,
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
      "evaluated_at": 1760292206
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
  "sig": "4df91c7fe8940b7de73fbc8ae65c8bfbcd8f8629b9e452283432b89b40c0fd5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 70664448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}