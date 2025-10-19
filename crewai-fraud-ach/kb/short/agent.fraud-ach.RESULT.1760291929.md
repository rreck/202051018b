```json
{
  "id": "9776401e04664f23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291929,
  "host_pid": "9e6742732c60:1",
  "hash": "9f825738a66e045e0249b618a619513d5e2ed4fc83abd8f48988e6a4fde78e7d",
  "cid": "QmV19f825738a66e045e0249b618a619513d5e2ed4fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291929,
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
      "evaluated_at": 1760291929
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
  "sig": "3f304179c67200811589c03865673ac0adeca7658dac23b3932739ed64aef3ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155322765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 79940382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}