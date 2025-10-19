```json
{
  "id": "bfc10b4990875103",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286607,
  "host_pid": "9e6742732c60:1",
  "hash": "cc050b4df146bdf6f08cba0c6aeef42a5ce1ec893f8e1b0ba686a65e13283db2",
  "cid": "QmV1cc050b4df146bdf6f08cba0c6aeef42a5ce1ec89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286607,
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
      "evaluated_at": 1760286607
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d871cdfec464e131ec80cb95fc3f6bf720b6ab19af0d2be71a19ffe05db6e0e1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030505524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13933601, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': '58071665864a5dbb'}}}g number checksum'}}}