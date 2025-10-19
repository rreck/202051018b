```json
{
  "id": "a21ef5133a98ce7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288438,
  "host_pid": "9e6742732c60:1",
  "hash": "71b6ee43e78dd5887fd060eacac7d739499e4ecbc7bad41ccf0099b3c0a8accd",
  "cid": "QmV171b6ee43e78dd5887fd060eacac7d739499e4ecb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288438,
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
      "evaluated_at": 1760288438
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
  "sig": "4cf1a71df25dbad525a29fbb18c102fdea35761b9e39d3b180d022729dccc79f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271527804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 45731820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': '5c006846cf6d606a'}}}