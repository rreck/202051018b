```json
{
  "id": "c1687f840dd082b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292054,
  "host_pid": "9e6742732c60:1",
  "hash": "c910d6c4ee001ee590d441311db48e9680aaf439c67dbb658fef1a97f77fe9e8",
  "cid": "QmV1c910d6c4ee001ee590d441311db48e9680aaf439",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292054,
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
      "evaluated_at": 1760292054
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
  "sig": "993765cf238c1ef2d5626a185eb945058f72d7ebe1acd04e966acb94b001dc86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 74918655, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}