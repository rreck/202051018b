```json
{
  "id": "daf4ea9ddcaa1d97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291935,
  "host_pid": "9e6742732c60:1",
  "hash": "158bcaa8f8139f87e2da39fd3a99b2b7a4c6e9a7a88578ff969ce53cf60ab69b",
  "cid": "QmV1158bcaa8f8139f87e2da39fd3a99b2b7a4c6e9a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291935,
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
      "evaluated_at": 1760291935
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
  "sig": "707a1664afe53fe74e1f9546830a535044e773c398959cdf0daae554bf6f0d05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 85334754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}