```json
{
  "id": "04a79c9090e3520c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289928,
  "host_pid": "9e6742732c60:1",
  "hash": "d68e6e8fb626e55d4aa5fab04330cb533bb39ec07135a3fe1844d0aeb012163f",
  "cid": "QmV1d68e6e8fb626e55d4aa5fab04330cb533bb39ec0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289928,
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
      "evaluated_at": 1760289928
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
  "sig": "f3a0812a88559e98d5096f11a83ef88d4fc92943bb1d31991fa4d218699ef1ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154786749
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 60163687, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '09892425b2f11015'}}}