```json
{
  "id": "e7aa06785a7466d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290792,
  "host_pid": "9e6742732c60:1",
  "hash": "33f1ee4795b093c949bbea5f73192c7d3b753e5fe47a1c59bcb0da960a583d6c",
  "cid": "QmV133f1ee4795b093c949bbea5f73192c7d3b753e5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290792,
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
      "evaluated_at": 1760290792
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
  "sig": "66a6ad4f88841399952dc0f36cf133ec7c64b3e85af6c2be52c92f6fb7f54be4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032270621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 36685752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '380f2fccd8369f51'}}}