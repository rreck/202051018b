```json
{
  "id": "bcb0e6fa28741e56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292649,
  "host_pid": "9e6742732c60:1",
  "hash": "68f179cef55eaf6b32cf141afec86c9a2b0b7868871c07d214a5f527ed85a4bd",
  "cid": "QmV168f179cef55eaf6b32cf141afec86c9a2b0b7868",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292649,
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
      "evaluated_at": 1760292649
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
  "sig": "8838bf6d5ab722c32dcb37e4c60f365099d9f9bd004bc69d4ae8b64c24f19311"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154730054
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 54390520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '3072a79f51416ab8'}}}