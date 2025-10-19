```json
{
  "id": "3325ad1ef49597f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289717,
  "host_pid": "9e6742732c60:1",
  "hash": "dc14e04520c07e3352653dc1656a972fc187b73121ba7a987433ffeffa7894fb",
  "cid": "QmV1dc14e04520c07e3352653dc1656a972fc187b731",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289717,
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
      "evaluated_at": 1760289717
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
  "sig": "9f5f03a557ca07163ef7e1ff15e93a94ebc98ed7c46f415b82450056e35e28e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156622392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 31498164, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '760602768636d516'}}}