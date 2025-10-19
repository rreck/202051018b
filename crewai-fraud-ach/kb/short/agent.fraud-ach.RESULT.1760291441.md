```json
{
  "id": "fd84a551362bab27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291441,
  "host_pid": "9e6742732c60:1",
  "hash": "d5c57005364d080d6e6be2002666d6465829d076a3e95f30318b22231375598d",
  "cid": "QmV1d5c57005364d080d6e6be2002666d6465829d076",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291441,
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
      "evaluated_at": 1760291441
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
  "sig": "d7a8e6cb7610639015d55adf16dc47f8be2227a53e7200b5a0812c3663bd171b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 79573025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}