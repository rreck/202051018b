```json
{
  "id": "a0b8df523c764560",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290776,
  "host_pid": "9e6742732c60:1",
  "hash": "89d0efb6624408a337e6e79979b1f3d1fafbef629e40d83ce4691d523f89063c",
  "cid": "QmV189d0efb6624408a337e6e79979b1f3d1fafbef62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290776,
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
      "evaluated_at": 1760290776
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
  "sig": "3ae03d37f2962a12a5a15714e971c1f07d5c0e689cc71f49486487a0c2d4524d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 46536597, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}