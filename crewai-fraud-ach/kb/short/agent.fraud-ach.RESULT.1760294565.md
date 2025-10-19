```json
{
  "id": "49f09e150f60aaac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294565,
  "host_pid": "9e6742732c60:1",
  "hash": "41373cf07faf2d94364f8c4090516b71dd0823ddcd9d5f4fccfe3cb6e8419257",
  "cid": "QmV141373cf07faf2d94364f8c4090516b71dd0823dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294565,
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
      "evaluated_at": 1760294565
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
  "sig": "f84a319f2601a71505f29a0787ddeace8b35441a23493573e1a8ce9470662b0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 91431120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}