```json
{
  "id": "5b0c5d166e727941",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293472,
  "host_pid": "9e6742732c60:1",
  "hash": "3b41b7e72cb6443a4de58def3b911345ccc308ec8da29ad952bd2252e204ac70",
  "cid": "QmV13b41b7e72cb6443a4de58def3b911345ccc308ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293472,
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
      "evaluated_at": 1760293472
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
  "sig": "3b2c0b27458538cad192a0df0a3a5faf2b90365d6b434480aa4ddc74b2b7c542"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277826130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 13714656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '6123129413abd06e'}}}