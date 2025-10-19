```json
{
  "id": "11e45f44ff0e3c43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293372,
  "host_pid": "9e6742732c60:1",
  "hash": "7a846ceef99cef43a27bcaaba32fc95c93d2a55e510a5a4f40abc8fc38958425",
  "cid": "QmV17a846ceef99cef43a27bcaaba32fc95c93d2a55e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293372,
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
      "evaluated_at": 1760293372
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
  "sig": "b8e7ee24a22923789dd58cc07d0795856b4492bff400e21b128092a35aee8089"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027363246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 25140752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}