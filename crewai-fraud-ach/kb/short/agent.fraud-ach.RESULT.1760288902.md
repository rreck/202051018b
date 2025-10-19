```json
{
  "id": "be4b6df8a282bedd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288902,
  "host_pid": "9e6742732c60:1",
  "hash": "dc5689fdd3fc29d7b627d108e6461e23b380324441fd909564efbe66a04f454e",
  "cid": "QmV1dc5689fdd3fc29d7b627d108e6461e23b3803244",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288902,
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
      "evaluated_at": 1760288902
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
  "sig": "7621a6bbd08e688ddabd9e1b00b96c3ab676642c9158629c45114132e2d2361f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 45104994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}