```json
{
  "id": "d723c15830b24448",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286869,
  "host_pid": "9e6742732c60:1",
  "hash": "4c340a41d391830c72e4f89c84d910e7826ce29b11da4cbb5d3d87638798083a",
  "cid": "QmV14c340a41d391830c72e4f89c84d910e7826ce29b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286869,
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
      "evaluated_at": 1760286869
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "651c8b6eaf19cd10a793d4924d285eb2180c251c0647b252343172985a748f07"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000028475138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13296000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285763, 'matching_hash': 'fd3dd6a8db70ef91'}}}