```json
{
  "id": "c10d54799ce535bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291457,
  "host_pid": "9e6742732c60:1",
  "hash": "b35c65eca28e8fda33a196ea7711e830c60d3fa376c64bac7beadb71590a04ad",
  "cid": "QmV1b35c65eca28e8fda33a196ea7711e830c60d3fa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291457,
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
      "evaluated_at": 1760291457
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
  "sig": "1dffc32f8c9ff30d4fcc0404a8c10a53bb3b1b18fa231497bc6b94593c47774c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245748791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 34925100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': 'b01b0e655b1e1c55'}}}