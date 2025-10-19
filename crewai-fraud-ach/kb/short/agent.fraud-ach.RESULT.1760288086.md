```json
{
  "id": "d3054c3c8d9f071e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288086,
  "host_pid": "9e6742732c60:1",
  "hash": "d339b2f23fcf7e82c7612fb944f64433cbd761b5b112d188fe70836e2087f199",
  "cid": "QmV1d339b2f23fcf7e82c7612fb944f64433cbd761b5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288086,
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
      "evaluated_at": 1760288086
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
  "sig": "337abd49d97ca4a3ba8dc17011c8ca0d27279d27c7b0382cedb6c4f2343f7959"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247969582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 78177294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}uting_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}