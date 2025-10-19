```json
{
  "id": "89db21171dd57bd6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294300,
  "host_pid": "9e6742732c60:1",
  "hash": "ca2dec3429fa0c97b11fd469b9e758aa422711a2e38cb5eeb2d429626ee38be0",
  "cid": "QmV1ca2dec3429fa0c97b11fd469b9e758aa422711a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294300,
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
      "evaluated_at": 1760294300
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
  "sig": "11c37b5ac77d2e9e67b4bcd466849d281433c212bc30ee090e8be61897745521"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 20463330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}