```json
{
  "id": "a653ec14def93f77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294268,
  "host_pid": "9e6742732c60:1",
  "hash": "a12fe25054ec98e8569eb625245cb12e6d5abd17e5062bfda70e9c560708b85d",
  "cid": "QmV1a12fe25054ec98e8569eb625245cb12e6d5abd17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294268,
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
      "evaluated_at": 1760294269
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
  "sig": "bbeb29dde9ba1d61277d04f04c9896f533d7977a311e46abede709e915b77134"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 104704485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}