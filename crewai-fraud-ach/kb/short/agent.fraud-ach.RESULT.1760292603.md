```json
{
  "id": "e9126453144daeee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292603,
  "host_pid": "9e6742732c60:1",
  "hash": "6af190f321e47a4924cc2ab6772eca470cd3b2b86e6b44f46302b7812733ebde",
  "cid": "QmV16af190f321e47a4924cc2ab6772eca470cd3b2b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292603,
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
      "evaluated_at": 1760292603
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
  "sig": "4d988db76b820ece438f5b85c34a3f80bb08cada73f03f73cd5ac3616f434a8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592473066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 65749311, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '48f07b8f6bc31034'}}}