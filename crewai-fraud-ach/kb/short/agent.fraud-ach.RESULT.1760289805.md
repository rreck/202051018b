```json
{
  "id": "e78af0334f726ba2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289805,
  "host_pid": "9e6742732c60:1",
  "hash": "210bced7b2fbf5995ee21913bf507a927cf4fab6cd5cabad4e21ed0862f09578",
  "cid": "QmV1210bced7b2fbf5995ee21913bf507a927cf4fab6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289805,
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
      "evaluated_at": 1760289805
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
  "sig": "a5c33980c9e93fc4909302f3026ee8e83051138e7b3753de95b21cd6e5664597"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150741223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 53089344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': '3a8aff16771fc05f'}}}