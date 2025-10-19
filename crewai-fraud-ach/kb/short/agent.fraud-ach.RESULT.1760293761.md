```json
{
  "id": "7413bd164f8c4a49",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293761,
  "host_pid": "9e6742732c60:1",
  "hash": "9164a438a0537767f687f3e0cdbf083d2428232cafde5f4c09c8aa190d25869c",
  "cid": "QmV19164a438a0537767f687f3e0cdbf083d2428232c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293761,
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
      "evaluated_at": 1760293761
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
  "sig": "89e8885239060107a028f7db76af4cb9fac53f6d03647379f4c169c41cc89860"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151550703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 86096250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '1af10bcd1b5a60d5'}}}