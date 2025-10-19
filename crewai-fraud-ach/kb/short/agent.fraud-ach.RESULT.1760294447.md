```json
{
  "id": "430f1ceeb48392b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294447,
  "host_pid": "9e6742732c60:1",
  "hash": "7db335fa78cf23bbfe6a82f2f2a4bf50887d66a0cf0b33dc29b941a3b1a1b476",
  "cid": "QmV17db335fa78cf23bbfe6a82f2f2a4bf50887d66a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294447,
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
      "evaluated_at": 1760294447
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
  "sig": "81f6085da496bf7f967654bfdc5219aa59a14b78cf4c7c7e128e6be6ce3dd215"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022462179
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 96586350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'b017d6ab8abfffc0'}}}}