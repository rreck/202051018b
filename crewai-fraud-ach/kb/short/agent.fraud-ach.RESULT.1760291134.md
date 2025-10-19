```json
{
  "id": "9333fae64bf4bddd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291134,
  "host_pid": "9e6742732c60:1",
  "hash": "023ba473f5a73939804fc6eefc42608b2118d6deddffb7d68f2bfcea6b442e5a",
  "cid": "QmV1023ba473f5a73939804fc6eefc42608b2118d6de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291134,
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
      "evaluated_at": 1760291134
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "d7effda68a9e5ec03ab22cb0858b711c0d83cfe62a647c36d726c71b90987077"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000020453252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 84000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '94693ae2b8a79c3a'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}