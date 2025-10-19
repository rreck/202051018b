```json
{
  "id": "5ae9121e1f304ada",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294227,
  "host_pid": "9e6742732c60:1",
  "hash": "079423bb95bea0302482c55e6a5d61d31bdacc74af3a9679b50da353dbaa6317",
  "cid": "QmV1079423bb95bea0302482c55e6a5d61d31bdacc74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294227,
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
      "evaluated_at": 1760294227
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
  "sig": "f07c367a67b9908a7624bee98bce625ac4a73ac1ee8d61ce7b78547f991e54cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596829725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 77328576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '14fa64c7f7d5a53d'}}}}