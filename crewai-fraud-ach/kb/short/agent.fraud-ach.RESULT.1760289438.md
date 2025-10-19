```json
{
  "id": "3f1561be5be53414",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289438,
  "host_pid": "9e6742732c60:1",
  "hash": "c37f06847449753a860f1420a809324649f96d07be0225b72349ce4b092e8856",
  "cid": "QmV1c37f06847449753a860f1420a809324649f96d07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289438,
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
      "evaluated_at": 1760289438
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
  "sig": "de413c7637e7d5e06a2c6307172b66724ac26d75b9d2bfa9bd9e81bffa83630a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023360084
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 22002732, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': 'bfec758d4b349e38'}}}