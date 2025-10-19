```json
{
  "id": "d5dff72d66a73b0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293801,
  "host_pid": "9e6742732c60:1",
  "hash": "d14ea80ba2fd4b48f45dfebff8574b75cb2977c9758cc064236bb41631d99986",
  "cid": "QmV1d14ea80ba2fd4b48f45dfebff8574b75cb2977c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293801,
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
      "evaluated_at": 1760293801
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
  "sig": "1093eb891008fb6d5d838e12d511f7253bc78a72feb3c81feb2bb24acdc40c23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 65883068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '12aaf4f6bb764c37'}}}