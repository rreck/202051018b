```json
{
  "id": "5b1bcb8a7fff38f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291492,
  "host_pid": "9e6742732c60:1",
  "hash": "fa11dd2a28edee465eb12b8d55c1c2de0ac6776bf4ad346d1e0211320370138b",
  "cid": "QmV1fa11dd2a28edee465eb12b8d55c1c2de0ac6776b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291492,
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
      "evaluated_at": 1760291492
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
  "sig": "574f990a073435067545be336ca7b3a2ccb35fac9f460ff313a5544832651b6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026184073
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 54950896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '5c433365b4c36f89'}}}