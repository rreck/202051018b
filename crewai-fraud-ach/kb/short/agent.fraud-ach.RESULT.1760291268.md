```json
{
  "id": "4efdc82691cd8e88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291268,
  "host_pid": "9e6742732c60:1",
  "hash": "ffc8e272c8cadd646c414b47723541caf181261b00a44e65a1e4fc24448b16c8",
  "cid": "QmV1ffc8e272c8cadd646c414b47723541caf181261b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291268,
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
      "evaluated_at": 1760291268
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
  "sig": "18ae40a7d4702ec5ffff9194855211a89ee88c129e63567c7d55ffd6890c55ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021368470
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 30479382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': 'a5ef2cf235167f67'}}}