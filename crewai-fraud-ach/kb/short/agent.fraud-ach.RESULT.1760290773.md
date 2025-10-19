```json
{
  "id": "7c50e669dc065b57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290773,
  "host_pid": "9e6742732c60:1",
  "hash": "4d59dcf32a7dea80f44a4cac9952856d08f4887226c2b832766085e50df5bcf5",
  "cid": "QmV14d59dcf32a7dea80f44a4cac9952856d08f48872",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290773,
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
      "evaluated_at": 1760290773
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
  "sig": "77d697f71fc73df776a984a559b7a870a270099457612c3aac9a67350ed93ff0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027960877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 51806652, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': '750facc395053d7c'}}}