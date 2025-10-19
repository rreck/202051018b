```json
{
  "id": "daeb7abbd53ddc7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290797,
  "host_pid": "9e6742732c60:1",
  "hash": "936d74c28d4e354b6cdc33008ebde9d004d380e9b480b4ca7cfa482dc0bfc89e",
  "cid": "QmV1936d74c28d4e354b6cdc33008ebde9d004d380e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290797,
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
      "evaluated_at": 1760290797
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
  "sig": "223756cf8dc3d7cb911dfb83e3feb2aac235504545a2317e1d39ecdf1e6f599c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028263855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 39750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': 'de539bef65b21552'}}}