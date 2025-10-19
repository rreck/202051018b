```json
{
  "id": "53a1d59ac97f4dc6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291076,
  "host_pid": "9e6742732c60:1",
  "hash": "f3e5c225dac3d257072e361b222558c8dad6f2d73d53f34bd68a7bde408dda46",
  "cid": "QmV1f3e5c225dac3d257072e361b222558c8dad6f2d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291076,
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
      "evaluated_at": 1760291076
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
  "sig": "ca326031e3f75e9dfd2e1e7345216b869c0d34a05903e8fff5207b8aff246fc4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 13991642, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}