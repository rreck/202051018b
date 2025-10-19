```json
{
  "id": "a2edc428974f86b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290497,
  "host_pid": "9e6742732c60:1",
  "hash": "584327bc20415598922e3651f9f4c3a3490a60a78827dbf93c64f9833ebbed68",
  "cid": "QmV1584327bc20415598922e3651f9f4c3a3490a60a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290497,
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
      "evaluated_at": 1760290497
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
  "sig": "19885f176b7e00eeadbb19468918093ee457252e24bddccce4c81bf697529e23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155093747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 38000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '733cbbfa8b499b66'}}}