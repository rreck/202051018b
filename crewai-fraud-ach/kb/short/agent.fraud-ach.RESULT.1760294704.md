```json
{
  "id": "2326bc11fc72235c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294704,
  "host_pid": "9e6742732c60:1",
  "hash": "4fa56f38cfa4ece62b69c81f5aafcc9b5c7392a8cdeb46c4825cf0d8ad5a3226",
  "cid": "QmV14fa56f38cfa4ece62b69c81f5aafcc9b5c7392a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294704,
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
      "evaluated_at": 1760294704
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
  "sig": "85bf1de1ecbbd6ec4faee6b2f5789a4826240256339c27ed52e133806a17afb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278849424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 69614397, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}