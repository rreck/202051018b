```json
{
  "id": "9ada19bd9670a8c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291499,
  "host_pid": "9e6742732c60:1",
  "hash": "349bc913b43df11c76bbdae45aef64b92640746b5cad41f3bad9308e0574aa25",
  "cid": "QmV1349bc913b43df11c76bbdae45aef64b92640746b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291499,
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
      "evaluated_at": 1760291499
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
  "sig": "8e198a3a1219f41dcfaa339ab11afaa8c7c243bc5c3709cec1345fdfef134315"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463787734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 56549680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}