```json
{
  "id": "0e089eb492d68d24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294812,
  "host_pid": "9e6742732c60:1",
  "hash": "1005c29ad73b55b82fc11ee187cfa177c707da471775cf6fb9288a9be1184e87",
  "cid": "QmV11005c29ad73b55b82fc11ee187cfa177c707da47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294812,
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
      "evaluated_at": 1760294812
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
  "sig": "de656e48ca3578f832564aaade6f2eefea5b993703e316e86574b7dc15fb9277"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598152937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 61250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '12ca21f72ace6b8c'}}}