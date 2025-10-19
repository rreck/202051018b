```json
{
  "id": "f983fab8012e2cd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292369,
  "host_pid": "9e6742732c60:1",
  "hash": "e54ddfdb6c9f19471e5743558ab7476b8c9be5887af952e6c0ddeb1b4cefdec2",
  "cid": "QmV1e54ddfdb6c9f19471e5743558ab7476b8c9be588",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292369,
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
      "evaluated_at": 1760292369
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
  "sig": "25c762efe60017c3e4936d889f6c711dbb39cabc696f1dbf4bcc376b678c8df5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 37339372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}