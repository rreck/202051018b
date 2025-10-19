```json
{
  "id": "4a16eb154a1ef8f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289988,
  "host_pid": "9e6742732c60:1",
  "hash": "9fee7b534ca468f6dc8226eda203e1dc2c785f78812695a1c71bc95c4a2a1794",
  "cid": "QmV19fee7b534ca468f6dc8226eda203e1dc2c785f78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289988,
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
      "evaluated_at": 1760289988
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
  "sig": "284b5a7372270ce4df8df3c03872119c913624e3de052e5bb7842ba034678122"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 66890394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}