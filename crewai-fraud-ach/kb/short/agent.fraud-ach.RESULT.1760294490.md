```json
{
  "id": "bb45a4c561145aa4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294490,
  "host_pid": "9e6742732c60:1",
  "hash": "3ca511fb11f4edc74e1508518479a3f31a5a74462006f20bba8e1068bffa316d",
  "cid": "QmV13ca511fb11f4edc74e1508518479a3f31a5a7446",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294490,
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
      "evaluated_at": 1760294490
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
  "sig": "66bbc58d017823c69848c927f87d2abf6c8b62235df77ea6daba76ec7f765f5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158076407
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 35502255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'bd01239b3993ff64'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}