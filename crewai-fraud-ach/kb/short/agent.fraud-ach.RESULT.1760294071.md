```json
{
  "id": "e660ce437650e5eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294071,
  "host_pid": "9e6742732c60:1",
  "hash": "c510678eb44ec0ed27c599fc779cc5ac81b14d41b6d9b1e31fb017197a4feac3",
  "cid": "QmV1c510678eb44ec0ed27c599fc779cc5ac81b14d41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294071,
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
      "evaluated_at": 1760294071
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
  "sig": "18273ea2b229442c5b36776ca55dc3cca3e3937e21030d8909490f308505935e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 88157916, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}