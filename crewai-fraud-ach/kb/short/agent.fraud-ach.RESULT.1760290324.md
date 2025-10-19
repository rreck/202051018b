```json
{
  "id": "8a1a7c7413d8862e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290324,
  "host_pid": "9e6742732c60:1",
  "hash": "f00009710431a6dc0449ec14377c8de7f295e9e8ca8b3df0ae2162fc9c428579",
  "cid": "QmV1f00009710431a6dc0449ec14377c8de7f295e9e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290324,
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
      "evaluated_at": 1760290324
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
  "sig": "928356df24be5da2bd20c0b305ba106435997441ad0ebdb224d81ea12eb1f4f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467895506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 23680671, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285764, 'matching_hash': 'b02327f98beb6712'}}}