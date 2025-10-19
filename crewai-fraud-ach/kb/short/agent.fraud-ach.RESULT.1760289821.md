```json
{
  "id": "9cb889100f283c52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289821,
  "host_pid": "9e6742732c60:1",
  "hash": "d8c1ac32c7af70c2af424b9acb0134424a6209ad8422a73e2f6cc4490b3db94f",
  "cid": "QmV1d8c1ac32c7af70c2af424b9acb0134424a6209ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289821,
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
      "evaluated_at": 1760289821
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
  "sig": "7e061c89d5dbe217cac81aeaa4d2aa2c801271f242329b22d3b49469b39a885b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022248507
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 52569540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': '9ba0ba747d27e727'}}}