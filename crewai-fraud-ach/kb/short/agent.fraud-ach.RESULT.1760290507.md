```json
{
  "id": "69e1681d1c51deac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290507,
  "host_pid": "9e6742732c60:1",
  "hash": "f2776fc7c1c352c8ec41c96b00ada9bc5d8602683dc20f54b53aa88a623279d0",
  "cid": "QmV1f2776fc7c1c352c8ec41c96b00ada9bc5d860268",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290507,
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
      "evaluated_at": 1760290507
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
  "sig": "fe1339fba45966d316b6504e4068a389d06315f2cd66c8d8af6fcb4bb2cb5926"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 68751880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}